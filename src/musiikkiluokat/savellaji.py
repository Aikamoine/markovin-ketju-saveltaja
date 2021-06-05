"""
Savellaji-luokka
"""

AANET = {
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11
}

class Savellaji:
    """
    Kappaleen sävellajia kuvaava olio
    """
    def __init__(self, molli, savel):
        if molli:
            self.laji = "m"
        else:
            self.laji = "d"
        self.savel = savel
        self.savel_indeksi = AANET[savel]

    def onko_molli(self):
        return self.laji == "m"

    def aanelle_indeksi(self, aani):
        return AANET[aani]
