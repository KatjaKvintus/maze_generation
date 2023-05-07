# Viikkoraportti 7

### Mitä olen tehnyt tällä viikolla?

Tältä viikolta ei vaadittu enää raporttia, mutta kirjoitanpahan sen silti. Haluan kirjata muistiin tällä viikolla tehtyjä asioita.

Perjantain ohjausajan jälkeen totesin, että tämä vääntäminen recursive division -algorithmin kanssa loppuu nyt. Jos en saanut sitä kolmessa viikossa toimimaan, se ei hyvin todennäköisesti valmistu tämän kurssin deadlineen mennessä. Uusi ehdokas oli Aldous-Broderin algoritmi, joka ei ole nopein eikä tehokkain, mutta osoittautui helpommaksi ymmärtää kuin recursive division. Se on huoleton vaeltelija, joka hortoilee pitkin labyrinttiä ja aina kohdatessaan uuden solun rikkoo seinän sen ja saapumissolun väliltä.

Loin myös kahdella jo toimivalla algoritmilla eri kokoisia labyrinttejä, 10 kutakin kokoa, ja otin ajat talteen tehokkuuskuvauksen tekoa varten. Kruskal on merkittävästi hitaampi kuin syvyyshaku, ja erot ovat niin isoja, että Kruskalissa on jotain vialla. Löysin jo yhden ongelman, jonka korjaaminen leikkasi suoritusajasta 2/3 pois: sen sijaan, että luuppi kävisi läpi kaikki verkon kaaret, se lopettaa läpikäynnin siinä vaiheessa kun käsiteltävän kaaren jomman kumman päässä olevan solmun setin koko on n^2 (nxn-kokoisen verkon solmujen määrä eli kaikki solmut kuuluvat samaan settiin). Silti 200x200-kokoisen labyrintin generointiin Kruskalin algortimillä menee keskimäärin 89 sekuntia, kun backtrackerilla vastaava syntyy 0,12 sekunnissa. Tätä pitää katsoa tarkemmin vielä ennen loppupalautusta ja tehostaa reippaasti.


### Miten ohjelma on edistynyt?

Vähänlaisesti. Turtle käy yli 20 x 20 ruudukkujen kanssa tosi hitaaksi, joten kokeilin erilaisia tapoja tuottaa labyrintin visualisointi. En kuitenkaan saanut mitään toimimaan tarpeeksi hyvin. Turtlella siis mennään.

Kokeilin myös rukata apin käyttöliittymää niin, että se loisi yhden labyrintin kerrallaan ja näyttäisi tulokset samalla sivulla. Universumi tarjosi minulle kasvattavia kokemuksia ja tuki kykyäni sietää pettymyksiä (= en saanut sitä toimimaan). Koska käyttöliittymällä ei tällä kurssilla ole (pisteiden suhteen) isoa merkitystä ja aikaa ei enää ole paljoa, taidan tyytyä nykyiseen käyttöliittymään.

Siirsin myös testit omaan alakansioonsa

Pylint antaa arvosanan 8.06/10.


### Mitä opin tällä viikolla?

Ehjää ei kannata korjata.


### Mikä jäi epäselväksi tai tuottanut vaikeuksia? 

Rekursiivinen jakoalgoritmi tuottaa edelleen vaikeuksia. Se tuottaa vaillinaisen labyrintin, jossa on usein umpinaisia huoneita. En kerta kaikkiaan ymmärrä, onko vika rekursiiviselle funktiolle annettavista parametreistä  funktion lopussa vai ehdosta, jolla rekursio päättyy. Tiedosto recursive_division.py sisältää tällä hetkellä paljon debuggauksessa käyttämiäni välitulostuksia.


### Mitä teen seuraavaksi?

Korjaan rekursiivisen jakoalgoritmin ja kirjoitan sille testit ja visualisoinnin. Satunnaiselle syvyyshaulle kirjoittamani visualisointialgoritmin pitäisi itse asiassa toimia tämänkin kanssa, koska se tuottaa samanlaisen kaksiulotteisen taulukon, jonka jokainen solu sisältää neljän alkion listan ykkösiä ja nollia merkkaamassa seiniä ja oviaukkoja.


### Ensi viikon työlista:

- rekursiivisen jakoalgoritmin korjaus
- Dokumentaation viimeistely
