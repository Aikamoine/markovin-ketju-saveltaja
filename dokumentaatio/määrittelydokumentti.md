# Automaattisäveltäjä Markovin ketjulla

## Perustietoja

Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti
Projektin dokumentaatiokieli: suomi
Projektin koodikieli: python

## Sovellus

Tarkoituksena on toteuttaa ohjelma, joka Markovin ketjuja hyödyntäen osaa "säveltää" sointukulkuja malliaineiston pohjalta. Malliaineiston tiedot tallennetaan trie-tietorakenteeseen. Kun sointukulut on muodostettu, generoidaan niille satunnainen melodia, joka soveltuu sointuihin.

Määrittelyä täsmennetään, kunhan implementaatio edistyy. Tässä ollaan itselle uuden äärellä, joten kaikki täsmällisempi määrittely olisi puhdasta arvausta.

### Algoritmit ja tietorakenteet

Markovin ketju on luonteva ratkaisu sointukulkujen "opetteluun" ja uusien luomiseen. 

Trie on puolestaan hyvä tietorakenne sointukulkujen tallentamiseen, koska käytännössä soinnut muodostavat sanoja, joita käydään läpi kirjain kirjaimelta.

Muita itse implenetoitavia luokkia ja tietorakenteita:
- midi-tiedostojen muodostamiseen käytettävä luokka
- sävelten, sointujen ja skaalojen käsittelyä helpottava luokka
- luokka malliaineiston muodostamiseen 

### Malliaineisto

Alustava ajatus on käyttää malliaineistona Johann Sebastian Bachin [nuottiaineistoja](https://www.mutopiaproject.org/cgibin/make-table.cgi?Composer=BachJS). Aineistot ovat tekijänoikeuden ulkopuolella, joten ne ovat vapaasti käytettävissä.

Tämä osa työstä ei ole vielä tätä kirjoittaessa vahvistunut. Määrittely malliaineistolle on, että saadaan muodostettua tunnetun ja arvostetun säveltäjän teoksista sointukulkuja,

## Lähteet

Toistaiseksi käytössä olleita lähteitä
- [Markovin ketju, Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
- [Trie-artikkeli ja implementaatio, Gild Academy](https://medium.com/@info.gildacademy/a-simpler-way-to-implement-trie-data-structure-in-python-efa6a958a4f2)
- [Trie-artikkeli ja implementaatio, Shubhadeep Roychowdhury](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)
- [Trie-tutoriaali, GeeksforGeeks](https://www.geeksforgeeks.org/trie-insert-and-search/)
