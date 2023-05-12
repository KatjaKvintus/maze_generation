# Toteutusdokumentti

### Ohjelman yleisrakenne

Sovellus on yksinkertainen webbisovellus. Käyttäjä antaa syötteenä haluamansa sokkelon koon (n x n) ja sovellus tuottaa halutun kokoiset sokkelot sovelluksen tarjoamilla algoritmeilla. Sovellus näyttää sokkelon kuvana ja tarjoaa siitä myös dataa: sokkelotyyppi, sen sisältämien umpikujien määrä ja sokkelon tuottamiseen kulunut aika. 

Sovelluksen toiminnallisuudet on kirjoitettu pythonilla ja ulkoasu HTML:llä. Labyrinttien visualisointi on tehty [Turtlella](https://docs.python.org/3/library/turtle.html).

Omiin kansioihinsa on sijoitettu testit, html-templaatit ja sovelluksen dokumentaatio. Muut tiedostot ovat sovelluksen juuressa.


### Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)

(lisätään myöhemmin)


### Suorituskykyvertailu


<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/iteratiivinen%20syvyyshaku%20DFS_generointiaika%20ka.jpg" width="50%" height="50%">

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/kruskal_generointiaika%20ka.png" width="50%" height="50%">

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/aldous-broder_generointiaika%20ka.png" width="50%" height="50%">

<img src="https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Kuvat/ajoaikojen%20vertailu.jpg" width="50%" height="50%">



### Tiedossa olevat virheet ja ongelmat

- modulien importit eivät välttämätät toimi kaikilla koneilla. Tyyli "from maze_generation import kruskal" ei ole tyyliopillisesti oikein, mutta jostakin syystä se on ainoa joka toimii. Testiluokkien importit saattaa siis joutua korjaamaan ennen kuin sovellusta voi testata.
- Testi test_drawing_function_returns_file_that_is_not_empty() antaa satunnaisesti hämärän virheilmoituksen Aldous-Broderin algoritmin tuottamasta labyrinttikuvasta
- Sovellus pitää buutata jokaisen ajon välissä, muuten se kaatuu turtle-moduulin käynnistyessä
- Kruskalin algoritmilla varsinkin isommat labyrintit ovat hitaita generoida ja algoritmi kaipaisikin tehostamista.
- Turle-ikkuna jää auki labyrinttien luomisen jälkeen ja se jää näkyviin selainikkunan päälle. Koodirivi, jolla sain sen sulkeutumaan automaattisesti, aiheutti virheen unittestejä ajaessa, joten päätin, että tämä on ominaisuus, ei vika.


### Jatkokehitysideoita

- Sovellusta voisi laajentaa niin, että siinä olisi tarjolla useampia eri algoritmeja, ja käyttäjä voisi valita, minkä/mitkä hän haluaa testata
- Tällä hetkellä käyttäjältä pyydetään vain yksi numeerinen arvo la labyrintit luodaan koossa n x n. Tätä voisi muuttaa siten, että käyttäjältä pyydetään erikseen sekä labyrintin toivottu leveys ja korkeus, jotta algoritmeilla voisi testata erimuotoisia labyrinttejä.
- Visualisoinnille jotain nopeampaa kuin turtle-moduuli
- Valmiin kuvan tuottamisen sijaan visualisoinnin voisi toteuttaa animaatiolla, joka olisi käyttäjälle informatiivisempi ja mielenkiintoisempi


### Lähteet

![Wikipedia: Maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

![John Stilley: Maze-generating algorithms](https://github.com/john-science/mazelib/blob/main/docs/MAZE_GEN_ALGOS.md)

![Survey Paper on Maze Generation Algorithms for Puzzle Solving Games](https://anoopmusale.github.io/resume/paper.pdf)

![Analysis of Maze Generating Algorithms](http://ipsitransactions.org/journals/papers/tir/2019jan/p5.pdf)
