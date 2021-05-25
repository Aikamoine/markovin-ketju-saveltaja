import unittest
from trie.trie import Trie
from musiikkiluokat.savel import Savel

class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie(8)

        self.savel_a = Savel(69)
        self.savel_d = Savel(62)
        self.savel_c = Savel(60)
        self.savel_f = Savel(65)
        self.savel_b = Savel(71)
        savelma_1 = [self.savel_a, self.savel_d, self.savel_c, self.savel_a]
        savelma_2 = [self.savel_a, self.savel_d, self.savel_f, self.savel_b]
        savelma_3 = [self.savel_b, self.savel_d, self.savel_a, self.savel_d]

        self.trie.lisaa_savelma(savelma_1)
        self.trie.lisaa_savelma(savelma_2)
        self.trie.lisaa_savelma(savelma_3)

    def test_trien_ensimmainen_taso_muodostuu_oikein(self):
        juurisavelet = []
        for solmu in self.trie.juurisolmu.lapset:
            juurisavelet.append(solmu.savel)
        self.assertTrue(self.savel_a in juurisavelet)
        self.assertTrue(self.savel_b in juurisavelet)
        self.assertFalse(self.savel_d in juurisavelet)

    def test_kerran_lisatyn_maara_on_yksi(self):
        self.assertEqual(self.trie.juurisolmu.lapset[1].maara, 1)

    def test_kahdesti_lisatyn_maara_on_kaksi(self):
        self.assertEqual(self.trie.juurisolmu.lapset[0].maara, 2)

    def test_loyda_seuraava_solmu_loytaa_oikean(self):
        solmu = self.trie.loyda_seuraava_solmu([self.savel_a, self.savel_d])
        self.assertEqual(solmu.savel, self.savel_d)

    def test_palauttaa_tyhjan_jos_savelmalle_ei_vastinetta(self):
        solmu = self.trie.loyda_seuraava_solmu([self.savel_d])
        self.assertEqual(solmu, None)