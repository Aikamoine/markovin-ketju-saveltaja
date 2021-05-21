import unittest
from musiikkiluokat.savel import Savel

class SavelTest(unittest.TestCase):
    def setUp(self):
        self.testisavel_c_neg1 = Savel(0)
        self.testisavel_g_9 = Savel(127)
        self.testisavel_f_5 = Savel(77)

    def test_savel_muodostuu_oikein(self):
        self.assertEqual(self.testisavel_c_neg1.aani, 0)
        self.assertEqual(self.testisavel_c_neg1.korkeus, 0)

        self.assertEqual(self.testisavel_g_9.aani, 7)
        self.assertEqual(self.testisavel_g_9.korkeus, 10)

        self.assertEqual(self.testisavel_f_5.aani, 5)
        self.assertEqual(self.testisavel_f_5.korkeus, 6)

    def test_eq_vertaa_oikein(self):
        vertaus_savel = Savel(77)
        self.assertEqual(self.testisavel_f_5, vertaus_savel)
        self.assertFalse(self.testisavel_g_9 == vertaus_savel)

    def test_str_palauttaa_oikean_arvon(self):
        self.assertEqual(str(self.testisavel_c_neg1), "C-1")
        self.assertEqual(str(self.testisavel_g_9), "G9")
        self.assertEqual(str(self.testisavel_f_5), "F5")
