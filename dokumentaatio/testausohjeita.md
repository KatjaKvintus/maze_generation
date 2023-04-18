# Testausohje

### Sovelluksen testaaminen

Lataa sovelluksen koodi oikean yläkulman vihreästä Code-napista (> Download zip). Pura zip-tiedosto omalle koneellesi. Avaa terminaali ja siirry sovellustiedostokansioon. Luo virtuaaliympäristö ja siirry sinne seuraavilla käskyillä:

```bash
python3 -m venv venv
source venv/bin/activate
```

Käynnistä sovellus terminaalissa seuraavalla käskyllä:

```bash
flask run
```

### Sovelluksen käyttö

Sovellus on vasta alustava runko. Pääset sisään ilman kirjautumista tai käyttäjätilin luontia. Anna lomakkeelle haluamasi sokkelon koko (n x n) ja sovellus luo kaksi sokkeloa: satunnaisen syvyyshakualgoritmin ja Kruskalin algoritmin mukaan. Sovellus piirtää sokkelot [Turtlella](https://docs.python.org/3/library/turtle.html), joten heti koon annettuasi aukeaa ikkuna, jossa sovellus piirtää kaksi sokkeloa ja tallentaa ne sitten kuvina.

Varoitus: isot sokkelot ovat hitaita piirtää Turtlella, joten kannattaa kokeilla aluksi maltillisen kokoisella (esim. 5 - 20).

En ole ehtinyt testata sovellusta ollenkaan toisella koneella, joten on ihan mahdollista, että mikään ei toimi. 

[requirements.txt](https://github.com/KatjaKvintus/maze_generation/blob/main/requirements.txt) -tiedostosta näkyy vaaditut riippuvuudet (mm. Flask ja Pillow).


### Tiedossa olevat virheet

- Kruskalin algoritmilla generoidun sokkelon kuvaan reunojen sisälle jää yli 20x20 sokkeloissa valkoiset palkit oikeaan ja alareunaan (skaalausongelma?)
- Kun sovelluksella on luotu yksi setti sokkeloita, ja käyttäjä palaa etusivulle luomaan toista settiä, useimmiten (mutta ei ihan aina) sovellus kaatuu 'Generate mazes' nappia painettaessa. Syy tuntematon
