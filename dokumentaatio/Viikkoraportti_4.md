# Viikkoraportti 4

### Mitä olen tehnyt tällä viikolla?

Aikaa on mennyt ihan hirveästi oman koodin debuggaamiseen. Tällä hetkellä valmiina on kaksi sokkeloalgoritmia ja niiden piirtäminen kuviksi. Nettiapista on valmiina runko, joka näyttää aika karulta, mutta perustoiminnallisuudet löytyvät. Sain viimein testit toiminaan ja syvyyshakualgoritmille on nyt kohtuullisen kattavat testit.


## Miten ohjelma on edistynyt?

Olen kirjoittanut Kruskalin algoritmilla luotavan labyrintin ja visualisoinnin sille. Kirjoitin myös testit syvyyshakualgoritmille.

Pylint-tarkistus antaa arvosanan 8.77/10 ja testikattavuus on seuraava:

Name                  Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------
__init__.py               0      0      0      0   100%
backtracker.py          114     39     60      0    70%   150-208
backtracker_test.py      79      5     58      5    91%   101->105, 103, 106-107, 111, 115
kruskal.py              132     64     66      1    48%   24, 53->exit, 132-221, 228-235
kruskal_test.py          44      2     26      2    94%   53, 79
-----------------------------------------------------------------
TOTAL                   369    110    210      8    70%




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
