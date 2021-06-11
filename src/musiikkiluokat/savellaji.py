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
    Kappaleen sävellajia kuvaava olio. Kokonaislukujen arvot tulevat Midi-standardista, jossa
    C on aina oktaavin matalin ääni.
    """
    def __init__(self, molli, savel):
        """
        Args:
            molli: boolean, onko sävellaji mollissa
            savel: teksti, mikä on kappaleen sävellaji
        """
        if molli:
            self.laji = "m"
        else:
            self.laji = "d"
        self.savel = savel
        self.savel_indeksi = AANET[savel]

    def onko_molli(self):
        """
        Palauttaa boolean arvon siitä, onko sävelmä mollissa.
        False tarkoittaa, että sävelmä on duurissa
        """
        return self.laji == "m"

    def aanelle_indeksi(self, aani):  # pylint: disable=no-self-use
        """
        Palauttaa tekstimuotoiselle sävelen kuvaukselle, esim C tai G# sen indeksin
        Indeksi tulee Midi-standardista, jossa C on aina oktaavin ensimmäinen sävel - eli 0
        Args:
            aani: sävelen nimi tekstinä, esim C, G# tai Bb
        """
        return AANET[aani]
