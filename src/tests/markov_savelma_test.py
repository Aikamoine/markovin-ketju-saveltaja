import unittest
from markovin_ketjut.markov_savelma import MarkovSavelma
from trie.trie import Trie
from musiikkiluokat.savel import Aani
from musiikkiluokat.tempo import Tempo
from musiikkiluokat.savel import Savel
from tests.fakerandom import FakeRandom

class MarkoSavelmaTest(unittest.TestCase):
    def setUp(self):
        self.arpoja = FakeRandom
        self.markov = MarkovSavelma(self._luo_trie(), Tempo(), self.arpoja)

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

    def test_seuraava_solmu_loytaa_ensimmaisen_solmun(self):
        savel = Savel(71, 2000)
        self.markov.savelma.append(savel)
        solmu = self.markov._seuraava_solmu()
        self.assertEqual(solmu.aani, Aani(71))

    def test_seuraava_solmu_loytaa_toisen_solmun(self):
        self.markov.savelma.append(Savel(71, 2000))
        self.markov.savelma.append(Savel(62, 2000))
        solmu = self.markov._seuraava_solmu()
        self.assertEqual(solmu.aani, Aani(62))

    def test_seuraava_solmu_loytaa_osa_savelmalla_solmun(self):
        self.markov.savelma.append(Savel(63, 2000))
        self.markov.savelma.append(Savel(69, 2000))
        self.markov.savelma.append(Savel(62, 2000))
        solmu = self.markov._seuraava_solmu()
        self.assertEqual(solmu.aani, Aani(62))