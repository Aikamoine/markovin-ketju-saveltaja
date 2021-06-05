"""
Midilukija-luokka
"""

import os
from mido import MidiFile

AANET = {
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11
}


class Midilukija:
    """
    Olio, joka osaa lukea Midi-tiedostosta soitindataa

    tiedosto = MidiFile-olento, joka sisältää kulloinkin avatun tiedoston
    luettuja_tiedostoja = käsiteltyjen tiedostojen määrä
    luettuja_savelia = käsiteltyjen sävelten määrä
    """

    def __init__(self):
        """
        Konstruktori
        """
        self.tiedosto = None
        self.luettuja_tiedostoja = 0
        self.luettuja_savelia = 0

    def avaa_tiedosto(self, tiedosto):
        """
        Alustaa tiedoston mukaisesta polusta MidiFile-olennon

        args:
            tiedosto: avattavan tiedoston suhteellinen polku
        """
        self.tiedosto = MidiFile(tiedosto)
        self.luettuja_tiedostoja += 1

    def tulosta_tiedoston_aanet(self):
        """
        Tulostaa terminaaliin kaikki tiedostossa soitettujen äänien sävelen
        """
        for i, raita in enumerate(self.tiedosto.tracks):
            print(f"Raita {i}: {raita.name}")
            soitetut_aanet = 0
            for viesti in raita:
                if not viesti.is_meta:
                    if viesti.type == "note_on":
                        print(viesti.note)
                        soitetut_aanet += 1
            print(f"Soitetut sävelet: {soitetut_aanet}")

    def tallenna_midin_tapahtumat(self, polku):
        """
        Tallentaa tiedoston kaikki tapahtumat tekstitiedostoon

        args:
            polku: uuden tiedoston nimi
        """
        for tiedosto in os.listdir(polku):
            if tiedosto.endswith(".mid"):
                self.avaa_tiedosto(polku+tiedosto)
                with open(f"{polku}{tiedosto[:-4]}.txt", 'w') as kirjoitettava:
                    for i, raita in enumerate(self.tiedosto.tracks):
                        kirjoitettava.write(f'Raita {i}: {raita.name}\n')
                        for msg in raita:
                            kirjoitettava.write(f"{msg}\n")

    def palauta_raidan_aanet(self, raita, raidan_savel, savellaji):
        """
        Syöttää taulukkoon kaikki yhdellä midi-raidalla olevat soitetut sävelet
        Lopullinen ääni on laskutoimituksen tulos: alkuperäinen ääni transponoidaan
        C-säveleen, minkä jälkeen sitä kasvatetaan halutun sävellajin verran
        args:
            raita: raita midi-tiedostossa
            raidan_savel: luettavan sävellyksen sävellaji
            savellaji: nyt luotavan sävellyksen sävellaji
        """
        aanet = []
        for viesti in raita:
            if not viesti.is_meta:
                if viesti.type == "note_on":
                    aani = viesti.note - savellaji.aanelle_indeksi(raidan_savel) + savellaji.savel_indeksi
                    aanet.append(aani)
                    self.luettuja_savelia += 1
        return aanet

    def tarkista_savellaji(self, raita):  # pylint: disable=no-self-use
        """
        Lukee midiraidan läpi ja palauttaa siellä mainitun sävellajin

        args:
            raita: MidiFilen Track-olio
        """
        for viesti in raita:
            if viesti.type == "key_signature":
                return viesti.key
        return "Ei säveltä"

    def tallenna_polku_trieen(self, polku, trie, savellaji):
        """
        Tallentaa kaikkien polussa olevien midi-tiedostojen soitetut sävelet trie-tietorakenteeseen

        args:
            polku: suhteellinen polku kansioon, jonka tiedostot luetaan
            trie: Trie-olio, johon tiedot tallennetaan
            savellaji: sävelmän sävellaji
        """
        for tiedosto in os.listdir(polku):
            if tiedosto.endswith(".mid"):

                self.avaa_tiedosto(polku + tiedosto)
                for raita in self.tiedosto.tracks:
                    raidan_savellaji = self.tarkista_savellaji(raita)

                    if raidan_savellaji == "Ei säveltä":
                        continue

                    if (raidan_savellaji[-1] == "m") == savellaji.onko_molli():
                        # Raidan molli-duuri -status on tarkastettu, enää kiinnostaa sävel
                        raidan_savellaji = raidan_savellaji.split("m")[0]
                        aanet = self.palauta_raidan_aanet(
                            raita, raidan_savellaji, savellaji)
                        trie.lisaa_aanet_trieen(aanet)

        print(f"Luettu {self.luettuja_tiedostoja} tiedostoa")
        print(f"Niistä kelpuutettu {self.luettuja_savelia} säveltä")
