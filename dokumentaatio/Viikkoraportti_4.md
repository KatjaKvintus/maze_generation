# Viikkoraportti 4

### Mitä olen tehnyt tällä viikolla?

Aikaa on mennyt ihan hirveästi oman koodin debuggaamiseen. Tällä hetkellä valmiina on kaksi sokkeloalgoritmia ja niiden piirtäminen kuviksi. Nettiapista on valmiina runko, joka näyttää aika karulta, mutta perustoiminnallisuudet löytyvät. Sain viimein testit toiminaan ja syvyyshakualgoritmille on nyt kohtuullisen kattavat testit.

Kirjoitin vertaisarviointia varten [lyhyen ohjeen](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/testausohjeita.md).

Aloitin testaus- ja toteutusdokumentaation kirjoittamisen:

![Testausdokumentti](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/testausdokumentti.md) (kesken)

![Toteutusdokumentti](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/toteutusdokumentti.md) (kesken)


### Miten ohjelma on edistynyt?

Olen kirjoittanut Kruskalin algoritmilla luotavan labyrintin ja visualisoinnin sille. Kirjoitin myös testit syvyyshakualgoritmille ja kruskalin algoritmille..

Pylint-tarkistus antaa arvosanan 8.77/10 ja testikattavuus on seuraava:

![](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/Testikattavuus%202023-04-6.png)

Tiedosto kruskal.py sisältää kruskalin algoritmin metodien lisäksi myös luokat Cell ja Edge, mutta en keksi, miten niille pitäisi kirjoittaa testit. Siksi kruskal.py:n testikattavuus on niin alhainen.


### Mitä opin tällä viikolla?

Opin enemmän Turtle-moduulin käyttöstä ja testien kirjoittamisesta.


### Mikä jäi epäselväksi tai tuottanut vaikeuksia? 

Turtle piirtää pienet sokkelot nopeasti, mutta esim. 100x100 -sokkelon piirtämiseen menee ihan liikaa aikaa. Jos löytyy vähällä vaivalla parempi piirtosysteemi, vaihdan siihen.

Testit ajetaan tällä hetkellä sotunnaisilla sokkeloilla, joiden sivu on 5-50. Kokeilen ensin niin, että max on 200, mutta testit kestivät tosi kauan, erityisesti kruskal.py:n osalta. Todennäköisesti siinä luokassa on turhaa hitautta, joka pitäisi pystyä siistimään pois. Max 50x50 sokkeloilla testiajo kestää yleensä 8-24 s.


### Mitä teen seuraavaksi?

Kirjoitan kolmannen algoritmin (Prim) ja sille visualisoinnin + testit. Sen jälkeen mietin webapin ulkoasua vähän fiksummaksi ja teen dokumentaatiota.


### Ensi viikon työlista:
- Primin algoritmin kirjoitus
- Webapin ulkoasun säätöä
- Dokumentaation kirjoitusta
- Sokkeloiden luontimisen keston seuraaminen ja kruskal.py:n nopeuttaminen
