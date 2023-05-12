# Toteutusdokumentti

### Ohjelman yleisrakenne

Sovellus on yksinkertainen webbisovellus. Käyttäjä antaa syötteenä haluamansa sokkelon koon (n) ja sovellus tuottaa  sokkelot (n x n) sovelluksen tarjoamilla algoritmeilla. Sovellus näyttää kunkin sokkelon kuvana ja tarjoaa siitä myös dataa: sokkelotyyppi, sen sisältämien umpikujien määrä ja sokkelon tuottamiseen kulunut aika. 

Sovelluksen toiminnallisuudet on kirjoitettu pythonilla ja ulkoasu HTML:llä. Labyrinttien visualisointi on tehty [Turtlella](https://docs.python.org/3/library/turtle.html).

Omiin kansioihinsa on sijoitettu testit, html-templaatit ja sovelluksen dokumentaatio. Muut tiedostot ovat sovelluksen juuressa. Yritykseni sijoittaa labyrinttejä generoivat tiedostot erikseen ja labyrinttien analysointiin keskittyvät erikseen johtivat epäselvään viittaushässäkkään. Ilmeisesti Flask on tässä vähän villi kortti, joka sotkee asioita ja normaalit tavat importata luokkia eivät toimi oikein. Pitkän debuggaamisen jälkeen luovitin ja jätin testejä lukuunottamatta kaikki.py-tiedostot juureen.


### Aikavaativuudet

Aikavaativuudet:

- Iteratiivinen syvyyshaku (iterative DFS): O(n)
- Kruskalin algoritmi: O(E log V)
- Aldous-Broderin algoritmi: on O(|V| + |E|), missä |V| on verkon solmujen ja |E| on kaarten lukumäärä


### Suorituskykyvertailu

Labyrinttien generoinnin näkökulmasta generointiaika ei ole merkittävin tekijä, mutta niitä on silti mielenkiintoista tarkastella. Loin kutakin labyrinttiä 10 kpl/koko jan laskin niille keskiarvot. Alle 25x25 -kokoisissa labyrinteissä erot eivät ole ihmisaisten erotettavissa, mutta suurimmassa testatussa koossa (200x200 eli 40 000 ruutua) erot olivat merkittäviä. Alla generointiaikakaaviot ensin per algoritmi, sitten kaikki samassa ja lopuksi ajat taulukossa.

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/iteratiivinen%20syvyyshaku%20DFS_generointiaika.png" width="50%" height="50%">

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/kruskal_generointiajat.png" width="50%" height="50%">

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/aldous-broder_%20generointiajat.png" width="50%" height="50%">

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/generointiajat_kaavio.png" width="70%" height="70%">

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/generointiajat_taulukko.png" width="40%" height="40%">



### Tiedossa olevat virheet ja ongelmat

- Modulien importit eivät välttämättä toimi oikein muilla koneilla. Tyyli "from maze_generation import kruskal" ei ole oikea tapa importata, mutta jostakin syystä se on ainoa joka toimii. Testiluokkien importit saattaa siis joutua korjaamaan ennen kuin sovellusta voi testata. Epäilen, että ongelma on Flask-peräinen.
- Testi test_drawing_function_returns_file_that_is_not_empty() antaa satunnaisesti hämärän virheilmoituksen Aldous-Broderin algoritmin tuottamasta labyrinttikuvasta
- Sovellus pitää buutata jokaisen generointiajon välissä, muuten se kaatuu turtle-moduulin käynnistyessä
- Kruskalin algoritmilla varsinkin isommat labyrintit ovat hitaita generoida ja algoritmi kaipaisikin tehostamista.
- Turtle-ikkuna jää auki labyrinttien luomisen jälkeen ja se jää näkyviin selainikkunan päälle. Koodirivi, jolla sain sen sulkeutumaan automaattisesti, aiheutti virheen unittestejä ajaessa, joten päätin, että tämä on ominaisuus, ei vika.


### Jatkokehitysideoita

- Sovellusta voisi laajentaa niin, että siinä olisi tarjolla useampia eri algoritmeja, ja käyttäjä voisi valita, minkä/mitkä hän haluaa testata
- Tällä hetkellä käyttäjältä pyydetään vain yksi numeerinen arvo ja labyrintit luodaan koossa n x n. Tätä voisi muuttaa siten, että käyttäjältä pyydetään erikseen sekä labyrintin toivottu leveys ja korkeus, jotta algoritmeilla voisi testata erimuotoisia labyrinttejä.
- Visualisoinnille jotain nopeampaa kuin turtle-moduuli
- Valmiin kuvan tuottamisen sijaan visualisoinnin voisi toteuttaa animaatiolla, joka olisi käyttäjälle informatiivisempi ja mielenkiintoisempi


### Lähteet

![Wikipedia: Maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

![John Stilley: Maze-generating algorithms](https://github.com/john-science/mazelib/blob/main/docs/MAZE_GEN_ALGOS.md)

![Survey Paper on Maze Generation Algorithms for Puzzle Solving Games](https://anoopmusale.github.io/resume/paper.pdf)

![Analysis of Maze Generating Algorithms](http://ipsitransactions.org/journals/papers/tir/2019jan/p5.pdf)
