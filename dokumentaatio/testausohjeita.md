# Testausohje

### Sovelluksen testaaminen

Lataa sovelluksen koodi oikean yläkulman vihreästä Code-napista (> Download zip). Pura zip-tiedosto omalle koneellesi. Avaa terminaali ja siirry sovellustiedostokansioon. Luo virtuaaliympäristö ja siirry sinne seuraavilla käskyillä:

```bash
python3 -m venv venv
source venv/bin/activate
```

Asenna riippuvuudet käskyllä:

```bash
pip install -r requirements.txt
```

Käynnistä sovellus terminaalissa seuraavalla käskyllä:

```bash
flask run
```

### Vertaisarviossa huomatut ongelmat

Jos kone herjaa kuvatiedostojen sijainnista, niiden ohjaaminen juureen static-kansion sijaan voi auttaa. Minun koneellani (fuksiläppäri 2021, Ubuntu 22.04.2 LTS) ohjelma toimii molemmilla tavoilla. (Ensimmäinen vertaisarvio löytyy [täältä](https://github.com/KatjaKvintus/maze_generation/issues/1).)

Toinen vertaisarvio osoitti, että joillakin koneilla testiluokkien importtien muotoa täytyy muuttaa jotta testit menevät läpi. Yritin korjata tätä vaikka kuinka monella tavalla, mutta ohjelma hyväksyi vain oman tapani. Epäilen Flaskin olevan osallinen tähän sotkuun. ([Toinen vertaisarvio](https://github.com/KatjaKvintus/maze_generation/issues/2))


### Sovelluksen käyttö

Sovellus avautuu ilman kirjautumista tai käyttäjätilin luontia. Anna lomakkeelle haluamasi sokkelon koko (n x n) ja sovellus generoi kolme sokkeloa: iteratiivisen syvyyshakualgoritmin, Kruskalin algoritmin ja Aldous-Broderin algoritmin mukaan. Sovellus piirtää sokkelot [Turtlella](https://docs.python.org/3/library/turtle.html), joten heti koon annettuasi aukeaa ikkuna, jossa sovellus piirtää kaksi sokkeloa ja tallentaa ne sitten kuvina. Kolmas sokkeloalgoritmi, rekursiivinen jakoalgoritmi, ei tällä hetkellä toimi oikein eikä tuota vielä kuvaa. 

Varoitus: isot sokkelot ovat _todella_ hitaita piirtää Turtlella, joten kannattaa kokeilla aluksi maltillisen kokoisella (esim. 5 - 12).

[requirements.txt](https://github.com/KatjaKvintus/maze_generation/blob/main/requirements.txt) -tiedostosta näkyy vaaditut riippuvuudet (mm. Flask ja Pillow).


### Testien ajaminen

1. siirry terminaalissa virtuaaliympäristöön komennolla 
```bash
poetry shell
```
2. anna komento 
```bash
poetry run invoke test
```

### Testikattavuuden tarkistus

Aja terminaalissa seuraavat käskyt:
```bash
poetry shell
coverage run --branch -m pytest
coverage report -m
```

### Tiedossa olevat virheet

- Kruskalin algoritmilla generoidun sokkelon kuvaan reunojen sisälle jää yli 20x20 sokkeloissa valkoiset palkit oikeaan ja alareunaan (skaalausongelma?)
- Kun sovelluksella on luotu yksi setti sokkeloita, ja käyttäjä palaa etusivulle luomaan toista settiä, useimmiten (mutta ei ihan aina) sovellus kaatuu 'Generate mazes' nappia painettaessa. Syy tuntematon.
