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

### Iteratiivinen syvyyshaku (DFS)

Syvyyshaku (DFS) on verkkoalgoritmi, jolla voi hakea verkosta kaikki lähtösolmun kautta saavutettavat solmut. Se tutkii kaikki mahdolliset haarautumat yksi kerrallaan. Se käyttää aputietorakenteena pinoa. 

Iterative DFS on satunnaistettu versio syvyyshausta ja sitä voi käyttää labyrinttien generoimiseen. Se on yksi yksinkertaisimmista tavoista generoida satunnainen sokkelo. Se luo aina täydellisiä labyrinttejä eli kaikkiin soluihin pääsee kaikista soluista. Ovettomia huoneita ei muodostu. 

**Pseudokoodi:**

1.	Valitse aloitusruutu, merkitse se vierailluksi ja lisää pinoon
2.	Niin kauan kuin pino ei ole tyhjä:
   * ota pinon päällimmäinen ruutu ja siirry siihen
   * Jos ruudulla on vierailemattomia naapureita:
      + Lisää nykyinen ruutu pinoon
      +	valitse arpomalla yksi vierailemattomista naapureita
      + poista seinä nykyisen ruudun ja naapurin väliltä
   * merkitse naapuri vierailluksi ja siirry siihen

Umpikujaan ajautuessaan algoritmi peruuttaa poimimalla pinosta viimeisimmän askelen yksi kerrallaan ja siirtyy sitten eteenpäin vasta siitä ruudusta, jolta löytyy vähintään yksi vierailematon naapuri. Kun kaikissa ruuduissa on käyty, algoritmi pysähtyy ja palauttaa labyrintin.

Tässä sovelluksessa mallinnan labyrintin kaksiulotteisena taulukkona. Taulukon jokainen solu sisältää nelipaikkaisen listan, jonka jokainen alkio on joko 1 tai 0. 1 tarkoittaa seinää, 0 ovea. Ensimmäinen alkio viittaan solun vasemmanpuoleiseen seinään, toinen kattoon, kolmas oikeanpuoleiseen seinään ja neljäs lattiaan. Kun seinä poistetaan, muutokset tehdään aina niihin kahteen soluun, joiden välillä seinä on. Algoritmi ei käy samoissa soluissa uudestaan, ellei se joudu peruuttamaan.


### Kruskalin algoritmi

Kruskalin algoritmi on ahne algoritmi, jolla voidaan muodostaa suunnatun verkon pienin virittävää puu. 

Labyrinttien generoinnissa algoritmin käsittelemän verkon kaaret ovat painottomia ja kaaret suuntaamattomia. Jos kaksi solmua (ruutua) on vierekkäin, niiden välillä on kaari. Alussa jokainen solmu (ruutu) muodostaa oman komponenttinsa ja labyrintti muodostetaan yhdistelemällä komponentteja, kunnes kaikki solmut kuuluvat samaan komponenttiin. Polku muodostuu siis vasta lopussa.


**Pseudokoodi:**

1.	Kokoa lista verkon kaarista ja sekoita niiden järjestys
2.	Luo oma komponentti verkon jokaiselle solmulle
3.	Niin kauan kuin kaaria on käymättä läpi ja kaikki solut eivät ole samassa komponentissa
   * Jos kaaren alku- ja loppusolmu ovat eri komponenteissa:
      + Pura seinä niiden väliltä
      + Yhdistä setit samaan komponenttiin

Tässä sovelluksessa mallinnan labyrintin kaksiulotteisena taulukkona, jonka jokainen ruutu vastaa yhtä solmua verkossa. Taulukon jokainen ruutu sisältää listan, joka pitää kirjaa soluun saapuvista tai sieltä lähtevistä kaarista. Kun seinä poistetaan, muutokset tehdään aina niihin kahteen soluun, joiden välillä seinä on. Koska käsittelen taulukon ruutua tilana, jonka reunat ovat joko seinää tai avointa tilaan, sen sijaan että yksittäinen ruutu olisi seinää tai avointa tilaa, algoritmi on hitaahko.


### Aldous-Broderin algoritmi

Aldous-Broderin algoritmi muodostaa verkon pienimmän yhtenäisen virittävän puun. 

Labyrinttien generoinnissa tämä on helpohko toteuttaa, mutta varsinkin isoilla syötteillä saattaa osoittautua hyvin hitaaksi ja tehottomaksi. Sen hidasteena on sellainen piirre, että se saattaa käydä samoissa soluissa monta kertaa uudelleen. Se pitää kirjaa vierailluista soluista, mutta vain siksi, että se tietää pitääkö solujen väliltä rikkoa seinä vai ei. Seuraavaa siirtoa harkitessaan algoritmi ei anna painoarvoa sille, onko solu vierailtu vai ei. Aldous-Broder-algoritmin aikavaativuus on O(|V| + |E|), missä |V| ja |E| ovat graafin solmujen ja kaarten lukumäärä. Suurten verkkojen käsittelyssä se voi olla hyvinkin hidas.


1.	Valitse satunnainen ruutu ja merkitse se vierailluksi
2.	Niin pitkään kuin ruudukossa on vierailemattomia ruutuja:
   * Valitse satunnainen naapuriruutu
   * Jos tuossa ruudussa ei ole vielä käyty:
      + Poista seinä nykyisen ruudun ja naapurin välistä
      + Merkitse naapuriruutu vierailluksi
   * Siirry naapuriruutuun ja merkitse se nykyiseksi ruuduksi

Tässä sovelluksessa toteutus on samanlainen kuin iteroivassa DFS:ssä. Mallinnan labyrintin kaksiulotteisena taulukkona. Taulukon jokainen solu sisältää nelipaikkaisen listan, jonka jokainen alkio on joko 1 tai 0. 1 tarkoittaa seinää, 0 ovea. Ensimmäinen alkio viittaan solun vasemmanpuoleiseen seinään, toinen kattoon, kolmas oikeanpuoleiseen seinään ja neljäs lattiaan. Kun seinä poistetaan, muutokset tehdään aina niihin kahteen soluun, joiden välillä seinä on. Erona on, että Aldous-Broder seuraavaa siirtoa valitessa se ei priorisoi vierailemattomia soluja vaan saattaa käydä samoissa paikoissa monta kertaa.

### Lähteet

![Wikipedia: Maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

![Wikipedia: DFS](https://en.wikipedia.org/wiki/Depth-first_search)

![Wikipedia: Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

![John Stilley: Maze-generating algorithms](https://github.com/john-science/mazelib/blob/main/docs/MAZE_GEN_ALGOS.md)

![Survey Paper on Maze Generation Algorithms for Puzzle Solving Games](https://anoopmusale.github.io/resume/paper.pdf)

![Analysis of Maze Generating Algorithms](http://ipsitransactions.org/journals/papers/tir/2019jan/p5.pdf)




