'''
Käyttöliittymästä vastaava luokka
'''
class UI:
    '''
    Luokka käyttäjän syötteiden validointiin
    '''

    def _syotteesta_numero(self):
        while True:
            syote = input()
            if syote.isnumeric():
                return int(syote)
            if syote == "exit":
                exit()

    def kysy_syvyys(self):
        print("Anna trien syvyys. Tämä on myös Markovin ketjun aste. Suositus on väliltä 4 - 6.")
        return self._syotteesta_numero()

    def onko_molli(self):
        print("Tehdäänkö sävelmä mollissa vai duurissa? Kirjoita molli, tai duuri")
        molli = False
        while True:
            syote = input()
            if syote == "molli":
                molli = True
                break
            if syote == "duuri":
                molli = False
                break
            if syote == "exit":
                exit()
        return molli
    
    def kysy_savel(self):
        savelet = "C, C#, Db, D, D#, Eb, E, F, F#, Gb, G, G#, Ab, A, A#, Bb, B"
        print("Missä sävelessä sävelmä tehdään? Vaihtoehdot ovat:")
        print(savelet)

        savelet = savelet.replace(" ", "")
        savelet = savelet.split(",")
        while True:
            syote = input()
            if syote in savelet:
                break
            if syote == "exit":
                exit()
        return syote

    def kysy_tempo(self):
        print("Anna tempo. Suositus on 120 - 150.")
        return self._syotteesta_numero()
    
    def kysy_tahdit(self):
        print("Anna sävelmän tahtien määrä. Toistaiseksi tuetaan vain 4/4-rakennetta.")
        return self._syotteesta_numero()
