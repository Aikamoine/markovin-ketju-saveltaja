'''
Midilukija-luokka
'''

import os
from mido import MidiFile

class Midilukija:
    '''
    Olio, joka osaa lukea Midi-tiedostosta soitindataa

    tiedosto = MidiFile-olento, joka sisältää kulloinkin avatun tiedoston
    luettuja_tiedostoja = käsiteltyjen tiedostojen määrä
    luettuja_savelia = käsiteltyjen sävelten määrä
    '''
    def __init__(self):
        '''
        Konstruktori
        '''
        self.tiedosto = None
        self.luettuja_tiedostoja = 0
        self.luettuja_savelia = 0

    def avaa_tiedosto(self, tiedosto):
        '''
        Alustaa tiedoston mukaisesta polusta MidiFile-olennon

        args:
            tiedosto: avattavan tiedoston suhteellinen polku
        '''
        self.tiedosto = MidiFile(tiedosto)
        self.luettuja_tiedostoja += 1

    def tulosta_tiedoston_aanet(self):
        '''
        Tulostaa terminaaliin kaikki tiedostossa soitettujen äänien sävelen
        '''
        for i, raita in enumerate(self.tiedosto.tracks):
            print(f"Raita {i}: {raita.name}")
            soitetut_aanet = 0
            for viesti in raita:
                if not viesti.is_meta:
                    if viesti.type == "note_on":
                        print(viesti.note)
                        soitetut_aanet += 1
            print(f"Soitetut sävelet: {soitetut_aanet}")

    def palauta_raidan_aanet(self, raita_numero):
        '''
        Syöttää taulukkoon kaikki yhdellä midi-raidalla olevat soitetut sävelet

        args:
            raita_numero: raidan numero midi-tiedostossa, kokonaisluku
        '''
        raita = self.tiedosto.tracks[raita_numero]
        aanet = []
        for viesti in raita:
            if not viesti.is_meta:
                if viesti.type == "note_on":
                    aanet.append(viesti.note)
                    self.luettuja_savelia += 1
        return aanet

    def tallenna_polku_trieen(self, polku, trie):
        '''
        Tallentaa kaikkien polussa olevien midi-tiedostojen soitetut sävelet trie-tietorakenteeseen

        args:
            polku: suhteellinen polku kansioon, jonka tiedostot luetaan
            trie: Trie-olio, johon tiedot tallennetaan
        '''
        for tiedosto in os.listdir(polku):
            if tiedosto.endswith(".mid"):
                self.avaa_tiedosto(polku+tiedosto)
                aanet = self.palauta_raidan_aanet(1)
                trie.lisaa_aanet_trieen(aanet)

        print(f"Luettu {self.luettuja_tiedostoja} tiedostoa, joissa {self.luettuja_savelia} säveltä")
