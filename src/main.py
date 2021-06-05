'''
Pääohjelma, joka ajetaan Invoken kautta
'''
from random import Random
from musiikkiluokat.midikirjoittaja import Midikirjoittaja
from musiikkiluokat.midilukija import Midilukija
from musiikkiluokat.tempo import Tempo
from trie.trie import Trie
from markovin_ketjut.markov_savelma import MarkovSavelma
from ui import UI


def main():
    ui = UI()
    ui.tervetuloa()

    syvyys = ui.kysy_syvyys()
    trie = Trie(syvyys)
    print()

    molli = ui.onko_molli()
    print()

    savel = ui.kysy_savel()
    print()

    lukija = Midilukija()
    lukija.tallenna_polku_trieen("src//musiikkidata//", trie, molli, savel)

    trie.tallenna()
    print()

    tempo = Tempo(ui.kysy_tempo())
    print()

    arpoja = Random()
    markov = MarkovSavelma(trie, tempo, savel, arpoja)

    tahteja = ui.kysy_tahdit()
    print()

    markov.luo_savellys(tahteja)
    midi = Midikirjoittaja()
    midi.kirjoita_aanet_uuteen_raitaan(0, markov.savelma, "Melodia")
    midi.kirjoita_aanet_uuteen_raitaan(0, markov.harmonia, "Harmonia")
    midi.kirjoita_tiedosto()
if __name__ == "__main__":
    main()
