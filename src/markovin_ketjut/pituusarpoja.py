"""
Pituusarpoja-luokka
"""


class Pituusarpoja:  # pylint: disable=too-few-public-methods
    """
    Olio, joka (ensimmäisen asteen) Markovin ketjua käyttäen arpoo sävelen pituuden

    arpoja: Arpoja-olio (Random-kirjastosta)
    tilasiirtymat: taulukko, jonka perusteella siirrytään eri tilojen välillä
                           x-akseli kuvaa tietystä tilasta siirtymisen todennäköisyyksiä
    selitteet: tilasiirtymien indeksien selitteet
    """

    def __init__(self, arpoja):
        """
        Args:
            arpoja: Arpoja-olio (Random-kirjastosta)
        """
        self.arpoja = arpoja
        self.tilasiirtymat = [
            [30, 20, 20, 15, 15],  # kokonuotti
            [10, 40, 25, 15, 10],  # puolinuotti
            [0, 0, 20, 80, 0],  # neljäsosanuotti
            [0, 0, 10, 80, 10],  # kahdeksasosanuotti
            [0, 0, 0, 80, 20],  # kuudestoistaosanuotti
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
        Varmistaa, ettei arvota tahdin ylittäviä pituuksia

        Args:
            edellinen: edellistä tilaa, eli nuottia, kuvaava kokonaisluku
            maksimi: yhdessä tahdissa jäljellä olevien kuudestoistaosien määrä
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
