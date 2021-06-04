import unittest
from trie.trie import Trie
from musiikkiluokat.aani import Aani
from musiikkiluokat.savel import Savel


class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie(4)

        self.aani_a = Aani(69)
        self.aani_d = Aani(62)
        self.aani_c = Aani(60)
        self.aani_f = Aani(65)
        self.aani_b = Aani(71)
        savelma_1 = [self.aani_a, self.aani_d, self.aani_c, self.aani_a]
        savelma_2 = [self.aani_a, self.aani_d, self.aani_f, self.aani_b]
        savelma_3 = [self.aani_b, self.aani_d, self.aani_a, self.aani_d]

        self.trie.lisaa_savelma(savelma_1)
        self.trie.lisaa_savelma(savelma_2)
        self.trie.lisaa_savelma(savelma_3)

    def test_trien_ensimmainen_taso_muodostuu_oikein(self):
        juurisavelet = []
        for solmu in self.trie.juurisolmu.lapset:
            juurisavelet.append(solmu.aani)
        self.assertTrue(self.aani_a in juurisavelet)
        self.assertTrue(self.aani_b in juurisavelet)
        self.assertFalse(self.aani_d in juurisavelet)

    def test_kerran_lisatyn_maara_on_yksi(self):
        self.assertEqual(self.trie.juurisolmu.lapset[1].maara, 1)

    def test_kahdesti_lisatyn_maara_on_kaksi(self):
        self.assertEqual(self.trie.juurisolmu.lapset[0].maara, 2)

    def test_loyda_seuraava_solmu_loytaa_oikean(self):
        testi_savelma = [Savel(69), Savel(62)]
        solmu = self.trie.loyda_seuraava_solmu(testi_savelma)
        self.assertEqual(solmu.aani, self.aani_d)

    def test_palauttaa_tyhjan_jos_savelmalle_ei_vastinetta(self):
        solmu = self.trie.loyda_seuraava_solmu([Savel(62)])
        self.assertEqual(solmu, None)

    def test_lisaa_b_ja_a_trieen_kasvattaa_b_maaraa(self):
        aanet = [71, 69]
        self.trie.lisaa_aanet_trieen(aanet)
        self.assertEqual(self.trie.juurisolmu.lapset[1].maara, 2)

    def test_lisaa_b_ja_a_trieen_lisaa_a_haaran(self):
        self.assertEqual(len(self.trie.juurisolmu.lapset[1].lapset), 1)
        aanet = [71, 69]
        self.trie.lisaa_aanet_trieen(aanet)
        self.assertEqual(len(self.trie.juurisolmu.lapset[1].lapset), 2)
