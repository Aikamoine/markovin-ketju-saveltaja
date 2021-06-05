"""
MarkovSavelma-luokka
"""

from musiikkiluokat.savel import Savel
from markovin_ketjut.pituusarpoja import Pituusarpoja
from markovin_ketjut.korkeusarpoja import Korkeusarpoja


class MarkovSavelma():
    """
    Markovin ketjulla sävelmiä luova olio

    trie: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
    savelma: taulukko Säveliä
    pituusarpoja: Pituusarpoja-olio nuottien pituuksien generointiin
    korkeusarpoja: Korkeusarpoja-olio nuottien korkeuksien generointiin
    tempo: Tempo-olio nuottien pituuksien ja todellisten pituuksien tulkintaan
    arpoja: Random-luokan olio
    savellaji: sävelmän sävellaji
    """

    def __init__(self, opetusaineisto, tempo, savellaji, arpoja):
        """
        Konstruktori

        Args:
            opetusaineisto: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
            tempo: Tempo-olio
            savellaji: Savellaji-olio, joka sisältää käyttäjän määrittämän sävellajin
            arpoja: Random-luokan olio
        """
        self.trie = opetusaineisto
        self.savelma = []
        self.harmonia = []
        self.pituusarpoja = Pituusarpoja(arpoja)
        self.korkeusarpoja = Korkeusarpoja(arpoja)
        self.tempo = tempo
        self.arpoja = arpoja
        self.savellaji = savellaji

    def luo_savellys(self, tahteja):
        """
        Luo sävellyksen triestä ääniä generoimalla. Triestä pyritään aina hakemaan mahdollisimman
        korkean asteen yhtenevyys. Jos sellaista ei löydy, tiputetaan haettavasta sävelmästä yksi
        ääni kerrallaan pois

        args:
            tahteja: kuinka monta tahtia halutaan yhteensä generoida
        """
        for i in range(tahteja):
            #Lisätään tahdin ensimmäinen ääni silmukan ulkopuolella, niin saadaan harmoniaääni tahdin alkuun
            seuraava = self._seuraava_solmu()
            tahdissa_jaljella = self._lisaa_savelmaan(
                seuraava, 16)

            self._lisaa_harmonia()

            while tahdissa_jaljella > 0:
                seuraava = self._seuraava_solmu()

                tahdissa_jaljella = self._lisaa_savelmaan(
                    seuraava, tahdissa_jaljella)

            print(f"Tahti {i + 1} kirjoitettu\n")

        self._lisaa_loppusointu()

    def _seuraava_solmu(self):
        """
        Hakee triestä seuraavan solmun, joka vastaa mahdollismman suurta
        astetta kirjoitetun sävelmän lopusta nähden.
        """

        kaytettava_savelma = self.savelma[-self.trie.maksimisyvyys + 1:]
        while True:
            self._tulosta_etsittava_savelma(kaytettava_savelma)
            seuraava = self.trie.loyda_seuraava_solmu(
                kaytettava_savelma)

            if seuraava is None or len(seuraava.lapset) == 0:
                kaytettava_savelma = kaytettava_savelma[1:]
            else:
                break
        return seuraava

    def _lisaa_savelmaan(self, seuraava, tahdissa_jaljella):
        """Arpoo parametrina saadulle äänelle korkeuden ja pituuden, lisää sen sitten sävelmään.
           Palauttaa tahdissa lisäyksen vapaana olevien kuudestoistaosien määrän
        Args:
            seuraava: Aani, joka tullaan lisäämään
            tahdissa_jaljella: Kuinka monta kuudestoistaosaa nykyisessä tahdissa on vielä jäljellä.
        """
        uusi_aani = self._arvo_solmu(seuraava.lapset).aani
        print(f"Ääni: {uusi_aani}")

        aanenkorkeus = self._arvo_korkeus()

        arvottu_pituus = self._arvo_pituus(tahdissa_jaljella)
        aanenpituus = self.tempo.get_aanen_pituus(arvottu_pituus)

        uusi_savel = Savel(uusi_aani.aani_luku +
                           aanenkorkeus, aanenpituus)
        self.savelma.append(uusi_savel)
        #print(str(self))
        print()

        return tahdissa_jaljella - (16 / (2**arvottu_pituus))

    def _lisaa_harmonia(self):
        """
        Viimeksi lisätyn äänen perusteella tehdään kokonuotin pituinen harmoniaääni
        Jos edellinen ääni on korkea (yli 4), lisätään sitä 7 intervallia matalampi ääni
        Jos edellinen ääni on matala, lisätään sitä 5 intervallia korkeampi ääni
        """
        edellinen = self.savelma[-1]
        edellinen_savel = edellinen.aani.aani_luku
        pituus = self.tempo.get_aanen_pituus(0)
        if edellinen.korkeus <= 3:
            uusi = Savel(4 * 12 + edellinen_savel + 5, pituus)
        else:
            uusi = Savel(edellinen.korkeus * 12 + edellinen_savel - 7, pituus)

        print(f"Lisätään harmoniaan ääni: {uusi}\n")
        self.harmonia.append(uusi)

    def _lisaa_loppusointu(self):
        """
        Lisää sävellajin perusteella viimeiseksi ääneksi pitkän soinnun.
        Näin sävelmä kuulosta enemmän loppuneelta
        Lisätään korkean viimeisen äänen perään oktaavia matalampi ääni.
        Matalan äänen perään lisätään 4-oktaavilta
        """
        edellinen_korkeus = self.harmonia[-1].korkeus
        if edellinen_korkeus > 5:
            korkeuskerroin = edellinen_korkeus - 1
        else:
            korkeuskerroin = 5

        juurinuotti = self.savellaji.savel_indeksi + (12 * korkeuskerroin)

        if self.savellaji.onko_molli():
            terssi = juurinuotti + 3
        else:
            terssi = juurinuotti + 4

        pituus = self.tempo.get_aanen_pituus(0)
        self.savelma.append(Savel(juurinuotti, pituus))
        self.harmonia.append(Savel(terssi, pituus))
        print("Lisätty loppusointu\n")

    def _tulosta_etsittava_savelma(self, savelma):  # pylint: disable=no-self-use
        """
        Tulostaa komentoriville seuraavaksi triestä etsittävän sävelmän

        args:
            savelma: osataulukko self.savelma -oliomuuttujasta
        """
        printtaus = ""
        for savel in savelma:
            printtaus += str(savel) + ","

        print(f"Etsitään seuraava ääni sävelmälle: {printtaus}")

    def _arvo_solmu(self, vaihtoehdot):  # pylint: disable=no-self-use
        """
        Laskee vaihtoehtojen jakauman ja sen perusteella arpoo yhden solmun

        args:
            vaihtoehdot: taulukko Solmuja
        """
        yhteensa = 0
        jakauma = [None]*len(vaihtoehdot)

        for i, vaihtoehto in enumerate(vaihtoehdot):
            yhteensa += vaihtoehto.maara
            jakauma[i] = vaihtoehto.maara

        arvottu = self.arpoja.randint(0, yhteensa)

        for i, vaihtoehto in enumerate(vaihtoehdot):
            if jakauma[i] >= arvottu:
                return vaihtoehto
            arvottu -= jakauma[i]
        return vaihtoehdot[-1]

    def _arvo_korkeus(self):
        """
        Arpoo sävelen korkeuden viimeisimmän sävelmään talletetun sävelen perusteella
        Esim. D-äänen indeksi on 2, joten D4 = 5 * 12 + 2 = 62 (äänet alkavat -1:stä, siksi 5 *)
        Lopputuloksessa D4 tämä metodi siis palauttaa 5 * 12
        """
        korkeus = 0
        if len(self.savelma) == 0:
            korkeus = self.korkeusarpoja.arvo_korkeus()
        else:
            edellisen_korkeus = self.savelma[-1].korkeus
            korkeus = self.korkeusarpoja.arvo_korkeus(edellisen_korkeus)
        return korkeus * 12

    def _arvo_pituus(self, max_pituus):
        """
        Arpoo sävelen pituuden viimeisimmän sävelmään talletetun sävelen perusteella.
        Palauttaa äänen pituutta kuvaavan kokonaisluvun, 0 on kokonuotti.
        ja toinen arvo on kuinka monta kuudestoistaosaa ääni vie tahdista

        args:
            max_pituus: kuinka monta kuudestoistaosaa pituus voi enintään olla
        """
        pituus = 0
        if len(self.savelma) == 0:
            pituus = self.pituusarpoja.arvo_pituus()
        else:
            edellisen_pituus = self.tempo.get_savelpituus(
                self.savelma[-1].pituus)
            pituus = self.pituusarpoja.arvo_pituus(
                edellisen_pituus, max_pituus)

        return pituus

    def __str__(self):
        """
        Tulostaa kaikki tähän mennessä luodun sävelmän äänet
        """
        tulostus = ""
        for savel in self.savelma:
            tulostus += f"{str(savel)}, "
        return "luotu sävelmä: " + tulostus
