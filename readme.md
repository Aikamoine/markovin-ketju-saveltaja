# Automaattisäveltäjä Markovin ketjulla

## Nykyinen toiminta

Tällä hetkellä ohjelma ei tee muuta kuin luo yksinkertaisen sävelmän muutamasta vaihtoehdosta. Sävelmässä on 4 puolen sekunnin pituista ääntä. Sävelmät voivat olla:
- 1/3 todennäköisyydellä: A D C A
- 1/3 todennäköisyydellä: A D F B
- 1/3 todennäköisyydellä: B D A D

## Linkit

### Dokumentaatio

- [Määrittelydokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/määrittelydokumentti.md)
- [Testausdokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/testausdokumentti.md)

Seuraavat ovat tyhjiä, mutta alustettu
- [Käyttöohje](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/käyttöohje.md)
- [Toteutusdokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/toteutusdokumentti.md)

### Viikkoraportit

- [Viikko 1](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/viikkoraportit/viikko1.md)
- [Viikko 2](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/viikkoraportit/viikko2.md)

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
