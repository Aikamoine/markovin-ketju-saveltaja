import datetime
from mido import Message, MidiFile, MidiTrack


def luo_aikaleima():
    aika = datetime.datetime.now()
    return aika.strftime("%Y%m%d%H%M%S")


def lisaa_raitaan(raita, savel, kesto):
    print(f"Lisätään ääni {savel} kestolla {kesto}")
    #raita.append(Message('note_on', note=savel, velocity=64))
    raita.append(Message('note_on', note=savel, velocity=64, time=kesto))


def poista_raidasta(raita, savel, aika):
    print(f"Poistetaan ääni {savel} kestolla {aika}")
    raita.append(Message('note_off', note=savel, velocity=127, time=aika))


def duurisointu(pohja_aani):
    return [pohja_aani, pohja_aani + 4, pohja_aani + 7]


def mollisointu(pohja_aani):
    return [pohja_aani, pohja_aani + 3, pohja_aani + 7]


def edista_raitaa(raita, aika):
    poista_raidasta(raita, 0, aika)


mid = MidiFile()
soinnut = MidiTrack()
savelet = MidiTrack()
mid.tracks.append(soinnut)
mid.tracks.append(savelet)

soinnut.append(Message('program_change', program=1, time=0))
savelet.append(Message('program_change', program=1, time=0))

c_duuri = duurisointu(48)
g_duuri = duurisointu(55)
a_molli = mollisointu(57)
f_duuri = duurisointu(53)

sointukulku = [c_duuri, g_duuri, a_molli, f_duuri]  # //optimistinen
#sointukulku = [a_molli, f_duuri, c_duuri, g_duuri] //pessimistinen

for i in range(2):
    for sointu in sointukulku:
        for aani in sointu:
            lisaa_raitaan(soinnut, aani, 0)
        edista_raitaa(soinnut, 1000)

lisaa_raitaan(savelet, 60, 0)
poista_raidasta(savelet, 60, 1000)
lisaa_raitaan(savelet, 72, 0)
poista_raidasta(savelet, 72, 500)
lisaa_raitaan(savelet, 71, 0)
poista_raidasta(savelet, 60, 1000)
lisaa_raitaan(savelet, 67, 0)
poista_raidasta(savelet, 60, 1000)
lisaa_raitaan(savelet, 65, 0)
poista_raidasta(savelet, 72, 500)
lisaa_raitaan(savelet, 64, 0)
poista_raidasta(savelet, 60, 2000)
lisaa_raitaan(savelet, 52, 0)
poista_raidasta(savelet, 52, 2000)

mid.save(f'src/savellykset/testisavelma{luo_aikaleima()}.mid')
