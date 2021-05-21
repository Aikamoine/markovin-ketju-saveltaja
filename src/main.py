'''
Pääohjelma, joka ajetaan Invoken kautta
'''

from musiikkiluokat.savel import Savel
from musiikkiluokat.midikirjoittaja import Midikirjoittaja
from trie.trie import Trie
from markov_savelma import MarkovSavelma

def luo_trie():
    '''
    Muodostaa trie-tietorakenteen. Toistaiseksi tietosisältö on kovakoodattu
    tässä metodissa.
    '''
    savel_a = Savel(69)
    savel_d = Savel(62)
    savel_c = Savel(60)
    savel_f = Savel(65)
    savel_b = Savel(71)

    trie = Trie()
    savelma_1 = [savel_a, savel_d, savel_c, savel_a]
    savelma_2 = [savel_a, savel_d, savel_f, savel_b]
    savelma_3 = [savel_b, savel_d, savel_a, savel_d]
    trie.lisaa_savelma(savelma_1)
    trie.lisaa_savelma(savelma_2)
    trie.lisaa_savelma(savelma_3)
    return trie

if __name__ == "__main__":
    trie = luo_trie()
    markov = MarkovSavelma(trie)
    #markov.alusta_savelma([Savel(69)]) #A
    #markov.alusta_savelma([Savel(71)])  # A
    trie.tulosta()
    print()
    markov.lisaa_savelmaan()
    markov.lisaa_savelmaan()
    markov.lisaa_savelmaan()
    markov.lisaa_savelmaan()

    midi = Midikirjoittaja()
    print()
    midi.kirjoita_aanet_uuteen_raitaan(markov.savelma, "uusi raita")
