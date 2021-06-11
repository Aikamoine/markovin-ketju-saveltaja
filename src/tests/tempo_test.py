import unittest
from musiikkiluokat.tempo import Tempo

class TempoTest(unittest.TestCase):
    def setUp(self):
        self.tempo = Tempo()
        self.tempo_180 = Tempo(180)

    def test_tempo_alustuu_120(self):
        uusitempo = Tempo(120)
        self.assertEqual(self.tempo.pituudet, uusitempo.pituudet)

    def test_kokonuotti_120bpm_palauttaa_2000(self):
        self.assertEqual(self.tempo.get_aanen_pituus(0), 2000)

    def test_kokonuotti_180bpm_palauttaa_1333(self):
        self.assertEqual(self.tempo_180.get_aanen_pituus(0), 1333)

    def test_neljasosa_120bpm_palauttaa_500(self):
        self.assertEqual(self.tempo.get_aanen_pituus(2), 500)

    def test_neljasosa_180bpm_palauttaa_333(self):
        self.assertEqual(self.tempo_180.get_aanen_pituus(2), 333)

    def test_kuudestoistaosa_120bpm_palauttaa_125(self):
        self.assertEqual(self.tempo.get_aanen_pituus(4), 125)

    def test_kuudestoistaosa_180bpm_palauttaa_1333(self):
        self.assertEqual(self.tempo_180.get_aanen_pituus(4), 83)

    def test_1000ms_120bpm_palauttaa_puolinuotin(self):
        self.assertEqual(self.tempo.get_savelpituus(1000), 1)

    def test_333ms_180bpm_palauttaa_neljasosan(self):
        self.assertEqual(self.tempo_180.get_savelpituus(333), 2)
