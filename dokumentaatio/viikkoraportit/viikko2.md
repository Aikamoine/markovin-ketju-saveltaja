# Viikkoraportti 2

## Mitä olen tehnyt tällä viikolla

Olen toteuttanut ohjelman pääasialliset tietorakenteet jossakin määrin. Trie ja Markovin ketjulla sävellyksiä tekevät luokat ovat nyt valmiit.

Sanoisin, että Trie on ainakin lopullisessa muodossa, Markov tulee ehkä vielä hieman muuttumaan, kun ohjelman lopullinen rakenne selkiytyy.

Tämän lisäksi olen tehnyt testit uusille luokille ja luonut yksinkertaisen pääfunktion, joka tuottaa esimerkkisävelmän uusia luokkia käyttäen.

## Miten ohjelma on edistynyt

Ohjelma on edistynyt vähintään erittäin hyvin. En odottanut Trien ja Markovin ketjun syntyvän näin "helpolla".

## Mitä opin tällä viikolla

Tämä viikko keskittyi ehkä enemmän ohjelmointirutiinin kehitykseen kuin uuden oppimiseen. Uusien luokkien teorian kun opiskelin viime viikon aikana.

Opin ainakin, että tietorakenteita luodessa on helppo jumiutua liian monimutkaiseen ajatustapaan, josta irtoaminen kaipaa joko ulkopuolista katselijaa tai selkeää taukoa ohjelmoinnista.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia

En ole vielä päättänyt / keksinyt miten teen sävelmien muodostamisen, kunhan saan oikeaa materiaalia luettua sisään. Tällä hetkellä ohjelma pystyy luomaan satunnaisen sävelmän siinä mielessä, että ohjelman käynnistäessä käyttäjä ei voi tietää mikä sävelmä tuotetaan, mutta sävelmä on deterministisesti jokin aineistoon syötetyistä (tai sellaisen osa).

Mikä olisi hyvä konsti lähteä luomaan satunnaista sävelmää heti alusta, tai ensimmäisestä sävelestä? Kannattaisiko ensin luoda esimerkiksi 1. - 4. asteen Markovin ketjuilla sävelmä, joka seuraa jotakin malliaineiston sävelmää, ja sen jälkeen palata 1. asteeseen luodun sävelmän viimeisimmän äänen perusteella? Tai kulkea asteita logiikalla 1., 2., 3., 4., 3., 2., 1., 2. tms?

## Mitä teen seuraavaksi

Seuraavaksi keskityn tuottamaan malliaineiston. Todennäköisesti yritän viritellä luokan, joka lukee midi-tiedostoja ja ottaa niistä sävelet ulos. Toinen vaihtoehto on lukea Lilypond-tiedostojen tekstimuotoa. Tämä tosin vaikuttaa haastavammalta kuin midien lukeminen. 

Tutustun joka tapauksessa Lilypondin maailmaan, koska ohjelmani tekemistä sävelmistä olisi varmasti ihan kiva pystyä tuottamaan jonkinlainen aineisto, että mitä siinä on soitettu.

## Käytetty aika

Aikaa olen käyttänyt 15 - 20 h. Ohjelmointiin on tästä mennyt 10 - 13 h ja muu aika teorian lukemiseen sekä dokumentointiin.
