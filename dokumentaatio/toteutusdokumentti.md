# Toteutusdokumentti

## Pakkausrakenne

src
* markovin_ketjut
   * Markovin ketjuja käyttävät luokat - pituuden ja korkeuden arpojat, sekä itse sävellykset muodostava luokka
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

Kaikkien ohjelman toimintojen pitäisi toimia O(n), ainakaan mikään kohta ei ole eksponentiaalinen.

### Trie

Dict-rakennetta käyttävän Trien lisäykset ja haut toimivat O(n) ajassa, kun n on trielle asetettu maksimisyvyys ([Trie, Wikipedia])(https://en.wikipedia.org/wiki/Trie#Algorithms). Tämän ohjelman nykyisellä toteutuksella jokaisen solmun lapset iteroidaan läpi ja katsotaan löytyykö etsittävää ääntä edustava solmu sieltä. Tämä saattaisi ensisilmäyksellä aiheuttaa korkeampaa aikavaativuutta.

On kuitenkin hyvä huomata, että lasten suurin mahdollinen määrä on tällä toteutuksella 12, joten iteroinnin aiheuttama lisätyö on erittäin vähäinen. Mielekkäiden lopputulosten kannalta trien maksimisyvyyden ei kannata olla kovin suuri (muuten vain kopioidaan lähdekappaleita). Tällä toteutuksella triestä hakemisen ja sinne lisäämisen pahimman tapauksen aikavaativuus on tarkemmin ilmaistuna O(12n) = O(n).

Tässä ohjelmassa triestä tehdään hakuja korkeintaan n - 1 pituisella kyselyllä, jolloin trie löytää n:nnen solmun vastauksena. Jos taas n - 1 kyselyllä ei löydy seuraavaa vaihetta, tehdään uusi kysely n - 2 pituisella aineistolla. Tällöin trie etsii n - 1 syvyydeltä solmua. Eli huonoimmassakin tapauksessa (ei löydy lainkaan vastaavuutta) jokainen seuraava kysely on edellistä lyhyempi.

### Markovin ketjut

Ohjelman käyttämät pituus- ja korkeusarpojat iteroivat omia taulukoitaan kertaalleen läpi. Tässä on hyvä huomata, että taulukoiden koko ei voi kasvaa, koska ne edustavat musiikin peruselementtejä - äänenkorkeus tulee aina pysymään 11 oktaavin sisällä. Iteroitava taulukko on yksiulotteinen. Näiden operaatioiden aikavaativuus on siis O(1).

Itse sävelmän muodostava Markovin ketju on puolestaan koko ohjelman monimutkaisin luokka. Tästä seuraa mielestäni suoraan se, että pelkän aikavaativuuden tarkastelu ei ole mielekästä, vaan kannattaa korostaa laskennallista vaativuutta. Käytännössä aikavaativuus on O(n), missä n on sävelmän tahtien määrä. Jokainen tahti koostuu ylhäältä rajoitetusta määrästä äänten pituuksia. Jokaisen äänen etsimistä varten tehdään useampi O(n) pituinen kysely: äänen haku Triestä, äänenkorkeuden arvonta, äänenpituuden arvonta. Eli siis aikavaativuus ei pääse nousemaan toiseen luokkaan, mutta operaatioita on melkoinen määrä.

Tästä seuraa se, että todella pitkien kappaleiden tekeminen ei skaalaudu erityisen hyvin, vaikka aikavaativuus näin saattaisikin antaa ymmärtää. Toisaalta ohjelman tavoitteena ei olekaan luoda pitkiä eepoksia.

## Suorituskyky

Suorituskykytestaus on käytännössä tarkoittanut luotujen sävelmien kuuntelua. Näistä testeistä on jonkin verran jätetty [aineistoa](Esimerkkisävelmiä/). Sävelmiä on luokiteltu sen mukaan, kuulostavatko ne omaan korvaan hyviltä / kiinnostavilta, vai tylsiltä tai liian erikoisilta.

Kuunnellessa ohjelmalla ei ole saatu aikaan käytännössä yhtäkään epävireiseltä kuulostavaa sävelmää. Monet sävelmät ovat kuulostaneet ikäviltä, mutta tämä on käytännössä aina johtunut äänenkorkeuden ja -pituuden arvonnasta. Ne ominaisuudet ovat enemmän ohjelmoijan itse tuottamia, joten malliaineistoa ei siitä voi syyttää.

Luotujen sävelmien tarkka kuuntelu on varsin työlästä, eikä sitä ole mahdollista automatisoida järkevällä työmäärällä. Tämän takia esimerkkiaineistoa on suhteellisen vähän, eikä siitä voida vakuuttavia tilastollisia päätelmiä tehdä. Havaitaan kuitenkin, että heikoksi todettujen sävelmien joukossa on huomattavasti enemmän matalan asteen sävellyksiä.

Ohjelman luonnissa tehty tyylivalinta irrottaa sävelten pituus ja korkeus malliaineistosta vaikuttaa merkittävästi siihen, miltä yksittäinen sävelmä kuulostaa. Epämääräisesti hyppivä tahditus ja oktaavit saavat melkein minkä vain kuulostamaan vähintäänkin haastavalta kuunneltavalta. Samoin taas "luonnolliselta" kuulostavat siirtymät saavat hieman tylsemmänkin melodian kuulostamaan musiikilta.

Kaiken kaikkiaan sanoisin, että Trien ja Markovin ketjun yhdistelmää käyttävä sävelten valinta toimii liki täydellisesti. Se tuottaa peräkkäin sopivia ja mukavan kuuloisia sävelkulkuja, jotka eivät kuitenkaan ole suoraan ennalta-arvattavia taikka noudata luonnollisia skaaloja orjallisesti. Tätä on helpointa tutkia tekemällä sävellyksiä C-duurista tai A-mollista, jolloin luonnolliseen skaalaan ei kuulu yhtäkään korotettua (#-merkillä varustettua) ääntä. Kun katsoo tällaisten sävelmien tulostuksia, niin valtaosa äänistä ovat suoraan skaalaan kuuluvia, mutta sekaan mahtuu muutamia särmää tuovia korotuksia - aivan kuin oikeissakin sävellyksissä.

## Jatkokehitysideoita

Tässä on pyritty listaamaan teknisiä kehitysideoita, mitä ohjelmassa olisi hyvä kehittää. [Määrittelydokumentissa](määrittelydokumentti.md) on listattu lisäominaisuuksiin keskittyviä kehitysideoita.

Trien toteutusta voisi tehostaa sillä, että jokaisessa solmussa olisi valmiiksi taulukko, johon talletetaan indeksiä vastaava sävel. Tällöin vältyttäisiin iteroinnilta ja operaatiot olisivat entistäkin nopeampia. Trie ei kuitenkaan tämän ohjelman toiminnassa ole minkäänlainen pullonkaula, ja siinä navigointi tapahtuu reaalimailmassa tehokkaasti.

Äänten pituus- ja korkeusarpojat olisi hyvä saada tuotua omiin tiedostoihinsa. Tällöin niitä voisi olla helpommin useampi ja pystyisi luomaan tyyliltään erilaisia sävelmiä. Näin myös todennäköisyyksien muokkaus olisi käyttäjälle lähestyttävämpää, kun ei tarvitse mennä koodia sorkkimaan.

## Lähteet

- [Trie, Wikipedia](https://en.wikipedia.org/wiki/Trie#Algorithms)
- [Markovin ketju, Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
- [Trie-artikkeli ja implementaatio, Gild Academy](https://medium.com/@info.gildacademy/a-simpler-way-to-implement-trie-data-structure-in-python-efa6a958a4f2)
- [Trie-artikkeli ja implementaatio, Shubhadeep Roychowdhury](https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1)
- [Trie-tutoriaali, GeeksforGeeks](https://www.geeksforgeeks.org/trie-insert-and-search/)
- [Midi-standradin kuvauksia](http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html)
- [Mido-kirjaston dokumentaatio](https://mido.readthedocs.io/en/latest/index.html)
- [Bach Inventions and Sinfonias](https://en.wikipedia.org/wiki/Inventions_and_Sinfonias_(Bach))
