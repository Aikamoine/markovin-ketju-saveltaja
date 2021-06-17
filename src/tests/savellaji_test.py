import unittest
from musiikkiluokat.savellaji import Savellaji


class SavelTest(unittest.TestCase):
    def setUp(self):
        self.duuri = Savellaji(False, "C")
        self.molli = Savellaji(True, "G#")

    def test_mollitarkistus_palauttaa_oikein(self):
        self.assertEqual(self.molli.onko_molli(), True)
        self.assertEqual(self.duuri.onko_molli(), False)

    def test_indeksikysely_palauttaa_oikein(self):
        self.assertEqual(self.molli.aanelle_indeksi("C"), 0)
        self.assertEqual(self.duuri.aanelle_indeksi("B"), 11)
        self.assertEqual(self.molli.aanelle_indeksi("F#"), 6)
        self.assertEqual(self.duuri.aanelle_indeksi("Gb"), 6)
