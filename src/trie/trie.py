'''
Sisältää Trie-tietorakenteen koodin
'''
from musiikkiluokat.savel import Savel

class Trie():
    '''
    Sisältää Trie-tietorakenteen koodin

        juurisolmu: Solmu
    '''
    def __init__(self, maksimisyvyys):
        '''
        Konstruktori.
        Alustaa juurisolmu-muuttujan Solmuksi, jolla ei ole säveltä
        '''
        self.juurisolmu = Solmu(None)
        self.maksimisyvyys = maksimisyvyys

    def lisaa_savelma(self, savelma):
        '''
        Lisää Trieen kokonaisen sävelmän

        args:
            savelma: taulukko Savel-olioita
        '''
        lahtosolmu = self.juurisolmu
        for i in range(len(savelma)):
            savel_loytyi = False
            for solmu in lahtosolmu.lapset:
                if solmu.savel == savelma[i]:
                    solmu.maara += 1
                    lahtosolmu = solmu
                    savel_loytyi = True
                    break
            if not savel_loytyi:
                uusi_solmu = Solmu(savelma[i])
                lahtosolmu.lapset.append(uusi_solmu)
                lahtosolmu = uusi_solmu

    def loyda_seuraava_solmu(self, savelma):
        '''
        Palauttaa Solmun, joka vastaa argumenttina annettua sävelmää
        sen viimeiseen solmuun saakka. Palauttaa siis viimeisen solmun,
        joka kuuluu annettuun sävelmään.

        args:
            savelma: taulukko Savel-olioita
        '''
        lahtosolmu = self.juurisolmu
        for i in range(0, len(savelma)):
            savel_loytyi = False
            for solmu in lahtosolmu.lapset:
                if solmu.savel == savelma[i]:
                    lahtosolmu = solmu
                    savel_loytyi = True
                    break

            if not savel_loytyi:
                return None

        return lahtosolmu

    def tulosta(self):
        '''
        Tulostaa Trien tiedostoon, että jokainen solmu on sisennetty vanhempaansa nähden
        '''
        tiedosto = open("src//trie//trie.txt", "w")
        for solmu in self.juurisolmu.lapset:
            #solmu.tulosta("", tiedosto)
            solmu.tallenna(0, tiedosto)

    def lisaa_savelet_trieen(self, aanet):
        savelet = []
        for aani in aanet:
            savel = Savel(aani)
            savelet.append(savel)

            if len(savelet) == self.maksimisyvyys:
                self.lisaa_savelma(savelet)
                savelet = []

class Solmu():
    '''
    Solmu-olio. Näistä koostuu Trie-puu
    '''
    def __init__(self, savel):
        '''
        Konstruktori.
            savel: Savel-olio. Mitä säveltä solmu kuvastaa
            maara: Kuinka monta kertaa solmun kautta on kuljettu arvoja lisätessä
            lapset: taulukko Solmuja, joihin tämän Solmun kautta kuljetaan
        args:
            savel: Savel-olio
        '''
        self.savel = savel
        self.maara = 1
        self.lapset = []

    def tallenna(self, syvyys, tiedosto):
        sisennykset = ""
        for i in range(0, syvyys):
            sisennykset += "| "
        tiedosto.write(f"{sisennykset}{self.savel}, {self.maara} kpl\n")
        for solmu in self.lapset:
            solmu.tallenna(syvyys + 1, tiedosto)

    def tulosta(self, sisennys, tiedosto):
        '''
        Tulostaa Solmun siten, että jokainen solmu on sisennetty vanhempaansa nähden
        Huom! Vaikka tulostuksessa näkyykin sävelen korkeus, esim A>4<, niin lukumäärään
        on kuitenkin huomioitu kaikki saman sävelen äänet, korkeudesta
        '''
        tiedosto.write(f"{sisennys}{self.savel}, {self.maara} kpl\n")
        for solmu in self.lapset:
            solmu.tulosta(f"{sisennys}  ", tiedosto)
