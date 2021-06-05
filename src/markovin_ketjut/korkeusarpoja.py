'''
Korkeusarpoja-luokka
'''


class Korkeusarpoja:
    '''
    Olio, joka (ensimmäisen asteen) Markovin ketjua käyttäen arpoo sävelen korkeuden
    '''

    def __init__(self, arpoja):
        '''
        Konstruktori.
            tilasiirtymat: taulukko, jonka perusteella siirrytään eri tilojen välillä
                           x-akseli kuvaa tietystä tilasta siirtymisen todennäköisyyksiä
        '''
        self.tilasiirtymat = [
            [20, 80, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # -1
            [15, 30, 55, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [0, 15, 25, 60, 0, 0, 0, 0, 0, 0, 0],  # 1
            [0, 0, 20, 30, 50, 0, 0, 0, 0, 0, 0],  # 2
            [0, 0, 0, 30, 30, 40, 0, 0, 0, 0, 0],  # 3
            [0, 0, 0, 0, 33, 34, 33, 0, 0, 0, 0],  # 4
            [0, 0, 0, 0, 0, 33, 34, 33, 0, 0, 0],  # 5
            [0, 0, 0, 0, 0, 0, 40, 30, 30, 0, 0],  # 6
            [0, 0, 0, 0, 0, 0, 0, 60, 25, 15, 0],  # 7
            [0, 0, 0, 0, 0, 0, 0, 0, 85, 15, 0],  # 8
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 10]  # 9
        ]
        self.arpoja = arpoja

    def arvo_korkeus(self, edellinen=5):
        '''
        Etsii seuraavan tilan. Tyhjälle tilalle etsitään arvo keski-c:n sisältävästä korkeudesta.
        Palauttaa taulukon indeksin mukaisen korkeutta kuvaavan tilan
        args:
            edellinen: edellistä tilaa, eli pituutta, kuvaava kokonaisluku
        '''
        arvottu = self.arpoja.randint(1, 100)
        mahdolliset_tilat = self.tilasiirtymat[edellinen]
        for i, tila in enumerate(mahdolliset_tilat):
            if tila >= arvottu:
                print(f"Arvottiin korkeudeksi: {i - 1}")
                return i
            arvottu -= tila

        return len(mahdolliset_tilat) - 1
