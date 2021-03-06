"""
Ääni-luokka
"""

AANTEN_NIMET = ["C", "C#", "D", "D#", "E",
                "F", "F#", "G", "G#", "A", "A#", "B"]


class Aani:
    """
    Ääni kuvastaa tyypillisessä länsimaisessa musiikkijärjestelmässä mikä 12 puolisävelaskeleesta
    on kyseessä. Midi-standardissa C on 0 ja mikä tahansa kahdellatoista jaollinen

    aani_luku: kokonaisluku väliltä 0 - 12
    """

    def __init__(self, midi_aani):
        """
        Args:
            midi_aani: midi-standardin mukainen äänen yksikkö, kokonaisluku 0 - 127
        """
        self.aani_luku = midi_aani % 12

    def __eq__(self, aani):
        """
        Yhtäläisyysvertailu. Vain sävelen nimeä verrataan, ei korkeutta

        Args:
            savel: Savel-olio
        """
        if isinstance(aani, Aani):
            return self.aani_luku == aani.aani_luku
        return False

    def __str__(self):
        """
        Tulostaa Sävelen nimen
        """
        return AANTEN_NIMET[self.aani_luku]
