# Automaattisäveltäjä Markovin ketjulla

## Nykyinen toiminta

Ohjelmassa on (mielestäni) varsin yksinkertainen käyttöliittymä komentorivillä. Käyttöohjeessa sen valintoja on hieman laajennettu, mutta en usko ohjeen olevan kovin tarpeellinen.

Ohjelma luo käyttäjän antamien parametrien perusteella sävelmiä. Tällä hetkellä ne kuulostavat hieman sattumanvaraisilta, koska äänten pituuksien arvontaan ei ole vielä panostettu kovin paljon. Kuitenkin teosten pitäisi kuulostaa suhteellisen melodisilta, eikä ainakaan epävireisiltä.

## Linkit

### Dokumentaatio

- [Määrittelydokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/määrittelydokumentti.md)
- [Testausdokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/testausdokumentti.md)
- [Käyttöohje](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/käyttöohje.md)

Seuraavat ovat tyhjiä, mutta alustettu

- [Toteutusdokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/toteutusdokumentti.md)

### Viikkoraportit

- [Viikko 1](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/viikkoraportit/viikko1.md)
- [Viikko 2](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/viikkoraportit/viikko2.md)
- [Viikko 3](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/viikkoraportit/viikko3.md)

## Asennus ja komentorivitoiminnot

Lataa ohjelma ja mene komentorivillä ohjelman kansioon

Asenna Poetryn avulla riippuvuudet komentorivillä:
```bash
poetry install
```

Voit käynnistää ohjelman komennolla:
```bash
poetry run invoke main
```
Ohjelma tulostaa komentoriville vaiheita suorituksesta; Trie-puun rakenteen, luodun sävelmän vaiheittain, sekä midi-tiedoston kirjoituksen.

Sävelmä muodostuu kansioon (./src/savellykset):


Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testien haaraumakattavuudesta saat luotua raportin komennolla (tämä myös ajaa testit, eli ylempää komentoa ei tarvitse tehdä):

```bash
poetry run invoke kattavuusraportti
```

Pylint-tyylitarkastukset ajetaan komennolla:

```bash
poetry run invoke lint
```
