'''
Pituusarpoja-luokka
'''

import random

class Pituusarpoja:
    '''
    Olio, joka (ensimmäisen asteen) Markovin ketjua käyttäen arpoo sävelen pituuden
    '''

    def __init__(self):
        '''
        Konstruktori.
            tilasiirtymat: taulukko, jonka perusteella siirrytään eri tilojen välillä
                           x-akseli kuvaa tietystä tilasta siirtymisen todennäköisyyksiä
            selitteet: tilasiirtymien indeksien selitteet
        '''
        self.tilasiirtymat = [
            [40, 15, 15, 15, 15],
            [10, 40, 25, 15, 10],
            [10, 20, 40, 20, 10],
            [15, 15, 15, 40, 15],
            [5, 5, 20, 30, 40],
        ]

        self.selitteet = {
            0: "kokonuotti",
            1: "puolinuotti",
            2: "neljäsosanuotti",
            3: "kahdeksasosanuotti",
            4: "kuudestoistaosanuotti"
        }

    def arvo_pituus(self, edellinen=2):
        '''
        Etsii seuraavan tilan. Tyhjälle tilalle etsitään arvo neljäsosanuotin arvojen perusteella

        args:
            edellinen: edellistä tilaa, eli nuottia, kuvaava kokonaisluku
        '''
        arvottu = random.randint(1, 100)
        mahdolliset_tilat = self.tilasiirtymat[edellinen]

        for i, tila in enumerate(mahdolliset_tilat):
            if tila >= arvottu:
                print(f"Arvottiin pituudeksi: {self.selitteet[i]}")
                return i
            arvottu -= tila

        return len(mahdolliset_tilat) - 1
