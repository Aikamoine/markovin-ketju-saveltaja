# Sävellysten luominen Markovin ketjuilla

## Asentaminen

Lataa ohjelman Release Githubista, tai kloonaa projekti. Pura mahdollinen zip-tiedosto.

Navigoi komentorivillä ohjelman päätasolle, eli markovin-ketju-saveltaja -nimiseen kansioon.

### Ensimmäisellä käyttökerralla

Asenna Poetryn avulla riippuvuudet komentorivillä:
```bash
poetry install
```

### Komentorivitoiminnot

Voit käynnistää ohjelman komennolla:
```bash
poetry run invoke main
```
Ohjelma tulostaa komentoriville vaiheita suorituksesta:
- sävelmän muodostuksen vaiheet
- midi-tiedoston kirjoituksen vaiheet
- lisäksi ohjelma tallentaa Trie-puun sisällön omaan [tiedostoonsa](https://github.com/Aikamoine/markovin-ketju-saveltaja/tree/main/src/trie/trie.txt)
   - Tätä tiedostoa ei ole repositoriassa, vaan se muodostuu vasta ensimmäisen ohjelman suorituksen jälkeen

Sävelmä muodostuu kansioon [src/savellykset](https://github.com/Aikamoine/markovin-ketju-saveltaja/tree/main/src/savellykset)


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

## Käyttöliittymä

### Käynnistysvalinnat

Ohjelman käynnistyessä voit tyhjällä syötteellä (eli kirjoittamatta mitään ja painamalla Enter) aloittaa perustoiminnallisuuden. Syötteellä "test" ohjelma suorittaa yksinkertaisen suorituskykytestin, jonka tulokset raportoidaan terminaaliin. Syöte "exit" lopettaa ohjelman missä vain kohdassa.

### Perustoiminnallisuus

Ohjelmaa käytetään komentoriviltä. Käynnistyksen yhteydessä kysytään käyttäjältä viisi lopputulokseen vaikuttavaa syötettä
- Trien syvyys: Tämä määrittää kuinka pitkiä yksittäisiä sävelketjuja muodostetaan. Mitä pidempi, niin sitä enemmän lopputulos seuraa malliaineiston osia.
- Molli vai duuri: Tehdäänkö kappale mollissa vai duurissa
- Kappaleen sävel: Missä sävelessä kappale tehdään. Molli/duuritiedon kanssa tämä muodostaa sävellajin
- Tempo: Tämä on kappaleen nopeus. Annettu yksikkö on neljäsosanuotin pituus, joka puolestaan on iskuja per minuutti. Hyvin tyypillinen tempo on 120.
- Sävelmän pituus: Kuinka monta tahtia sävelmään tuodaan. Kannattaa tehdä sopivan pitkä, että on jotain kuunneltavaa. Temmosta riippuen kiva pituus on 6 - 16.
   - Maksimipituus on 30 tahtia. Tämä alkaa olla jo aika pitkä siinä mielessä, että sävelmä ei "mene mihinkään". Tietysti pitkässä sävelmässä voi olla enemmän hienoja kohtia.

### Käyttäjän kirjoitusvirheistä ohjelman suorituksen aikana
Komentoriviä käyttäessä on hyvä huomata, että käyttöliittymä kysyy syötteitä, kunnes se saa kelvollisen syötteen. Ohjelman pyöritykseen käytettävän Invoken takia syötteiden peruuttaminen ei onnistu, vaan ne tekevät näkymättömiä merkkejä syötteen perään. Eli jos kirjoitat jotain väärin, et pysty poistamaan väärää syötettä siltä riviltä, mutta voit kirjoittaa perään jotakin varmasti väärää ja painaa enter, niin pääse kokeilemaan uutta syötettä.

## Valmis kappale

Kun ohjelma on pyörähtänyt, ilmoittaa se komentorivillä mihin ja millä nimellä uusi kappale on tehty. Tiedoston polku ilmoitetaan suhteessa ohjelman juureen, mistä ohjelmakin ajetaan.

Huom! Midi-soittimissa on huomattavia eroja ja ne todella vaikuttavat äänen laatuun - enemmän kuin kuulokkeet. Fuksiläppäriltä pitäisi löyty TiMidity, joka on suhteellisen hyvä.

## Manuaalisemmat toiminnot

### Lähdemateriaalin muuttaminen

Ohjelman mukana tulee Bachin useita sävellyksiä, jotka käytetään lähdemateriaalina. Materiaali on ohjelman kansiossa (src/musiikkidata). Tänne voit lisätä uusia .mid -tiedostoja, tai koittaa poistaa jo olemassaolevia. Huom! Tiedostossa tulee lukea missä sävellajissa kyseinen kappale on - tämä ei ole Mideissä aina taattua. [Täältä](https://www.mutopiaproject.org/) klassisia pianosävellyksiä hakiessa sen ei pitäisi olla ongelma.

Huom! Jos nappaat jostakin tekijänoikeuden alaista lähdemateriaalia (ja luot sen avulla hittibiisin), niin tämän sovelluksen tekijä ei vastaa siitä etteikö alkuperäisen kappaleen tekijä tulisi perimään sinulta korvauksia.

### Todennäköisyyksien muuttaminen

Ohjelman koodissa luokat [Korkeusarpoja](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/main/src/markovin_ketjut/korkeusarpoja.py) ja [Pituusarpoja](https://github.com/Aikamoine/markovin-ketju-saveltaja/blob/main/src/markovin_ketjut/pituusarpoja.py) sisältävät taulukot, joiden perusteella arvotaan sävelten pituuksia ja korkeuksia. Näitä taulukoita voi halutessaan muuttaa, jos haluaa yrittää luoda erityyppisiä sävelmiä. Varmista kuitenkin, että jokaisen rivin yhteissumma on 100, muuten arvonta ei ole tasapuolinen.
