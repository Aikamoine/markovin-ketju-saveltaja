import unittest
from musiikkiluokat.savel import Savel

class SavelTest(unittest.TestCase):
    def setUp(self):
        self.testisavel_c_neg1 = Savel(0)
        self.testisavel_g_9 = Savel(127, 3)
        self.testisavel_f_5 = Savel(77)

    def test_savelen_korkeus_muodostuu_oikein(self):
        self.assertEqual(self.testisavel_c_neg1.korkeus, 0)
        self.assertEqual(self.testisavel_g_9.korkeus, 10)
        self.assertEqual(self.testisavel_f_5.korkeus, 6)

    def test_savelen_pituus_muodostuu_oikein(self):
        self.assertEqual(self.testisavel_c_neg1.pituus, 0)
        self.assertEqual(self.testisavel_g_9.pituus, 3)
        self.assertEqual(self.testisavel_f_5.pituus, 0)

    def test_eq_vertaa_oikein(self):
        vertaus_savel = Savel(77)
        self.assertEqual(self.testisavel_f_5, vertaus_savel)
        self.assertFalse(self.testisavel_g_9 == vertaus_savel)
        ei_savel = "Tämä on tekstiä"
        self.assertFalse(ei_savel == self.testisavel_c_neg1)

    def test_str_palauttaa_oikean_arvon(self):
        self.assertEqual(str(self.testisavel_c_neg1), "C-1")
        self.assertEqual(str(self.testisavel_g_9), "G9")
        self.assertEqual(str(self.testisavel_f_5), "F5")
