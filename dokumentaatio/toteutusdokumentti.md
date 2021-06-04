# Toteutusdokumentti

## Pakkausrakenne

src
* markovin_ketjut
   * Markovin ketjuja käyttävät luokat - pituuden ja korkeuden arpojat, sekä itse sävellykset muodostovan luokan
* musiikkidata
   * ohjelman lähdemateriaalina käytettävät Midi-tiedostot
* musiikkiluokat
   * musiikin luomisen peruselementit, sekä miditiedostojen kirjoitusluokat
* savellykset
   * tänne tallentuu kaikki ohjelman tekemät kappalleet
* tests
* trie
   * trie-tietorakenteen luokat, sekä ohjelman suorituksessa muodostetun trien kuvaus
* main.py
   * pääohjelma, joka ajetaan Poetryllä
* ui.py
   * käyttäjän kanssa kommunikoinnista vastaava luokka

## Aikavaativuus

Periaatteessa kaikkien ohjelman toimintojen pitäisi toimia O(n), ainakaan mikään kohta ei ole eksponentiaalinen.

Trien lisäykset ja haut toimivat O(n) ajassa, kun n on trielle asetettu maksimisyvyys. 

## Lähteet

[Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie#Algorithms)
