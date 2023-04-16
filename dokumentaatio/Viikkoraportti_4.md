# Viikkoraportti 4

### Mitä olen tehnyt tällä viikolla?

Aikaa on mennyt ihan hirveästi oman koodin debuggaamiseen. Tällä hetkellä valmiina on kaksi sokkeloalgoritmia ja niiden piirtäminen kuviksi. Nettiapista on valmiina runko, joka näyttää aika karulta, mutta perustoiminnallisuudet löytyvät. Sain viimein testit toiminaan ja syvyyshakualgoritmille on nyt kohtuullisen kattavat testit.


## Miten ohjelma on edistynyt?

Olen kirjoittanut Kruskalin algoritmilla luotavan labyrintin ja visualisoinnin sille. Kirjoitin myös testit syvyyshakualgoritmille.

Pylint-tarkistus antaa arvosanan 8.77/10 ja testikattavuus on seuraava:




### Mitä opin tällä viikolla?

Opin enemmän Turtle-moduulin käyttöä.


### Mikä jäi epäselväksi tai tuottanut vaikeuksia? 

Turtle piirtää pienet sokkelot nopeasti, mutta esim. 100x100 -sokkelon piirtämiseen menee ihan liikaa aikaa. Jos löytyy vähällä vaivalla parempi piirtosysteemi, vaihdan siihen.

Toinen ongelma on tiedosto kruskal.py, joka sisältää kruskalin algoritmin metodien lisäksi myös luokat Cell ja Edge. En keksi, miten niille pitäisi kirjoittaa testit.

### Mitä teen seuraavaksi?

Kirjoitan kolmannen algoritmin (Prim) ja sille visualisoinnin + testit. Sen jälkeen mietin webapin ulkoasua vähän fiksummaksi ja teen dokumentaatiota.


### Ensi viikon työlista:
- Primin algoritmin kirjoitus
- Webapin ulkoasun säätöä
- Dokumentaation kirjoitusta
