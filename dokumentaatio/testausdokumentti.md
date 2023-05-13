# Testausdokumentti

Sovelluksen toimintaa testataan unittesteillä. Labyrinttien luomista koskevissa testeissä arvotaan viisi kokonaislukua (4-200), ja silmukassa ensin luodaan kunkin luvun kokoinen labyrintti ja suoritetaan niille testit. Testit keskittyvät labyrintteja generoiviin ja analysoiviin funktioihin, eivätkä ne käsittele labyrintin visualisoivia funktioita. Testien ajamiseen kuluu 3-8 minuuttia.

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



### Testikattavuus 16.4.2023
![Testikattavuus 16.4.2023](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/Testikattavuus%202023-04-6.png)


### Testikattavuus 23.4.2023

![](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/Testikattavuus%202023-04-23.png)


### Testikattavuus 30.4.2023

![](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/Testikattavuus%202023-04-30.png)


### Testikattavuus 7.5.2023

![](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/Testikattavuus%202023-05-07.png
)

### Pylint

Pylint-tarkastus antaa sovellukselle arvosanan 9.30/10. Kympistä sen tiputtaa mm. liian monimutkainen haarautuvuus genrointialgoritmeissa (too-many-branches) ja koodin toisteisuus (too-many-branches) kuvatiedostoja luovissa funktioissa. Tässä versiossa jokaiselle generointialgorimille on oma kuvanluontifunktio, vaikka ne voisi kohtuullisella säädöllä yhdistää.

