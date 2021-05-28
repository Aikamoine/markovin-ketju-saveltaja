# Sävellysten luominen Markovin ketjuilla

## Käyttöliittymä

Ohjelmaa käytetään komentoriviltä. Käynnistyksen yhteydessä kysytään käyttäjältä kolme lopputulokseen vaikuttavaa syötettä
- Trien syvyys: Tämä määrittää kuinka pitkiä yksittäisiä sävelketjuja muodostetaan. Mitä pidempi, niin sitä enemmän lopputulos seuraa malliaineiston osia.
- Tempo: Tämä on kappaleen nopeus. Annettu yksikkö on neljäsosanuotin pituus, joka puolestaan on iskuja per minuutti.
- Sävelmän pituus: Kuinka monta ääntä sävelmään tuodaan

## Lähdemateriaalin muuttaminen

Ohjelman mukana tulee Bachin useita sävellyksiä, jotka käytetään lähdemateriaalina. Materiaali on ohjelman kansiossa /src/musiikkidata. Tänne voit lisätä uusia .mid -tiedostoja, tai koittaa poistaa jo olemassaolevia. Huom! Tällä hetkellä tiedostosta luetaan vain ensimmäinen raita, joten moniääniset sävellykset voivat tässä mennä vähän hukkaan.
