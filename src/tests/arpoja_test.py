import unittest
from markovin_ketjut.korkeusarpoja import Korkeusarpoja
from markovin_ketjut.pituusarpoja import Pituusarpoja

class FakeRandom:
    def __init__(self):
        self.palautus = 0

    def randint(self, eka, toka):
        return self.palautus

class KorkeusArpojaTest(unittest.TestCase):
    def setUp(self):
        self.arpoja = FakeRandom()
        self.korkeusarpoja = Korkeusarpoja(self.arpoja)

    def hae_arvottu(self, palautusarvo, edellinen_korkeus):
        self.arpoja.palautus = palautusarvo
        return self.korkeusarpoja.arvo_korkeus(edellinen_korkeus)

    def test_arvo_33_edellinen_5_palauttaa_4(self):
        arvottu = self.hae_arvottu(33, 5)
        self.assertEqual(arvottu, 4)

    def test_arvo_34_edellinen_5_palauttaa_5(self):
        arvottu = self.hae_arvottu(34, 5)
        self.assertEqual(arvottu, 5)

    def test_arvo_67_edellinen_5_palauttaa_5(self):
        arvottu = self.hae_arvottu(67, 5)
        self.assertEqual(arvottu, 5)

    def test_arvo_68_edellinen_5_palauttaa_6(self):
        arvottu = self.hae_arvottu(68, 5)
        self.assertEqual(arvottu, 6)

    #Tämä on vähän turha testi, mutta saadaanpa kattavuus täyteen...
    def test_arvo_yli100_edellinen_5_palauttaa_10(self):
        arvottu = self.hae_arvottu(101, 5)
        self.assertEqual(arvottu, 10)

class PituusArpojaTest(unittest.TestCase):
    def setUp(self):
        self.arpoja = FakeRandom()
        self.pituusarpoja = Pituusarpoja(self.arpoja)
        self.selitteet = {
            "kokonuotti": 0,
            "puolinuotti": 1,
            "4osa": 2,
            "8osa": 3,
            "16osa": 4,
        }

    def hae_arvottu(self, palautusarvo, edellinen_nuotti, maksimi):
        self.arpoja.palautus = palautusarvo
        edellinen = self.selitteet[edellinen_nuotti]
        return self.pituusarpoja.arvo_pituus(edellinen, maksimi)

    def test_arvo_1_edellinen_kokonuotti_tahti_tyhja_palauttaa_kokonuotti(self):
        arvottu = self.hae_arvottu(1, "kokonuotti", 16)
        self.assertEqual(arvottu, self.selitteet["kokonuotti"])

    def test_arvo_100_edellinen_kokonuotti_tahti_tyhja_palauttaa_16osa(self):
        arvottu = self.hae_arvottu(100, "kokonuotti", 16)
        self.assertEqual(arvottu, self.selitteet["16osa"])

    def test_arvo_1_edellinen_4osa_tahti_puolillaan_palauttaa_puolinuotti(self):
        arvottu = self.hae_arvottu(1, "4osa", 8)
        self.assertEqual(arvottu, self.selitteet["puolinuotti"])

    def test_arvo_100_edellinen_4osa_tahti_puolillaan_palauttaa_16osa(self):
        arvottu = self.hae_arvottu(100, "4osa", 8)
        self.assertEqual(arvottu, self.selitteet["16osa"])

    def test_arvo_31_edellinen_4osa_tahti_puolillaan_palauttaa_4osa(self):
        arvottu = self.hae_arvottu(31, "4osa", 8)
        self.assertEqual(arvottu, self.selitteet["4osa"])

    def test_arvo_30_edellinen_4osa_tahti_puolillaan_palauttaa_puolinuotti(self):
        arvottu = self.hae_arvottu(30, "4osa", 8)
        self.assertEqual(arvottu, self.selitteet["puolinuotti"])

    def test_arvo_10_edellinen_4osa_tahdissa_1_palauttaa_16osa(self):
        arvottu = self.hae_arvottu(10, "4osa", 1)
        self.assertEqual(arvottu, self.selitteet["16osa"])

    #Tämä on vähän turha testi, mutta saadaanpa kattavuus täyteen...
    def test_arvo_yli100_edellinen_16osa_palauttaa_16osa(self):
        arvottu = self.hae_arvottu(101, "16osa", 16)
        self.assertEqual(arvottu, self.selitteet["16osa"])
