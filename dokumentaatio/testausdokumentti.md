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

## Yksikkötestauksen ulkopuolelle jätettyjä kokonaisuuksia

omit = src/tests/**, src/savellykset/**, src/main.py, src/ui.py, src/midiluokat/**

Muutamia kokonaisuuksia on päätetty jättää testaamatta. Näistä luonnollisia pois jätettäviä main ja ui -tiedostot. Main-tiedosto on jätetty pois, koska siinä ei ole sinänsä mitään haauramia, joiden testaaminen olisi tarpeen - lisäksi kaikki sen käyttämät toiminnallisuudet testataan muiden testien ohessa. Käyttäjän kanssa kommunikoiva UI-luokka on jätetty yksikkötestien ulkopuolelle, koska se ei tee kovin monimutkaisia toimintoja. Lisäksi sen käyttäjätestaaminen tapahtuu jokaisen ohjelman ajon yhteydessä.

Tämän lisäksi miditiedostoja manipuloivat luokat Midilukija ja Midikirjoittaja on päätetty jättää yksikkötestauksen ulkopuolelle. Tämä sen takia, että suurin osa niiden toiminnallisuuksista perustuu tiedostojen lukemiseen ja kirjoittamiseen. Tämä vaatisi yksikkötestauksen toimivuuden kannalta huomattavaa abstraktiota, enkä näe testien tuomaa hyötyä tässä tapauksessa.

## Suorituskykytestaus

Ohjelman suorituskyvyn testaaminen on ollut lähes täysin manuaalista. 

Käyttöliittymällä on mahdollista ajaa yksi suorituskykytesti, jossa Trieen luetaan malliaineisto useaan kertaan siten, että tiedostoja tulee yhteensä luettua 510 ja niistä poimitaan noin 150 000 säveltä. Tämä testi suorittaa omalla koneellani noin neljässä sekunnissa, mikä on suuren tiedostojen lukemisen määrän takia mielestäni oikein kelvollinen aika.

Muu suorituskykytestaus on käytännössä tarkoittanut luotujen sävelmien kuuntelua. Näistä testeistä on jonkin verran jätetty aineistoa polkuun (dokumentaatio/Esimerkkisävelmiä/). Tässä polussa sävelmiä on luokiteltu sen mukaan, kuulostavatko ne omaan korvaan hyviltä / kiinnostavilta, vai tylsiltä tai liian erikoisilta.

Kuunnellessa ohjelmalla ei ole saatu aikaan käytännössä yhtäkään epävireiseltä kuulostavaa sävelmää. Monet sävelmät ovat kuulostaneet ikäviltä, mutta tämä on käytännössä aina johtunut äänenkorkeuden ja -pituuden arvonnasta. Ne ominaisuudet ovat enemmän ohjelmoijan itse tuottamia, joten malliaineistoa ei siitä voi syyttää.
