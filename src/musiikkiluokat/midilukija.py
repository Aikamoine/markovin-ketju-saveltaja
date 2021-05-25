import os
from mido import MidiFile

class Midilukija:
    def __init__(self):
        self.tiedosto = None
        self.luettuja_tiedostoja = 0
        self.luettuja_savelia = 0

    def avaa_tiedosto(self, tiedosto):
        self.tiedosto = MidiFile(tiedosto)
        self.luettuja_tiedostoja += 1

    def tulosta_tiedoston_savelet(self):
        for i, raita in enumerate(self.tiedosto.tracks):
            print(f"Raita {i}: {raita.name}")
            soitetut_savelet = 0
            for viesti in raita:
                if not viesti.is_meta:
                    if viesti.type == "note_on":
                        print(viesti.note)
                        soitetut_savelet += 1
            print(f"Soitetut sävelet: {soitetut_savelet}")

    def palauta_raidan_savelet(self, raita_numero):
        raita = self.tiedosto.tracks[raita_numero]
        savelet = []
        for viesti in raita:
            if not viesti.is_meta:
                if viesti.type == "note_on":
                    savelet.append(viesti.note)
                    self.luettuja_savelia += 1
        return savelet

    def tallenna_polku_trieen(self, polku, trie):
        for tiedosto in os.listdir(polku):
            if tiedosto.endswith(".mid"):
                self.avaa_tiedosto(polku+tiedosto)
                savelet = self.palauta_raidan_savelet(1)
                trie.lisaa_savelet_trieen(savelet)

        print(f"Luettu {self.luettuja_tiedostoja} tiedostoa, joissa {self.luettuja_savelia} säveltä")
