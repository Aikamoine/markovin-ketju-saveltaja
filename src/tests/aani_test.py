import unittest
from musiikkiluokat.aani import Aani


class AaniTest(unittest.TestCase):
    def setUp(self):
        self.testiaani_c = Aani(0)
        self.testiaani_g = Aani(127)
        self.testiaani_fis = Aani(78)

    def test_aanen_nimi_muodostuu_oikein(self):
        self.assertEqual(self.testiaani_c.aani_luku, 0)
        self.assertEqual(self.testiaani_g.aani_luku, 7)
        self.assertEqual(self.testiaani_fis.aani_luku, 6)

    def test_eq_vertaa_oikein(self):
        vertaus_aani = Aani(96)
        self.assertEqual(self.testiaani_c, vertaus_aani)
        self.assertFalse(self.testiaani_g == vertaus_aani)
        ei_aani = "Tämä on tekstiä"
        self.assertFalse(ei_aani == self.testiaani_c)

    def test_str_palauttaa_oikean_arvon(self):
        self.assertEqual(str(self.testiaani_c), "C")
        self.assertEqual(str(self.testiaani_g), "G")
        self.assertEqual(str(self.testiaani_fis), "F#")
