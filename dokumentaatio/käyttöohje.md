# Sävellysten luominen Markovin ketjuilla

## Käyttöliittymä

### Käynnistysvalinnat

Ohjelman käynnistyessä voit tyhjällä syötteellä aloittaa perustoiminnallisuuden. Syötteellä "test" ohjelma suorittaa yksinkertaisen suorituskykytestin, jonka tulokset raportoidaan terminaaliin. Syöte "exit" lopettaa ohjelman missä vain kohdassa.

### Perustoiminnallisuus

Ohjelmaa käytetään komentoriviltä. Käynnistyksen yhteydessä kysytään käyttäjältä viisi lopputulokseen vaikuttavaa syötettä
- Trien syvyys: Tämä määrittää kuinka pitkiä yksittäisiä sävelketjuja muodostetaan. Mitä pidempi, niin sitä enemmän lopputulos seuraa malliaineiston osia.
- Molli vai duuri: Tehdäänkö kappale mollissa vai duurissa
- Kappaleen sävel: Missä sävelessä kappale tehdään. Molli/duuritiedon kanssa tämä muodostaa sävellajin
- Tempo: Tämä on kappaleen nopeus. Annettu yksikkö on neljäsosanuotin pituus, joka puolestaan on iskuja per minuutti.
- Sävelmän pituus: Kuinka monta ääntä sävelmään tuodaan

Komentoriviä käyttäessä on hyvä huomata, että käyttöliittymä kysyy syötteitä, kunnes se saa kelvollisen syötteen. Ohjelman pyöritykseen käytettävän Invoken takia syötteiden peruuttaminen ei onnistu, vaan ne tekevät näkymättömiä merkkejä syötteen perään. Eli jos kirjoitat jotain väärin, et pysty poistamaan väärää syötettä siltä riviltä, mutta voit kirjoittaa perään jotakin varmasti väärää ja painaa enter, niin pääse kokeilemaan uutta syötettä.

## Valmis kappale

Kun ohjelma on pyörähtänyt, ilmoittaa se komentorivillä mihin ja millä nimellä uusi kappale on tehty. Tiedoston polku ilmoitetaan suhteessa ohjelman juureen, mistä ohjelmakin ajetaan.

Huom! Midi-soittimissa on huomattavia eroja ja ne todella vaikuttavat äänen laatuun - enemmän kuin kuulokkeet. Fuksiläppäriltä pitäisi löyty TiMidity, joka on suhteellisen hyvä.

## Manuaalisemmat toiminnot

### Lähdemateriaalin muuttaminen

Ohjelman mukana tulee Bachin useita sävellyksiä, jotka käytetään lähdemateriaalina. Materiaali on ohjelman kansiossa (src/musiikkidata). Tänne voit lisätä uusia .mid -tiedostoja, tai koittaa poistaa jo olemassaolevia. Huom! Tiedostossa tulee lukea missä sävellajissa kyseinen kappale on - tämä ei ole Mideissä aina taattua. [Täältä](https://www.mutopiaproject.org/) klassisia pianosävellyksiä hakiessa sen ei pitäisi olla ongelma.

### Todennäköisyyksien muuttaminen

Ohjelman koodissa luokat [Korkeusarpoja](src/markovin_ketjut/korkeusarpoja.py) ja [Pituusarpoja](src/markovin_ketjut/pituusarpoja.py) sisältävät taulukot, joiden perusteella arvotaan sävelten pituuksia ja korkeuksia. Näitä taulukoita voi halutessaan muuttaa, jos haluaa yrittää luoda erityyppisiä sävelmiä. Varmista kuitenkin, että jokaisen rivin yhteissumma on 100, muuten arvonta ei ole tasapuolinen.
