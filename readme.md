# Automaattisäveltäjä Markovin ketjulla

## Nykyinen toiminta

Tällä hetkellä ohjelma ei tee muuta kuin luo yksinkertaisen sävelmän, jolla voi testata midi-tiedoston muodostusta. Yksikkötesteissä on vain yksi testi, eikä sekään liity ohjelman toimintaan.

## Linkit

### Dokumentaatio

- [Määrittelydokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/määrittelydokumentti.md)

Seuraavat ovat tyhjiä, mutta alustettu
- [Käyttöohje](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/käyttöohje.md)
- [Testausdokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/testausdokumentti.md)
- [Toteutusdokumentti](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/toteutusdokumentti.md)

### Viikkoraportit

- [Viikko 1](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/master/dokumentaatio/viikkoraportit/viikko1.md)

## Asennus ja komentorivitoiminnot

Lataa ohjelma ja mene komentorivillä ohjelman kansioon

Asenna Poetryn avulla riippuvuudet komentorivillä:
```bash
poetry install
```

Voit luoda testisävelmän komennolla. Sävelmä muodostuu kansioon (./src/savellykset):
```bash
poetry run invoke testisavelma
```

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testien haaraumakattavuudesta saat luotua raportin komennolla:

```bash
poetry run invoke kattavuusraportti
```

Pylint-tyylitarkastukset ajetaan komennolla:

```bash
poetry run invoke lint
