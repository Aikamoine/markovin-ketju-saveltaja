"""
Käyttöliittymästä vastaava luokka
"""


class UI:
    """
    Luokka käyttäjän syötteiden validointiin
    """

    def tervetuloa(self):
        print("Tällä sovelluksella pääset luomaan mahtavia musikaalisia elämyksiä.")
        print("Aluksi sovellus kysyy sinulta parametreja kappaleen luontiin.\n")
        print("Jokaisen syötteen kohdalla voit lopettaa kirjoittamalla 'exit'\n")
        print("Jos teet virheen kirjoittaessa, niin backspace tai delete eivät toimi.")
        print("Sen sijaan voit kirjoittaa jotain hölynpölyä ja painaa enter - pääset aloittamaan syötteen alusta\n")

    def _syotteesta_numero(self, minimi, maksimi):
        """Kysyy käyttäjältä syötettä, kunnes tämä antaa numeroarvon minimin ja maximin väliltä
           Palauttaa syötteen kokonaislukuarvon
        Args:
            min: kokonaisluku
            max: kokonaisluku
        """
        while True:
            syote = input()
            if syote.isnumeric():
                luku = int(syote)
                if luku < minimi:
                    print("Liian pieni arvo")
                elif luku > maksimi:
                    print("Liian suuri arvo")
                else:
                    return luku
            if syote == "exit":
                exit()

    def kysy_syvyys(self):
        print("Anna trien syvyys. Tämä on myös Markovin ketjun aste. Suositus on väliltä 4 - 6.")
        return self._syotteesta_numero(2, 15)

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
        return self._syotteesta_numero(50, 250)

    def kysy_tahdit(self):
        print("Anna sävelmän tahtien määrä. Toistaiseksi tuetaan vain 4/4-rakennetta.")
        return self._syotteesta_numero(1, 30)
