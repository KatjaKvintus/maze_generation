# Määrittelydokumentti

### Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti (TKT), Helsingin yliopisto


### Ohjelmointikieli

Käytän työssä pääohjelmointikielenä pythonia. Vertaisarvioita varten myös Java on tuttu.

Kirjoitan dokumentaation suomeksi ja koodin (sis. docstringit) englanniksi.


### Algoritmit ja tietorakenteet projektissa

Olen selaillut erilaisia sokkelojen luomiseen soveltuvia algoritmeja ja suunnitelmissani on käyttää seuraavia algoritmeja:
- satunnainen syvyyshaku (recursive backtracker)
- Primin algoritmi
- Kruskalin algoritmi
- Binääripuu


### Mitä ongelmaa sovellus ratkaisee

Tässä sovelluksessa käyttäjä voi vertailla kahta sokkeloa luovaa algoritmia. Käyttäjä antaa syötteenä sokkelon koon (n * n) ja valitsee sitten listasta kaksi sokkeloalgoritmia. Sovellus luo molemmilla algoritmeilla halutun kokoisen sokkelon ja näyttää sen visuaalisen ilmentymän käyttäjälle. Lisäksi sovellus antaa dataa valittujen algoritmien suorituksista: 
- Kuinka kauan sokkelon luominen kesti
- Onko sokkelolla 0, 1 vai useampi ratkaisu
- Sokkelon kompleksisuus (miten tämän voisi määritellä?)
(- Muita ominaisuuksia?)


### Tavoitteena olevat aika- ja tilavaativuudet 

Sokkelon koolle on asetettava jonkinlainen maksimikoko niin, että sokkelon esittäminen näytöllä on järkevää. Se on kuitenkin oltava tarpeeksi iso, jotta aikavertailulla saadaan esille näkyviä eroja. Alustavasti n <= 200.

Aikavaativuudet:
- satunnainen syvyyshaku (recursive backtracker): O(n)
- Primin algoritmi: O(E log V)
- Kruskalin algoritmi: O(E log V)
- Binääripuu: O(n)


### Lähteet

![Wikipedia: Maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

![John Stilley: Maze-generating algorithms](https://github.com/john-science/mazelib/blob/main/docs/MAZE_GEN_ALGOS.md)

![Survey Paper on Maze Generation Algorithms for Puzzle Solving Games](https://anoopmusale.github.io/resume/paper.pdf)

![Analysis of Maze Generating Algorithms](http://ipsitransactions.org/journals/papers/tir/2019jan/p5.pdf)




