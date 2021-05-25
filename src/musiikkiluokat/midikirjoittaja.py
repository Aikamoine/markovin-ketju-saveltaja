'''
Midikirjoittaja-luokka
'''
import datetime
from mido import Message, MidiFile, MidiTrack

class Midikirjoittaja():
    '''
    Olio, joka kirjoittaa Midi-raitaan sävelmän
    '''
    def __init__(self):
        '''
        Konstruktori
            mid: MidiFile-olio, johon kirjoitetaan äänet
            raidat: Midi-tiedostoon kirjoitettavat raidat.
                    Dictionary, jossa avaimena on raidan nimi ja arvona raita
        '''
        self.mid = MidiFile()
        self.raidat = {}

    def kirjoita_tiedosto(self):
        '''
        Tallentaa Midi-tiedoston.

        Todo: Tallennussijainti jotenkin käyttäjän päätettäväksi
        '''
        aikaleima = self._luo_aikaleima()
        tiedostonimi = f'src/savellykset/savelma{aikaleima}.mid'
        self.mid.save(tiedostonimi)
        print(f"Tallennettu {tiedostonimi}")

    def _luo_aikaleima(self):
        '''
        Palauttaa aikaleiman tiedston nimeä varten
        '''
        aika = datetime.datetime.now()
        return aika.strftime("%Y%m%d%H%M%S")

    def lisaa_raita(self, soitin, nimi):
        '''
        Lisää Midi-tiedostoon uuden sointiraidan

        args:
            soitin: Midi-standardin mukainen soittimen tunnus, kokonaisluku
            nimi: uuden raidan nimi
        '''
        raita = MidiTrack()
        raita.append(Message('program_change', program=soitin, time=0))
        self.mid.tracks.append(raita)
        self.raidat[nimi] = raita

    def lisaa_raitaan(self, nimi, savel, voimakkuus):
        '''
        Lisää äänen nimettyyn raitaan

        args:
            nimi: raita, johon lisätään - raidan tekstimuotoinen nimi
            savel: Sävel-olio, jonka mukainen ääni lisätään
            voimakkuus: kuinka kovaa ääni soitetaan. Midin oletusvoimakkuus on 64
        '''
        raita = self.raidat[nimi]
        raita.append(Message('note_on', note=savel.midi, velocity=voimakkuus, time=0))
        #self.mid.print_tracks()

    def poista_raidasta(self, nimi, savel, aika):
        '''
        Poistaa äänen raidasta. Raita edistyy annetun ajan verran.

        args:
            nimi: raita, johon lisätään - raidan tekstimuotoinen nimi
            savel: Sävel-olio, jonka mukainen ääni poistetaan
            aika: aika, jonka kohdalla poisto tapahtuu. Kokonaisluku mikrosekunteina
        '''
        raita = self.raidat[nimi]
        raita.append(Message('note_off', note=savel.midi, velocity=127, time=aika))

    def edista_raitaa(self, nimi, aika):
        '''
        Poistaa raidasta kaikista matalimman äänen ja edistää raitaa ajan verran
        Oletus on, että koko skaalan matalinta ääntä ei käytetä

        args:
            nimi: raita, johon lisätään - raidan tekstimuotoinen nimi
            aika: aika, jonka kohdalla poisto tapahtuu. Kokonaisluku mikrosekunteina
        '''
        raita = self.raidat[nimi]
        self.poista_raidasta(raita, 0, aika)

    def kirjoita_aanet_uuteen_raitaan(self, soitin, aanet, nimi):
        '''
        Luo uuden raidan ja kirjoittaa kaikki annetut äänet sinne.

        args:
            aanet: taulukko Säveliä
            nimi: raita, johon lisätään - raidan tekstimuotoinen nimi
        '''
        self.lisaa_raita(soitin, nimi)
        for aani in aanet:
            print(f"Lisätään midiin {str(aani)}")
            self.lisaa_raitaan(nimi, aani, 64)
            self.poista_raidasta(nimi, aani, 500)
        print()
        self.kirjoita_tiedosto()
