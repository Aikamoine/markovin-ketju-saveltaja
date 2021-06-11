"""
Käyttöliittymästä vastaava luokka
"""

from random import Random
from datetime import datetime
from trie.trie import Trie
from markovin_ketjut.markov_savelma import MarkovSavelma
from midiluokat.midikirjoittaja import Midikirjoittaja
from midiluokat.midilukija import Midilukija
from musiikkiluokat.savellaji import Savellaji
from musiikkiluokat.tempo import Tempo

class UI:
    """
    Luokka käyttäjän syötteiden validointiin
    """

    def __init__(self):
        self.savelet = ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
        self.datapolku = "src//musiikkidata//"

    def aloita(self):
        self.tervetuloa()

        self.valitse_toiminto()

    def tervetuloa(self):
        print()
        print("Tällä sovelluksella pääset luomaan mahtavia musikaalisia elämyksiä.")
        print("Aluksi sovellus kysyy sinulta parametreja kappaleen luontiin.\n")
        print("Jokaisen syötteen kohdalla voit lopettaa kirjoittamalla 'exit'\n")
        print("Jos teet virheen kirjoittaessa, niin backspace tai delete eivät toimi.")
        print("Sen sijaan voit kirjoittaa jotain hölynpölyä ja painaa enter - "+
              "pääset aloittamaan syötteen alusta\n")

    def valitse_toiminto(self):
        while True:
            print("Tyhjä syöte aloittaa perustoiminallisuuden, " +
                "voit kirjoittaa 'test' suorituskykytestiin. 'exit' lopettaa ohjelman.")
            syote = input()
            
            if syote == "":
                self.tee_savellys()
            if syote == "test":
                self.suorituskykytestaus()
            if syote == "exit":
                break
            print()

    def tee_savellys(self):
        syvyys = self.kysy_syvyys()
        trie = Trie(syvyys)
        savellaji = self.kysy_savel()

        lukija = Midilukija()
        lukija.tallenna_polku_trieen(self.datapolku, trie, savellaji)

        trie.tallenna()
        print()

        tempo = Tempo(self.kysy_tempo())
        arpoja = Random()
        tahteja = self.kysy_tahdit()

        markov = MarkovSavelma(trie, tempo, savellaji, arpoja)

        markov.luo_savellys(tahteja)
        print()

        midi = Midikirjoittaja()
        midi.kirjoita_aanet_uuteen_raitaan(0, markov.savelma, "Melodia")
        midi.kirjoita_aanet_uuteen_raitaan(0, markov.harmonia, "Harmonia")
        midi.kirjoita_tiedosto()

    def suorituskykytestaus(self):
        """
        Tallentaa yhteen Trie-rakenteeseen kaikki polusta löytyvät jokaiselle sävellajille.
        Yhteensä käsittelyitä siis tehdään lähdemateriaalin määrä * 17.
        Suorituksen kesto ajastetaan.
        """
        lukija = Midilukija()

        aloitus = datetime.now()

        for savel in self.savelet:
            syvyys = 5
            trie = Trie(syvyys + 1)
            if syvyys % 2 == 0:
                savellaji = Savellaji(True, savel)
            else:
                savellaji = Savellaji(False, savel)
            
            lukija.tallenna_polku_trieen(self.datapolku, trie, savellaji)

            syvyys += 1
        kesto = datetime.now() - aloitus

        print(f"Testi kesti yhteensä {kesto} aikayksikköä")

    def _syotteesta_numero(self, minimi, maksimi):
        """Kysyy käyttäjältä syötettä, kunnes tämä antaa numeroarvon minimin ja maximin väliltä
           Palauttaa syötteen kokonaislukuarvon
        Args:
            min: kokonaisluku
            max: kokonaisluku
        """
        while True:
            syote = input()
            if syote.isnumeric():
                luku = int(syote)
                if luku < minimi:
                    print("Liian pieni arvo")
                elif luku > maksimi:
                    print("Liian suuri arvo")
                else:
                    print()
                    return luku
            if syote == "exit":
                exit()

    def kysy_syvyys(self):
        print("Anna Markovin ketjun suurin mahdollinen aste. Suositus on väliltä 4 - 10.")
        return self._syotteesta_numero(1, 15)

    def onko_molli(self):
        print("Tehdäänkö sävelmä mollissa vai duurissa? Kirjoita molli, tai duuri")
        molli = False
        while True:
            syote = input()
            if syote == "molli":
                molli = True
                break
            if syote == "duuri":
                molli = False
                break
            if syote == "exit":
                exit()
        print()
        return molli

    def kysy_savel(self):
        molli = self.onko_molli()

        print("Missä sävelessä sävelmä tehdään? Vaihtoehdot ovat:")
        print(self.savelet)

        #savelet = self.savelet.replace(" ", "")
        #savelet = savelet.split(",")
        while True:
            syote = input()
            if syote in self.savelet:
                break
            if syote == "exit":
                exit()
        print()
        return Savellaji(molli, syote)

    def kysy_tempo(self):
        print("Anna tempo. Suositus on 120 - 150.")
        print("Huom! Midi-standardin rajoitteista johtuen kaikki temmot eivät toimi yhtä hyvin.")
        print("Suositeltuja tempoja ovat esim. 80, 100, 120, 150, 200")
        return self._syotteesta_numero(50, 250)

    def kysy_tahdit(self):
        print("Anna sävelmän tahtien määrä. Toistaiseksi tuetaan vain 4/4-rakennetta.")
        return self._syotteesta_numero(1, 30)
