# Määrittelydokumentti

### Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti (TKT), Helsingin yliopisto


### Ohjelmointikieli

Käytän työssä pääohjelmointikielenä pythonia. Vertaisarvioita varten myös Java on tuttu.

Kirjoitan dokumentaation suomeksi ja koodin (sis. docstringit) englanniksi.


### Algoritmit ja tietorakenteet projektissa

Olen selaillut erilaisia sokkelojen luomiseen soveltuvia algoritmeja ja suunnitelmissani on käyttää seuraavia algoritmeja:
- satunnainen syvyyshaku (recursive backtracker)
- Kruskalin algoritmi
- Rekursiivinen jakoalgoritmi (recursive division algorithm)


### Mitä ongelmaa sovellus ratkaisee

Tässä sovelluksessa käyttäjä voi vertailla kolmea sokkeloa luovaa algoritmia. Käyttäjä antaa syötteenä sokkelon koon (n * n). Sovellus luo  algoritmeilla halutun kokoisen sokkelon ja näyttää sen visuaalisen ilmentymän käyttäjälle. Lisäksi sovellus antaa dataa valittujen algoritmien suorituksista: 
- Sokkelon tyyppi (täydellinen, epätäydellinen jne)
- Kuinka kauan sokkelon luominen kesti
- Sokkelon umpikujien määrä


### Tavoitteena olevat aika- ja tilavaativuudet 

Sokkelon koolle on asetettava jonkinlainen maksimikoko niin, että sokkelon esittäminen näytöllä on järkevää. Se on kuitenkin oltava tarpeeksi iso, jotta aikavertailulla saadaan esille näkyviä eroja. Alustavasti n <= 200.

Aikavaativuudet:
- satunnainen syvyyshaku (recursive backtracker): O(n)
- Kruskalin algoritmi: O(E log V)
- Rekursiivinen jakoalgoritmi (recursive division algorithm): O(n)


### Lähteet

![Wikipedia: Maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

![John Stilley: Maze-generating algorithms](https://github.com/john-science/mazelib/blob/main/docs/MAZE_GEN_ALGOS.md)

![Survey Paper on Maze Generation Algorithms for Puzzle Solving Games](https://anoopmusale.github.io/resume/paper.pdf)

![Analysis of Maze Generating Algorithms](http://ipsitransactions.org/journals/papers/tir/2019jan/p5.pdf)




