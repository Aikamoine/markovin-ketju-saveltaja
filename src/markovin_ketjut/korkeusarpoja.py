'''
Korkeusarpoja-luokka
'''
import random

class Korkeusarpoja:
    '''
    Olio, joka (ensimmäisen asteen) Markovin ketjua käyttäen arpoo sävelen korkeuden
    '''

    def __init__(self):
        '''
        Konstruktori.
            tilasiirtymat: taulukko, jonka perusteella siirrytään eri tilojen välillä
                           x-akseli kuvaa tietystä tilasta siirtymisen todennäköisyyksiä
        '''
        self.tilasiirtymat = [
            [30, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0],#-1
            [20, 30, 50, 0, 0, 0, 0, 0, 0, 0, 0],#0
            [0, 20, 30, 50, 0, 0, 0, 0, 0, 0, 0],#1
            [0, 0, 25, 30, 45, 0, 0, 0, 0, 0, 0],#2
            [0, 0, 0, 30, 30, 40, 0, 0, 0, 0, 0],#3
            [0, 0, 0, 0, 33, 34, 33, 0, 0, 0, 0],#4
            [0, 0, 0, 0, 0, 33, 34, 33, 0, 0, 0],#5
            [0, 0, 0, 0, 0, 0, 40, 30, 30, 0, 0],#6
            [0, 0, 0, 0, 0, 0, 0, 45, 30, 25, 0],#7
            [0, 0, 0, 0, 0, 0, 0, 0, 50, 30, 20],#8
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 30] #9
        ]

    def arvo_korkeus(self, edellinen=5):
        '''
        Etsii seuraavan tilan. Tyhjälle tilalle etsitään arvo keski-c:n sisältävästä korkeudesta
        Esim. D-äänen indeksi on 2, joten D4 = 5 * 12 + 2 = 62 (äänet alkavat -1:stä, siksi 5 *)
        Lopputuloksessa D4 tämä metodi siis palauttaa 5 * 12
        args:
            edellinen: edellistä tilaa, eli pituutta, kuvaava kokonaisluku
        '''
        arvottu = random.randint(1, 100)
        mahdolliset_tilat = self.tilasiirtymat[edellinen]
        for i, tila in enumerate(mahdolliset_tilat):
            if tila >= arvottu:
                print(f"Arvottiin korkeudeksi: {i - 1}")
                return i * 12
            arvottu -= tila

        return len(mahdolliset_tilat) - 1
