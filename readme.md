# Automaattisäveltäjä Markovin ketjulla

## Nykyinen toiminta

Ohjelma luo käyttäjän antamien parametrien perusteella sävelmiä.

Ohjelmassa on (mielestäni) varsin yksinkertainen käyttöliittymä komentorivillä. [Käyttöohjeessa](dokumentaatio/käyttöohje.md) sen valintoja on hieman laajennettu, mutta en usko ohjeen olevan kovin tarpeellinen.

Komentoriviä käyttäessä on hyvä huomata, että käyttöliittymä kysyy syötteitä, kunnes se saa kelvollisen syötteen. Ohjelman pyöritykseen käytettävän Invoken takia syötteiden peruuttaminen ei onnistu, vaan ne tekevät näkymättömiä merkkejä syötteen perään. Eli jos kirjoitat jotain väärin, et pysty poistamaan väärää syötettä siltä riviltä, mutta voit kirjoittaa perään jotakin varmasti väärää ja painaa enter, niin pääse kokeilemaan uutta syötettä.

## Linkit

### Dokumentaatio

- [Määrittelydokumentti](dokumentaatio/määrittelydokumentti.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)
- [Käyttöohje](dokumentaatio/käyttöohje.md)
- [Toteutusdokumentti](dokumentaatio/toteutusdokumentti.md)

### Viikkoraportit

- [Viikko 1](dokumentaatio/viikkoraportit/viikko1.md)
- [Viikko 2](dokumentaatio/viikkoraportit/viikko2.md)
- [Viikko 3](dokumentaatio/viikkoraportit/viikko3.md)
- [Viikko 4](dokumentaatio/viikkoraportit/viikko4.md)
- [Viikko 5](dokumentaatio/viikkoraportit/viikko5.md)
- [Viikko 6](dokumentaatio/viikkoraportit/viikko6.md)

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
