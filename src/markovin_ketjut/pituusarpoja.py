"""
Pituusarpoja-luokka
"""


class Pituusarpoja:
    """
    Olio, joka (ensimmäisen asteen) Markovin ketjua käyttäen arpoo sävelen pituuden
    """

    def __init__(self, arpoja):
        """
        Konstruktori.
            tilasiirtymat: taulukko, jonka perusteella siirrytään eri tilojen välillä
                           x-akseli kuvaa tietystä tilasta siirtymisen todennäköisyyksiä
            selitteet: tilasiirtymien indeksien selitteet
        """
        self.arpoja = arpoja
        self.tilasiirtymat = [
            [30, 20, 20, 15, 15],  # kokonuotti
            [10, 40, 25, 15, 10],  # puolinuotti
            [10, 20, 40, 20, 10],  # neljäsosanuotti
            [15, 15, 15, 40, 15],  # kahdeksasosanuotti
            [5, 5, 20, 30, 40],  # kuudestoistaosanuotti
        ]

        self.selitteet = {
            0: "kokonuotti",
            1: "puolinuotti",
            2: "neljäsosanuotti",
            3: "kahdeksasosanuotti",
            4: "kuudestoistaosanuotti"
        }

    def arvo_pituus(self, edellinen=2, maksimi=16):
        """
        Etsii seuraavan tilan. Tyhjälle tilalle etsitään arvo neljäsosanuotin arvojen perusteella

        Args:
            edellinen: edellistä tilaa, eli nuottia, kuvaava kokonaisluku
        """
        arvottu = self.arpoja.randint(1, 100)
        mahdolliset_tilat = self.tilasiirtymat[edellinen]

        for i, tila in enumerate(mahdolliset_tilat):
            if 16 / (2**i) <= maksimi:
                if tila >= arvottu:
                    print(f"Arvottiin pituudeksi: {self.selitteet[i]}")
                    return i
            arvottu -= tila

        return len(mahdolliset_tilat) - 1
