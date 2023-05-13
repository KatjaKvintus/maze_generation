# Testausdokumentti

Sovelluksen toimintaa testataan unittesteillä (59 kpl). Labyrinttien luomista koskevissa testeissä arvotaan testistä riippuen 5-20 kokonaislukua väliltä 4-200 labyrintin kooksi (n x n), ja silmukassa ensin luodaan kunkin luvun kokoinen labyrintti ja suoritetaan niille testit. Testit keskittyvät enemmän labyrintteja generoiviin ja analysoiviin funktioihin, ja jonkin verran analysointiin funktioihin, eivätkä ne juuri käsittele labyrintin visualisoivia funktioita. Testien ajamiseen kuluu 3-8 minuuttia.

Sovelluksen käyttöliittymässä on lisäksi CSS-scriptejä, jotka pitävät huolta, että käyttäjän antama syöte on oikeaa tyyppiä ja väliltä 4-20. Päädyin rajaamaan käyttöliittymässä labyrintin maksimikooksi 20x20, sillä sitä suurempien labyrinttien visualisointi kävi hyvin hitaaksi (ja Kruskalin algoritmin kohdalla myös itse generointi oli hitaahkoa).


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

### Testikattavuus

![](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/testikattavuus%202023-05-13.png)

Koska labyrintteja generoivat ja analysoinvat .py-tiedostot ovat juuressa (en saanut importteja toimimaan kansioiden välillä ja nytkin ne ovat vähän sinne päin), testikattavuus 97 % kattaa myös testitiedostot. Ns. päätiedostoilla eli genrointialgoritmiluokilla (aldous_broder.py, dfs.py ja kruskal.py) testien haaraumakattavuus on 99 - 100 %.

Testien ajaminen kestää keskimäärin 398,79 s (n. 6 min 39 s). Ajoin testit kymmenen kertaa ja ajoajat vaihtelivat 237,02 - 518,38 s välillä. 


### Pylint

Pylint-tarkastus antaa sovellukselle arvosanan 9.30/10. Kympistä sen tiputtaa mm. liian monimutkainen haarautuvuus genrointialgoritmeissa (too-many-branches) ja koodin toisteisuus (too-many-branches) kuvatiedostoja luovissa funktioissa. Tässä versiossa jokaiselle generointialgorimille on oma kuvanluontifunktio, vaikka ne voisi kohtuullisella säädöllä yhdistää.

