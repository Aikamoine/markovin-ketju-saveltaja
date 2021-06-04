"""
Tempo-luokka
"""


class Tempo:
    """
    Midi-tiedoston edistämiseen käytetään tuhannesosasekunteja kokonaislukuina
    Tämä luokka muodostaa musiikissa käytetyn iskua per minuutti / temmon

    bps: iskua sekunnissa
    nuottien pituudet: nuotin pituus sekunnin tuhannesosina
    """

    def __init__(self, bpm=120):
        """
        Konstruktori.

        args: bpm = iskua minuutissa, eli kappaleen tempo
        """
        bps = bpm / 60
        self.pituudet = [int(1000 / (bps / 4)),
                         int(1000 / (bps / 2)),
                         int(1000 / bps),
                         int(1000 / (bps * 2)),
                         int(1000 / (bps * 4)),
                         int(1000 / (bps * 8))]

    def get_aanen_pituus(self, nuotti):
        """
        Palauttaa nuotin pituuden sekunnin tuhannesosina

        args:
            nuotti: äänen pituuden indeksi, 0 on täysnuotti, 1 puolinuotti, jne
        """
        print(f"Määritettiin äänen pituudeksi: {self.pituudet[nuotti]}")
        return self.pituudet[nuotti]

    def get_savelpituus(self, pituus):
        """
        Palauttaa nuotin pituuden, argumenttina sen pituus sekunnin tuhannesosina

        args:
            pituus: kokonaisluku, äänen pituus sekunnin tuhannesosina
        """
        for i, savelpituus in enumerate(self.pituudet):
            if pituus == savelpituus:
                return i
        return self.pituudet[-1]
