'''
Pääohjelma, joka ajetaan Invoken kautta
'''
from ui import UI

def main():
    """
    Luodaan käyttöliittymä ja käynnistetään se
    """
    kayttoliittyma = UI()
    kayttoliittyma.aloita()

if __name__ == "__main__":
    main()
