# Automaattisäveltäjä Markovin ketjulla

## Perustietoja

- Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti
- Projektin dokumentaatiokieli: suomi
- Projektin koodikieli: python

## Sovellus

Tarkoituksena on toteuttaa ohjelma, joka Markovin ketjuja hyödyntäen osaa "säveltää" malliaineiston pohjalta. Malliaineiston tiedot tallennetaan trie-tietorakenteeseen. Kun malliaineisto on muodostettu, generoidaan sen pohjalta satunnainen melodia.

Jos ohjelmalle pitää määritellä jokin käyttötarkoitus, niin se olisi toimia ihmismuusikon inspiraation lähteenä. Näin ollen ensisijainen prioriteetti ei ole, että tuotetut tiedostot olisivat valmiita kappaleita, vaan että ne olisivat uniikkeja, melodisia. 

Malliaineistosta otetaan talteen vain toisiaan seuraavat äänet. Niiden korkeuksia tai kestoja ei tallenneta, vaan ne tuotetaan toisistaan riippumatta. Näin saadaan aikaan sekä uniikimpia että kaoottisempia sävelmiä.

### Algoritmit ja tietorakenteet

Markovin ketju on luonteva ratkaisu sointukulkujen "opetteluun" ja uusien luomiseen. 

Trie on puolestaan hyvä tietorakenne sointukulkujen tallentamiseen, koska käytännössä soinnut muodostavat sanoja, joita käydään läpi kirjain kirjaimelta.

Muita itse implenetoitavia luokkia ja tietorakenteita:
- midi-tiedostojen muodostamiseen käytettävä luokka
- musiikin peruselementtien, kuten sävelten, sointujen ja skaalojen käsittelyä helpottavia luokkia

### Malliaineisto

Käytetään malliaineistona Johann Sebastian Bachin [nuottiaineistoja](https://www.mutopiaproject.org/cgibin/make-table.cgi?Composer=BachJS). Aineistot ovat tekijänoikeuden ulkopuolella, joten ne ovat vapaasti käytettävissä. Ohjelman kansioon on ladattuna Bachin Inventionit ja Sinfoniat.

### Jatkokehitysideoita

Tässä on pyritty listaamaan ominaisuuksia, mitä ohjelmassa olisi hyvä kehittää. [Toteutusdokumentissa](toteutusdokumentti.md) on listattu hieman lisää teknisempiä kehitysideoita.

Alustavasti määrittelyn ulkopuolelle jätetään moniraitaisten sävellysten luominen. Ensimmäinen perustoiminnallisuuden ulkopuolinen tavoite on tehdä ohjelma, joka osaa luomiensa sävellysten päälle generoida sointuja ja näin tehdä musikaalisempia teoksia. Tämä ominaisuus toteutettu viikon 5 aikana siten, että jokaisen tahdin alkuun lisätään koko tahdin pituinen ääni harmoniassa tahdin ensimmäisen äänen suhteen.

Musiikista voisi tehdä luonnollisemman kuuloista muutamalla äänten voimakkuutta, samaan tapaan kuin ne oikeassa soitossa muuttuvat. Myös vaihtoehtoiset tahtilajit olisi hyvä lisäys ohjelmaan.

Harmonian mahdollisuuksia olisi mielenkiintoista tutkia enemmän. Voisiko sitä lukea malliaineistosta? Tämä vaatisi myös äänten pituuksien lukemista.

Etenkin äänten pituutta arpovan luokan kanssa olisi kiinnostavaa toteuttaa toisen asteen Markovin ketju, jolloin otettaisiin kaksi edellistä ääntä huomioon. Tästä saisi varmasti rakennettua tyypillisemmältä kuulostavia musikaalisia motifeja.

## Lähteet

Käytössä olleita lähteitä
- [Markovin ketju, Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
- [Trie-artikkeli ja implementaatio, Gild Academy](https://medium.com/@info.gildacademy/a-simpler-way-to-implement-trie-data-structure-in-python-efa6a958a4f2)
- [Trie-artikkeli ja implementaatio, Shubhadeep Roychowdhury](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)
- [Trie-tutoriaali, GeeksforGeeks](https://www.geeksforgeeks.org/trie-insert-and-search/)
- [Midi-standradin kuvauksia](http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html)
- [Mido-kirjaston dokumentaatio](https://mido.readthedocs.io/en/latest/index.html)
- [Bach Inventions and Sinfonias](https://en.wikipedia.org/wiki/Inventions_and_Sinfonias_(Bach))
