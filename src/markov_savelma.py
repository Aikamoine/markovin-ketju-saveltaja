'''
MarkovSavelma-luokka
'''

import random

class MarkovSavelma():
    '''
    Markovin ketjulla sävelmiä luova olio
    '''
    def __init__(self, opetusaineisto):
        '''
        Konstruktori
            trie: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
            savelma: taulukko Säveliä

        args:
            opetusaineisto: Trie-olio, jossa on tallennettuna erilaiset sävelkulut
        '''
        self.trie = opetusaineisto
        self.savelma = []

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
        lisattava = None
        print(f"Markov ennen lisäystä:\n {self}")
        if len(self.savelma) == 0:
            lisattava = self._arvo_savel(self.trie.juurisolmu.lapset).savel
        else:
            seuraava = self.trie.loyda_seuraava_solmu(self.savelma)
            lisattava = self._arvo_savel(seuraava.lapset).savel
        self.savelma.append(lisattava)
        print(f"Markov lisäyksen jälkeen:\n {self}")

    def _arvo_savel(self, vaihtoehdot):
        '''
        Laskee vaihtoehtojen jakauman ja sen perusteella arpoo yhden solmun

        args:
            vaihtoehdot: taulukko Solmuja
        '''
        yhteensa = 0
        jakauma = [None]*len(vaihtoehdot)

        for i in range(len(vaihtoehdot)):
            yhteensa += vaihtoehdot[i].maara
            jakauma[i] = vaihtoehdot[i].maara
        arvottu = random.randint(0, yhteensa)
        for i in range(len(vaihtoehdot)):
            if jakauma[i] >= arvottu:
                return vaihtoehdot[i]
            arvottu -= jakauma[i]

    def __str__(self):
        '''
        Tulostaa kaikki tähän mennessä luodun sävelmän äänet
        '''
        tulostus = ""
        for savel in self.savelma:
            tulostus += f"{str(savel)}, "
        return "luotu sävelmä: " + tulostus