# Käyttöohje

KESKEN - puuttuu vielä:
- Miten ohjelma suoritetaan
- miten eri toiminnallisuuksia käytetään
- Minkä muotoisia syötteitä ohjelma hyväksyy
- Missä hakemistossa on jar ja ajamiseen tarvittavat testitiedostot.
- kaaviot


### Sovelluksen käyttöönotto

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

Kopioi terminaalin antama url ja liitä se selaimen osoiteriville. Paina Enter.


### Sovelluksen käyttö

Pääset sisään sovellukseen ilman kirjautumista tai käyttäjätilin luontia. Anna lomakkeelle haluamasi sokkelon koko (n x n) ja sovellus luo kaksi sokkeloa: satunnaisen syvyyshakualgoritmin ja Kruskalin algoritmin mukaan. Sovellus piirtää sokkelot [Turtlella](https://docs.python.org/3/library/turtle.html), joten heti koon annettuasi aukeaa ikkuna, jossa sovellus piirtää kaksi sokkeloa ja tallentaa ne sitten kuvina. Kolmas sokkeloalgoritmi, rekursiivinen jakoalgoritmi, ei tällä hetkellä toimi oikein eikä tuota vielä kuvaa. 

Varoitus: isot sokkelot ovat _todella_ hitaita piirtää Turtlella, joten kannattaa kokeilla aluksi maltillisen kokoisella (esim. 5 - 10). Käyttöliittymä hyväksyy parametriksi luvut välillä 4-20. (Testiä ajaessa sovellus generoi arvoituista luvuista max 200 x 200 kokosia labyrinttejä.)


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

### Pylint-arvion ajaminen

Aja terminaalissa seuraava käsky:
```bash
pylint *.py
```


### Tiedossa olevat virheet

- Kruskalin algoritmilla generoidun sokkelon kuvaan reunojen sisälle jää yli 20x20 sokkeloissa valkoiset palkit oikeaan ja alareunaan (skaalausongelma?)
- Kun sovelluksella on luotu yksi setti sokkeloita, ja käyttäjä palaa etusivulle luomaan toista settiä, useimmiten (mutta ei ihan aina) sovellus kaatuu 'Generate mazes' nappia painettaessa. Syy tuntematon. Sovellus siis kannattaa buutata jokaisen ajon välissä (terminaalissa 'Ctrl+C').
