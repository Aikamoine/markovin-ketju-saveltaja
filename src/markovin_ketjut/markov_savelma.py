"""
MarkovSavelma-luokka
"""

from musiikkiluokat.savel import Savel
from markovin_ketjut.pituusarpoja import Pituusarpoja
from markovin_ketjut.korkeusarpoja import Korkeusarpoja


class MarkovSavelma():
    """
    Markovin ketjulla sävelmiä luova olio
    """

    def __init__(self, opetusaineisto, tempo, arpoja):
        """
        Konstruktori
            trie: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
            savelma: taulukko Säveliä
            pituusarpoja: Pituusarpoja-olio nuottien pituuksien generointiin
            tempo: Tempo-olio nuottien pituuksien ja todellisten pituuksien tulkintaan
        args:
            opetusaineisto: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
            tempo: Tempo-olio
        """
        self.trie = opetusaineisto
        self.savelma = []
        self.pituusarpoja = Pituusarpoja(arpoja)
        self.korkeusarpoja = Korkeusarpoja(arpoja)
        self.tempo = tempo
        self.arpoja = arpoja

    def luo_savellys(self, tahteja):
        """
        Luo sävellyksen triestä ääniä generoimalla. Triestä pyritään aina hakemaan mahdollisimman
        korkean asteen yhtenevyys. Jos sellaista ei löydy, tiputetaan haettavasta sävelmästä yksi
        ääni kerrallaan pois

        args:
            tahteja: kuinka monta tahtai halutaan yhteensä generoida
            // todo: generoidaan tahtien määrä
        """
        for i in range(tahteja):
            tahdissa_jaljella = 16

            while tahdissa_jaljella > 0:
                seuraava = self._seuraava_solmu()

                tahdissa_jaljella = self._lisaa_savelmaan(
                    seuraava, tahdissa_jaljella)

            print(f"Tahti {i + 1} kirjoitettu\n")

    def _seuraava_solmu(self):
        """
        Hakee triestä seuraavan solmun, joka vastaa mahdollismman suurta
        astetta kirjoitetun sävelmän lopusta nähden.
        """
        kaytettava_savelma = self.savelma[-self.trie.maksimisyvyys:]
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
            seuraava: Ääni, joka tullaan lisäämään
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
        print(str(self))
        print()

        return tahdissa_jaljella - (16 / (2**arvottu_pituus))

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
