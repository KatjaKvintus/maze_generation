# Määrittelydokumentti

### Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti (TKT), Helsingin yliopisto


### Ohjelmointikieli

Tässä työssä pääohjelmointikielenä on python ja sovelluksen ulkoasussa html. Vertaisarvioita varten myös Java on tuttu.

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

Sokkelon koolle on asetettava jonkinlainen maksimikoko niin, että sokkelon esittäminen näytöllä on järkevää. Se on kuitenkin oltava tarpeeksi iso, jotta aikavertailulla saadaan esille näkyviä eroja. Sovelluksessa raja on 4 <= n <= 20, mutta pelkkiä algoritmeja tutkiessa raja on 4 <= n <= 200.

Aikavaativuudet:
- Iteratiivinen syvyyshaku (iterative DFS): O(n)
- Kruskalin algoritmi: O(E log V)
- Aldous-Broderin algoritmi: on O(|V| + |E|), missä |V| on verkon solmujen ja |E| on kaarten lukumäärä


## Algoritmien tarkemmat kuvaukset

#### Iteratiivinen syvyyshaku (DFS)

Syvyyshaku (DFS) on verkkoalgoritmi, jolla voi hakea verkosta kaikki lähtösolmun kautta saavutettavat solmut. Se tutkii kaikki mahdolliset haarautumat yksi kerrallaan. Se käyttää aputietorakenteena pinoa. 

Iterative DFS on satunnaistettu versio syvyyshausta ja sitä voi käyttää labyrinttien generoimiseen. Se on yksi yksinkertaisimmista tavoista generoida satunnainen sokkelo. Se luo aina täydellisiä labyrinttejä eli kaikkiin soluihin pääsee kaikista soluista. Ovettomia huoneita ei muodostu. 

**Pseudokoodi:**

1.	Valitse aloitusruutu, merkitse se vierailluksi ja lisää pinoon
2.	Niin kauan kuin pino ei ole tyhjä:
   a) ota pinon päällimmäinen ruutu ja siirry siihen
   b)  Jos ruudulla on vierailemattomia naapureita:
      i) Lisää nykyinen ruutu pinoon
      ii) valitse arpomalla yksi vierailemattomista naapureita
      iii) poista seinä nykyisen ruudun ja naapurin väliltä
      iv) merkitse naapuri vierailluksi ja siirry siihen

Umpikujaan ajautuessaan algoritmi peruuttaa poimimalla pinosta viimeisimmän askelen yksi kerrallaan ja siirtyy sitten eteenpäin vasta siitä ruudusta, jolta löytyy vähintään yksi vierailematon naapuri. Kun kaikissa ruuduissa on käyty, algoritmi pysähtyy ja palauttaa labyrintin.

Tässä sovelluksessa mallinnan labyrintin kaksiulotteisena taulukkona. Taulukon jokainen solu sisältää nelipaikkaisen listan, jonka jokainen alkio on joko 1 tai 0. 1 tarkoittaa seinää, 0 ovea. Ensimmäinen alkio viittaan solun vasemmanpuoleiseen seinään, toinen kattoon, kolmas oikeanpuoleiseen seinään ja neljäs lattiaan. Kun seinä poistetaan, muutokset tehdään aina niihin kahteen soluun, joiden välillä seinä on. Algoritmi ei käy samoissa soluissa uudestaan, ellei se joudu peruuttamaan.






### Kruskalin algoritmi

1.	Kokoa lista verkon kaarista ja sekoita niiden järjestys
2.	Luo oma komponentti verkon jokaiselle solmulle
3.	Käy kaaret läpi:
   a.	Jos kaaren alku- ja loppusolmu ovat eri komponenteissa:
      i.	Pura seinä niiden väliltä
      ii. yhdistä setit samaan komponenttiin



### Aldous-Broderin algoritmi

1.	Valitse satunnainen ruutu ja merkitse se vierailluksi
2.	Niin pitkään kuin ruudukossa on vierailemattomia ruutuja:
   a.	Valitse satunnainen naapuriruutu
   b.	Jos tuossa ruudussa ei ole vielä käyty:
      i.	Poista seinä nykyisen ruudun ja naapurin välistä
      ii. Merkitse naapuriruutu vierailluksi
   c.	Siirry naapuriruutuun ja merkitse se nykyiseksi ruuduksi



### Lähteet

![Wikipedia: Maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

![Wikipedia: DFS](https://en.wikipedia.org/wiki/Depth-first_search)

![Wikipedia: Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

![John Stilley: Maze-generating algorithms](https://github.com/john-science/mazelib/blob/main/docs/MAZE_GEN_ALGOS.md)

![Survey Paper on Maze Generation Algorithms for Puzzle Solving Games](https://anoopmusale.github.io/resume/paper.pdf)

![Analysis of Maze Generating Algorithms](http://ipsitransactions.org/journals/papers/tir/2019jan/p5.pdf)




