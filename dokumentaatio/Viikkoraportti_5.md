# Viikkoraportti 5

### Mitä olen tehnyt tällä viikolla?

Luin uudestaan ajatuksella ensimmäisen viikon palautteen ja tajusin, että koska näytän vain valmiit labyrintit, minun pitää löytää Primille korvaaja, koska se tuottaa hyvin samanlaisia labyrinttejä kuin Kruskalin algoritmi. Joten olen viettänyt paljon aikaa Googlen ja Youtuben kanssa. Päädyin valitsemaan recursive division -algoritmin, jossa on erilainen lähestymistapa kuin kahdessa muussa.

Lisäksi löysin Kruskalin algoritmin visualisoinnista virheen, joka ilmenee vasta kun labyrintti on yli 20 x 20 -kokoinen, joten sen perkaamiseen on mennyt myös kiitettävästi aikaa. Tähän ei ole löytynyt vielä ratkaisua.


### Miten ohjelma on edistynyt?

Olen kirjoittanut recursive bactracker -algoritmille runkoa ja toistaiseksi se kääntyy, mutta ei tuota täydellistä labyrnttiä. Myöskään sen visualisointi ei toimi.

Pylint-tarkistus antaa arvosanan 8.32/10 ja testikattavuus on seuraava:

![](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/Testikattavuus%202023-04-23.png)

Raportista puuttuu kokonaan kolmannen algoritmin testit, joita ei ole vielä kirjoitettu.


### Mitä opin tällä viikolla?

Tutustuin recursive backtracker -algoritmiin syvällisemmin (ja moneen muuhun labyrinttejä luovaab algoritmiin, joista en ollut koskaan kuullutkaan).


### Mikä jäi epäselväksi tai tuottanut vaikeuksia? 

Kruskalin algoritmin visualisointi ei toimi oikein isoilla syötteillä. Ongelma on selvityksessä.

Rekursiivinen jakoalgoritmi ei tuota oikeanlaista labyrinttiä ja sen visualisointi ei toimi ollenkaan.


### Mitä teen seuraavaksi?

Kirjoitan Rekursiivinen jakoalgoritmi  valmiiksi + korjaan sen visualisoinnin ja kirjoitan testit. Korjaan Kruskan algoritmin visualisoinnin. Ja kirjoitan dokumentaatiota pidemmälle.


### Ensi viikon työlista:
- Rekursiivinen jakoalgoritmin kirjoitus valmiiksi
- Rekursiivinen jakoalgoritmin visualisoinnin kirjoitus valmiiksi
- Rekursiivinen jakoalgoritmin testien kirjoitus 
- Webapin ulkoasun säätöä
- Dokumentaation kirjoitusta
