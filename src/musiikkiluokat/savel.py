"""
Savel-luokka
"""

from musiikkiluokat.aani import Aani


class Savel():
    """
    Sävelen tiedot sisällään pitävä olio
        midi_aani: midi-standardin mukainen äänen yksikkö, kokonaisluku 0 - 127
        aani: sävelen nimi, Aani-olio
        korkeus: sävelen oktaavi, kokonaisluku välillä 0 - 10
        pituus: sävelen kesto, kokonaisluku sekunnin tuhannesosina
    """

    def __init__(self, midi_aani, pituus=0):
        """Konstruktori
        Args:
            midi_aani : midi-standardin mukainen äänen yksikkö, kokonaisluku 0 - 127
            pituus: sävelen kesto, kokonaisluku sekunnin tuhannesosina
        """
        self.midi = midi_aani
        self.aani = Aani(midi_aani)
        self.korkeus = midi_aani // 12
        self.pituus = pituus

    def __eq__(self, savel):
        """
        Yhtäläisyysvertailu. Vain sävelen nimeä verrataan, ei korkeutta

        args:
            savel: Savel-olio
        """
        if isinstance(savel, Savel):
            return self.aani == savel.aani
        return False

    def __str__(self):
        """
        Tulostaa Sävelen nimen ja korkeuden. Korkeus ilmaistaan normaalina sävelkorkeutena,
        eli välillä -1 - 9
        """

        return f"{self.aani}{self.korkeus - 1}"
