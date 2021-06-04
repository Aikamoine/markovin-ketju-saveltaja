"""
Sisältää Trie-tietorakenteen koodin
"""
from musiikkiluokat.aani import Aani


class Trie():
    """
    Trie-rakenteen läpikäyntiin tarkoitettu koodi

        juurisolmu: Solmu
    """

    def __init__(self, maksimisyvyys):
        """
        Konstruktori.
        Alustaa juurisolmu-muuttujan Solmuksi, jolla ei ole säveltä
        """
        self.juurisolmu = Solmu(None)
        self.maksimisyvyys = maksimisyvyys

    def lisaa_savelma(self, savelma):
        """
        Lisää Trieen kokonaisen sävelmän

        args:
            savelma: taulukko Aani-olioita
        """
        lahtosolmu = self.juurisolmu

        for savel in savelma:
            aani_loytyi = False
            for solmu in lahtosolmu.lapset:
                if solmu.aani == savel:
                    solmu.maara += 1
                    lahtosolmu = solmu
                    aani_loytyi = True
                    break
            if not aani_loytyi:
                uusi_solmu = Solmu(savel)
                lahtosolmu.lapset.append(uusi_solmu)
                lahtosolmu = uusi_solmu

    def loyda_seuraava_solmu(self, savelma):
        """
        Palauttaa Solmun, joka vastaa argumenttina annettua sävelmää
        sen viimeiseen solmuun saakka. Palauttaa siis viimeisen solmun,
        joka kuuluu annettuun sävelmään.

        args:
            savelma: taulukko Aani-olioita
        """
        lahtosolmu = self.juurisolmu
        for savel in savelma:
            aani_loytyi = False
            for solmu in lahtosolmu.lapset:
                if solmu.aani == savel.aani:
                    lahtosolmu = solmu
                    aani_loytyi = True
                    break

            if not aani_loytyi:
                return None

        return lahtosolmu

    def tallenna(self):
        """
        Tallentaa Trien tiedostoon, että jokainen solmu on sisennetty vanhempaansa nähden
        """
        #tiedosto = open("src//trie//trie.txt", "w")
        with open("src//trie//trie.txt", "w") as tiedosto:
            for solmu in self.juurisolmu.lapset:
                solmu.tallenna("", tiedosto)

    def lisaa_aanet_trieen(self, aanet):
        """
        Lisää taulukon kaikki äänet Trieen.

        args:
            aanet: taulukko kokonaislukuja, Midi-standarin äänenkorkeuksia
        """
        lisattavat = []
        for aani in aanet:
            lisattava = Aani(aani)
            lisattavat.append(lisattava)

            if len(lisattavat) == self.maksimisyvyys:
                self.lisaa_savelma(lisattavat)
                lisattavat = []
        if len(lisattavat) > 0:
            self.lisaa_savelma(lisattavat)


class Solmu():
    """
    Solmu-olio. Näistä koostuu Trie-puu

    aani: Aani-olio. Mitä ääntä solmu kuvastaa
    maara: Kuinka monta kertaa solmun kautta on kuljettu arvoja lisätessä
    lapset: taulukko Solmuja, joihin tämän Solmun kautta kuljetaan
    """

    def __init__(self, aani):
        """
        Konstruktori.

        args:
            aani: Aani-olio
        """
        self.aani = aani
        self.maara = 1
        self.lapset = []

    def tallenna(self, sisennys, tiedosto):
        """
        Tallentaa Solmun tiedostoon siten, että jokainen solmu on sisennetty vanhempaansa nähden
        """
        tiedosto.write(f"{sisennys}{str(self.aani)}, {self.maara} kpl\n")
        for solmu in self.lapset:
            solmu.tallenna(f"{sisennys}| ", tiedosto)
