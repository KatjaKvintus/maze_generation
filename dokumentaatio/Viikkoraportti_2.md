# Viikkoraportti 2

### Mitä olen tehnyt tällä viikolla?

Tällä viikolla työt ja toisen kurssin deadline veivät suurimman osan vapaa-ajastani, joten minulla on hyvin vähän näytettävää. Työaikaa kertyi vain kuusi tuntia [(ks.tuntikirjanpito)](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/tuntikirjanpito.md).

Olen lukenut lisää valitsemistani algoritmeista sekä kahlannut Youtubesta videoita eri tavoista visualisoida sokkelo. Näyttää siltä, että alkuperäinen ajatukseni keskittää kaikki sokkeloalgoritmit yhteen luokkaan ei toimikaan, vaan on kannattavampaa luoda jokaiselle oma luokka ja koota niihin kuhunkin algoritmiin liittyvät tarkistukset (ja visualisoinnit?). 

Ensimmäinen kokeiluni on backtracker.py -luokka. Rockets and Robotics -kanavalta löytyi [video](https://www.youtube.com/watch?v=jZQ31-4_8KM&t=216s), jossa esitettiin sokkelon luominen Pythonin [turtle-kirjastolla](https://docs.python.org/3/library/turtle.html). Turle oli minulle ennalta tuntematon ja sehän oli varsin näppärä! Testasin backtracker-luokassa videossa esiteltyä syvyyshakuun pohjautuvaa koodia ja se toimii, mutta en vielä saa sokkelonluomisanimaatiota talteen - Googlen mukaan senkin pitäisi onnistua. 

En ole ihan varma, että kuinka pitkälti tällä kurssilla saa käyttää valmista koodia - kyseessä ovat kuitenkin tunnetut algoritmit - vai onko luvallista vain ottaa ideoita ja kirjoittaa koodi alusta lähtien itse. Tällä hetkellä koodissa on suoraan kopioitu kaksi funktiota: syvyyhakualgoritmi, joka muodostaa sokkelon, ja toinen joka visualisoi sen turtlella. Omaan makuuni sokkeloalgoritmi on aika pitkä, ja pilkkoisin sen mielelläni testausta varten 2-4 osaan. 


### Miten ohjelma on edistynyt?

Olen löytänyt hyvän tavan visualisoida sokkelo satunnaisessa syvyyshaussa. Pitää selvittää, miten se toimisi muiden valitsemieni algoritmien kanssa. Minulla ei ole vielä mitään valmista, joten en ole kirjoittanut vielä testejäkään. 

Pylint-tarkistus antaa arvosanan 0.00/10 ja testien puuttuessa myös testien kattavuus on 0 %.


### Mitä opin tällä viikolla?

Tutustuin Pythonin turtle-kirjastoon ja erilaisiin logiikkoihin visualisoida sokkeloita.


### Mikä jäi epäselväksi tai tuottanut vaikeuksia? 

Minulle on epäselvää, onko koodin kopioiminen muista lähteistä luvallista ja jos on, missä määrin. 


### Mitä teen seuraavaksi?

Ensi viikon työlista:
- Algoritmien kirjoittaminen koodiksi
- Käyttöliittymän säätäminen niin, että sokkeloalgoritmi näyttää myös animaation sen rakentumisesta
- Sovelluksen toimintojen miettiminen: onko tarvetta käyttäjätilin luomiselle, sokkelotestien tulosten tallentamiselle tai tarkemmalle analyysille kahden sokkelon eroista? 
