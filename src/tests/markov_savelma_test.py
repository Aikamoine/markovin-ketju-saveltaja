import unittest
from markovin_ketjut.markov_savelma import MarkovSavelma
from trie.trie import Trie
from musiikkiluokat.savel import Aani
from musiikkiluokat.tempo import Tempo
from musiikkiluokat.savel import Savel
from musiikkiluokat.savellaji import Savellaji
from tests.fakerandom import FakeRandom

class MarkoSavelmaTest(unittest.TestCase):
    def setUp(self):
        self.arpoja = FakeRandom()
        self.savellaji = Savellaji(False, "C")
        self.markov = MarkovSavelma(self._luo_trie(), Tempo(), self.savellaji, self.arpoja)

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

    def test_arvo_korkeus_palauttaa_48_kun_arpoja_on_1_ja_savelma_tyhja(self):
        self.arpoja.palautus = 1
        self.assertEqual(self.markov._arvo_korkeus(), 48)

    def test_arvo_korkeus_palauttaa_60_kun_arpoja_on_1_ja_edellinen_korkeus_on_oktaavilla_5(self):
        self.arpoja.palautus = 1
        savel = Savel(74, 2000)
        self.markov.savelma.append(savel)
        self.assertEqual(self.markov._arvo_korkeus(), 60)

    def test_arvo_pituus_palauttaa_2_kun_arpoja_on_1_ja_savelma_tyhja(self):
        self.arpoja.palautus = 1
        self.assertEqual(self.markov._arvo_pituus(16), 2)

    def test_arvo_pituus_palauttaa_3_kun_arpoja_on_1_ja_edellinen_pituus_kuudestoistaosa(self):
        self.arpoja.palautus = 1
        savel = Savel(74, 125)
        self.markov.savelma.append(savel)
        self.assertEqual(self.markov._arvo_pituus(16), 3)
