Tähän mennessä toteutetut testit ovat unittest-kirjastolla toteutettuja automaattisia yksikkötestejä.

Testit on toteutettu siten, että on katsottu ohjelmakoodista mitä kohtia testaus ei vielä kata. Tämän jälkeen on pohdittu mahdollisimman kattavasti, mitä kaikkia ongelmatilanteita kattamattomissa kohdissa on, ja luotu niille testit. Kun ohjelman edetessä on huomattu bugeja, joita testit eivät kata, on kyseisiin bugeihin luotu testi.

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testien haaraumakattavuudesta saat luotua raportin komennolla (tämä myös ajaa testit, eli ylempää komentoa ei tarvitse tehdä):

```bash
poetry run invoke kattavuusraportti
```
