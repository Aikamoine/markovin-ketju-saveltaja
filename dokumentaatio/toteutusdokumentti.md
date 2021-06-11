# Toteutusdokumentti

## Pakkausrakenne

src
* markovin_ketjut
   * Markovin ketjuja käyttävät luokat - pituuden ja korkeuden arpojat, sekä itse sävellykset muodostovan luokan
* musiikkidata
   * ohjelman lähdemateriaalina käytettävät Midi-tiedostot
* musiikkiluokat
   * musiikin luomisen peruselementit
* midiluokat
   * miditiedostojen lukemiseen ja kirjoittamiseen käytettävät luokat
* savellykset
   * tänne tallentuu kaikki ohjelman tekemät kappaleet
* tests
* trie
   * trie-tietorakenteen luokat, sekä ohjelman suorituksessa muodostetun trien kuvaus
* main.py
   * pääohjelma, joka ajetaan Poetryllä
* ui.py
   * käyttäjän kanssa kommunikoinnista vastaava luokka

## Aikavaativuus

Periaatteessa kaikkien ohjelman toimintojen pitäisi toimia O(n), ainakaan mikään kohta ei ole eksponentiaalinen.

### Trie

Trien lisäykset ja haut toimivat O(n) ajassa, kun n on trielle asetettu maksimisyvyys [Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie#Algorithms).

Tässä ohjelmassa triestä tehdään hakuja korkeintaan n - 1 pituisella kyselyllä, jolloin trien pitäisi löytää n:nnes solmu vastauksena. Tällöin on selkeää, että kyselyn tehokkuus on O(n). Jos taas n - 1 kyselyllä ei löydy seuraavaa vaihetta, tehdään uusi kysely n - 2 pituisella aineistolla. Tällöin trie etsii n - 1 syvyydeltä solmua. Eli huonoimmassakin tapauksessa (ei löydy lainkaan vastaavuutta) jokainen seuraava kysely on edellistä lyhyempi.

Mielekkäiden lopputulosten kannalta trien maksimisyvyyden ei kannata olla kovin suuri, joten näiden operaatioiden aikavaativuutta voidaan pitää marginaalisena.



## Lähteet

[Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie#Algorithms)
