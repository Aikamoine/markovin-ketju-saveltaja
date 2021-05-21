import unittest
from markov_savelma import MarkovSavelma
from trie.trie import Trie
from musiikkiluokat.savel import Savel

class MarkoSavelmaTest(unittest.TestCase):
    def setUp(self):
        self.markov = MarkovSavelma(self._luo_trie())

    def _luo_trie(self):
        trie = Trie()

        savel_a = Savel(69)
        savel_d = Savel(62)
        savel_c = Savel(60)
        savel_f = Savel(65)
        savel_b = Savel(71)
        savelma_1 = [savel_a, savel_d, savel_c, savel_a]
        savelma_2 = [savel_a, savel_d, savel_f, savel_b]
        savelma_3 = [savel_b, savel_d, savel_a, savel_d]

        trie.lisaa_savelma(savelma_1)
        trie.lisaa_savelma(savelma_2)
        trie.lisaa_savelma(savelma_3)

        return trie

    def test_markov_alustuu_oikein(self):
        self.assertEqual(self.markov.savelma, [])

    def test_alusta_savelma_lisaa_savelet_listaan(self):
        savelma = [Savel(71), Savel(62)]
        self.markov.alusta_savelma(savelma)
        self.assertEqual(self.markov.savelma, savelma)

    def test_lisaa_b_savelmaan_aani_lisaa_d(self):
        savelma = [Savel(71)]
        self.markov.alusta_savelma(savelma)
        self.markov.lisaa_savelmaan()
        savelma.append(Savel(62))
        self.assertEqual(self.markov.savelma, savelma)

    def test_lisaa_adc_savelmaan_aani_lisaa_a(self):
        savelma = [Savel(69), Savel(62), Savel(60)]
        self.markov.alusta_savelma(savelma)
        self.markov.lisaa_savelmaan()
        savelma.append(Savel(69))
        self.assertEqual(self.markov.savelma, savelma)

    def test_tyhjaan_savelmaan_lisays_arpoo_savelen(self):
        self.markov.lisaa_savelmaan()
        savel = self.markov.savelma[0]

        savel_a_tai_b = False
        if savel == Savel(69):
            savel_a_tai_b = True
        if savel == Savel(71):
            savel_a_tai_b = True
        self.assertTrue(savel_a_tai_b)
