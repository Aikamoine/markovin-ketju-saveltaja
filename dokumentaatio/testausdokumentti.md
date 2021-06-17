# Testausdokumentti

Testit ovat unittest-kirjastolla toteutettuja automaattisia yksikkötestejä. Tämän lisäksi on käytetty laajaa käyttäjätestausta.

Testit on toteutettu siten, että on katsottu ohjelmakoodista mitä kohtia testaus ei vielä kata. Tämän jälkeen on pohdittu mahdollisimman kattavasti, mitä kaikkia ongelmatilanteita kattamattomissa kohdissa on, ja luotu niille testit. Kun ohjelman edetessä on huomattu bugeja, joita testit eivät kata, on kyseisiin bugeihin luotu testi.

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testien haaraumakattavuudesta saat luotua raportin komennolla (tämä myös ajaa testit, eli ylempää komentoa ei tarvitse tehdä):

```bash
poetry run invoke kattavuusraportti
```

## Testikattavuus

Testikattavuus on pääpiirteittäin erittäin hyvällä tolalla. Oikeastaan ainoa vajavaisesti testattu luokka on [MarkovSavelma](src/markovin_ketjut/markov_savelma.py). 

Käytännössä kaikki muut kattavuuspuutteet ovat tyylivalintoja; metodit palauttavat jonkin arvon silmukasta, joka on kirjoitettu siten, että arvo palautuu aina. Kuitenkin tällaisiin metodeihin on loppuun laitettu palautusarvo, jotta pylint ei kiukuttele puuttuvista palautuksista.

MarkovSavelma-luokan testauksen puutteisiin on muutama syy. Suurin vaikuttava tekijä on ajan puute - joitakin metodeja on siis vain päätetty jättää testaamatta. Tämän lisäksi luokan metodit käyttävät melko paljon muita luokkia, jotka on jo testattu. Viimeisenä syynä testauksen puutteeseen täytyy tunnustaa, että koodin rakenne ei ole parasta mahdollista testien tekemiseen - työaika puolestaan ei ole riittänyt refaktorointiin tai haastaviin testitapauksiin.

## Yksikkötestauksen ulkopuolelle jätettyjä kokonaisuuksia

omit = src/tests/**, src/savellykset/**, src/main.py, src/ui.py, src/midiluokat/**

Muutamia kokonaisuuksia on päätetty jättää testaamatta. Näistä luonnollisia pois jätettäviä main ja ui -tiedostot. Main-tiedosto on jätetty pois, koska siinä ei ole sinänsä mitään haauramia, joiden testaaminen olisi tarpeen - lisäksi kaikki sen käyttämät toiminnallisuudet testataan muiden testien ohessa. Käyttäjän kanssa kommunikoiva UI-luokka on jätetty yksikkötestien ulkopuolelle, koska se ei tee kovin monimutkaisia toimintoja. Lisäksi sen käyttäjätestaaminen tapahtuu jokaisen ohjelman ajon yhteydessä.

Tämän lisäksi miditiedostoja manipuloivat luokat Midilukija ja Midikirjoittaja on päätetty jättää yksikkötestauksen ulkopuolelle. Tämä sen takia, että suurin osa niiden toiminnallisuuksista perustuu tiedostojen lukemiseen ja kirjoittamiseen. Tämä vaatisi yksikkötestauksen toimivuuden kannalta huomattavaa abstraktiota, enkä näe testien tuomaa hyötyä tässä tapauksessa.

## Suorituskykytestaus

Ohjelman suorituskyvyn testaaminen on ollut lähes täysin manuaalista. 

Käyttöliittymällä on mahdollista ajaa yksi suorituskykytesti, jossa Trieen luetaan malliaineisto useaan kertaan siten, että tiedostoja tulee yhteensä luettua 510 ja niistä poimitaan noin 150 000 säveltä. Tämä testi suorittaa omalla koneellani noin neljässä sekunnissa, mikä on suuren tiedostojen levyltä lukemisen määrän takia mielestäni oikein kelvollinen aika.

Muusta suorituskykytestauksesta on kerrottu tarkemmin [toteutusdokumentissa](dokumentaatio/toteutusdokumentti.md).

