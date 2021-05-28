'''
MarkovSavelma-luokka
'''

import random
from musiikkiluokat.savel import Savel
from markovin_ketjut.pituusarpoja import Pituusarpoja

class MarkovSavelma():
    '''
    Markovin ketjulla sävelmiä luova olio
    '''
    def __init__(self, opetusaineisto, tempo):
        '''
        Konstruktori
            trie: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
            savelma: taulukko Säveliä
            pituusarpoja: Pituusarpoja-olio nuottien pituuksien generointiin
            tempo: Tempo-olio nuottien pituuksien ja todellisten pituuksien tulkintaan
        args:
            opetusaineisto: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
            tempo: Tempo-olio
        '''
        self.trie = opetusaineisto
        self.savelma = []
        self.pituusarpoja = Pituusarpoja()
        self.tempo = tempo

    def alusta_savelma(self, lahtotilanne):
        '''
        Lisää sävelmään tietyn sointukulun. Tätä käytetään, jos haluaa luoda tunnetun alun
        sävelmälle ennen kuin Markovin ketju aloittaa pähkäilynsä

        args:
            lahtotilanne: taulukko Savel-olioita
        '''
        for savel in lahtotilanne:
            self.savelma.append(savel)

    def lisaa_savelmaan(self):
        '''
        Lisää olemassa olevaan sävelmään yhden äänen.
        '''
        uusi_aani = None
        if len(self.savelma) == 0:
            uusi_aani = self._arvo_solmu(self.trie.juurisolmu.lapset).aani
        else:
            seuraava = self.trie.loyda_seuraava_solmu(self.savelma)
            uusi_aani = self._arvo_solmu(seuraava.lapset).aani
        #Todo:arvo sävelen korkeus
        aanenkorkeus = self._arvo_korkeus()
        aanenpituus = self._arvo_pituus()
        uusi_savel = Savel(uusi_aani.aani_luku + aanenkorkeus, aanenpituus)
        self.savelma.append(uusi_savel)

    def luo_savellys(self, savelten_maara):
        '''
        Luo sävellyksen triestä ääniä generoimalla. Triestä pyritään aina hakemaan mahdollisimman
        korkean asteen yhtenevyys. Jos sellaista ei löydy, tiputetaan haettavasta sävelmästä yksi
        ääni kerrallaan pois

        args:
            savelten_maara: kuinka monta säveltä halutaan yhteensä generoida
            // todo: generoidaan tahtien määrä
        '''
        for i in range(savelten_maara):
            kaytettava_savelma = self.savelma[-self.trie.maksimisyvyys:]

            while True:
                self._tulosta_etsittava_savelma(kaytettava_savelma)
                seuraava = self.trie.loyda_seuraava_solmu(kaytettava_savelma)

                if seuraava is None or len(seuraava.lapset) == 0:
                    kaytettava_savelma = kaytettava_savelma[1:]
                else:
                    break

            uusi_aani = self._arvo_solmu(seuraava.lapset).aani
            #Todo: arvo sävelen korkeus, pituus
            print(f"Aani: {uusi_aani}")
            aanenkorkeus = self._arvo_korkeus()
            aanenpituus = self._arvo_pituus()
            uusi_savel = Savel(uusi_aani.aani_luku + aanenkorkeus, aanenpituus)
            self.savelma.append(uusi_savel)
            print(str(self))
            print()

    def _tulosta_etsittava_savelma(self, savelma):  #pylint: disable=no-self-use
        '''
        Tulostaa komentoriville seuraavaksi triestä etsittävän sävelmän

        args:
            savelma: osataulukko self.savelma -oliomuuttujasta
        '''
        printtaus = ""
        for savel in savelma:
            printtaus += str(savel) + ","

        print(f"Etsitään seuraava ääni sävelmälle: {printtaus}")

    def _arvo_solmu(self, vaihtoehdot):  # pylint: disable=no-self-use
        '''
        Laskee vaihtoehtojen jakauman ja sen perusteella arpoo yhden solmun

        args:
            vaihtoehdot: taulukko Solmuja
        '''
        yhteensa = 0
        jakauma = [None]*len(vaihtoehdot)

        for i, vaihtoehto in enumerate(vaihtoehdot):
            yhteensa += vaihtoehto.maara
            jakauma[i] = vaihtoehto.maara

        arvottu = random.randint(0, yhteensa)

        for i, vaihtoehto in enumerate(vaihtoehdot):
            if jakauma[i] >= arvottu:
                return vaihtoehto
            arvottu -= jakauma[i]
        return vaihtoehdot[-1]

    def _arvo_korkeus(self):  # pylint: disable=no-self-use
        '''
        Arpoo sävelen korkeuden. Toistaiseksi kahden oktaavin väliltä
        //todo: implementoi korkeusarpoja-luokka
        '''
        korkeus = random.randint(5, 6)
        print(f"Arvottu korkeus = {korkeus}")
        return korkeus * 12

    def _arvo_pituus(self):
        '''
        Arpoo sävelen pituuden viimeisimmän sävelmään talletetun sävelen perusteella
        '''
        pituus = 0
        if len(self.savelma) == 0:
            pituus = self.pituusarpoja.arvo_pituus()
        else:
            edellinen = self.savelma[-1]
            print(edellinen)
            print(edellinen.pituus)
            edellisen_pituus = self.tempo.get_savelpituus(self.savelma[-1].pituus)
            print(edellisen_pituus)
            pituus = self.pituusarpoja.arvo_pituus(edellisen_pituus)

        return self.tempo.get_aanen_pituus(pituus)

    def __str__(self):
        '''
        Tulostaa kaikki tähän mennessä luodun sävelmän äänet
        '''
        tulostus = ""
        for savel in self.savelma:
            tulostus += f"{str(savel)}, "
        return "luotu sävelmä: " + tulostus
