'''
Savel-luokka
'''

class Savel():
    '''
    Sävelen tiedot sisällään pitävä olio
    '''
    def __init__(self, midi_aani):
        '''
        Konstruktori
            midi: midi-standardin mukainen äänen yksikkö, kokonaisluku 0 - 127
            aani: sävelen nimi, tekstimuuttuja väliltä A - G, korotettuna #
            korkeus: sävelen oktaavi, kokonaisluku välillä 0 - 10
        '''
        self.midi = midi_aani
        self.aani = midi_aani % 12
        self.korkeus = midi_aani // 12

    def __eq__(self, savel):
        '''
        Yhtäläisyysvertailu. Vain sävelen nimeä verrataan, ei korkeutta

        args:
            savel: Savel-olio
        '''
        if isinstance(savel, Savel):
            return self.aani == savel.aani
        return False


    def __str__(self):
        '''
        Tulostaa Sävelen nimen ja korkeuden. Korkeus ilmaistaan normaalina sävelkorkeutena,
        eli välillä -1 - 9
        '''
        savelet = ["C", "C#", "D", "D#", "E",
                   "F", "F#", "G", "G#", "A", "A#", "B"]
        return f"{savelet[self.aani]}{self.korkeus - 1}"
