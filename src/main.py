'''
Pääohjelma, joka ajetaan Invoken kautta
'''

from musiikkiluokat.midikirjoittaja import Midikirjoittaja
from musiikkiluokat.midilukija import Midilukija
from musiikkiluokat.tempo import Tempo
from trie.trie import Trie
from markovin_ketjut.markov_savelma import MarkovSavelma

if __name__ == "__main__":
    #luo_testisavelma()
    print("Anna trien syvyys. Tämä on myös Markovin ketjun aste. Suositus on väliltä 4 - 6.")
    syvyys = int(input())
    trie = Trie(syvyys)
    lukija = Midilukija()
    lukija.tallenna_polku_trieen("src//musiikkidata//", trie)

    trie.tallenna()
    print()

    print("Anna tempo. Suositus on 120 - 150.")
    valittu_tempo = int(input())
    print()
    tempo = Tempo(valittu_tempo)
    markov = MarkovSavelma(trie, tempo)


    print("Anna sävelmän äänten pituus. Suositus on vähintään 10, että on jotain kuunneltavaa.")
    pituus = int(input())
    print()
    markov.luo_savellys(pituus)
    midi = Midikirjoittaja()
    midi.kirjoita_aanet_uuteen_raitaan(0, markov.savelma, "uusi raita")
