import unittest
from markovin_ketjut.markov_savelma import MarkovSavelma
from trie.trie import Trie
from musiikkiluokat.savel import Aani
from musiikkiluokat.tempo import Tempo
from musiikkiluokat.savel import Savel

class MarkoSavelmaTest(unittest.TestCase):
    def setUp(self):
        self.markov = MarkovSavelma(self._luo_trie(), Tempo())

    def _luo_trie(self):
        trie = Trie(4)

        aani_a = Aani(69)
        aani_d = Aani(62)
        aani_c = Aani(60)
        aani_f = Aani(65)
        aani_b = Aani(71)
        savelma_1 = [aani_a, aani_d, aani_c, aani_a]
        savelma_2 = [aani_a, aani_d, aani_f, aani_b]
        savelma_3 = [aani_b, aani_d, aani_a, aani_d]

        trie.lisaa_savelma(savelma_1)
        trie.lisaa_savelma(savelma_2)
        trie.lisaa_savelma(savelma_3)
        trie.tallenna()
        return trie

    def test_markov_alustuu_oikein(self):
        self.assertEqual(self.markov.savelma, [])

    def test_alusta_savelma_lisaa_savelet_listaan(self):
        savelma = [Savel(71), Savel(62)]
        self.markov.alusta_savelma(savelma)
        self.assertEqual(self.markov.savelma, savelma)

    def test_lisaa_b_savelmaan_aani_lisaa_d(self):
        savelma = [Savel(71, 500)]
        self.markov.alusta_savelma(savelma)
        self.markov.lisaa_savelmaan()
        savel = Savel(62)
        savelma.append(savel)
        self.assertEqual(self.markov.savelma, savelma)

    def test_lisaa_adc_savelmaan_aani_lisaa_a(self):
        savelma = [Savel(69, 500), Savel(62, 500), Savel(60, 500)]
        self.markov.alusta_savelma(savelma)
        self.markov.lisaa_savelmaan()
        savelma.append(Savel(69, 500))
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
