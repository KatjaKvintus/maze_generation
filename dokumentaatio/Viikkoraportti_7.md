# Viikkoraportti 7

### Mitä olen tehnyt tällä viikolla?

Tältä viikolta ei vaadittu enää raporttia, mutta kirjoitanpahan sen silti. Haluan kirjata muistiin tällä viikolla tehtyjä asioita.

Perjantain ohjausajan jälkeen totesin, että tämä vääntäminen recursive division -algorithmin kanssa loppuu nyt. Jos en saanut sitä kolmessa viikossa toimimaan, se ei hyvin todennäköisesti valmistu tämän kurssin deadlineen mennessä. Uusi ehdokas oli Aldous-Broderin algoritmi, joka ei ole nopein eikä tehokkain, mutta osoittautui helpommaksi ymmärtää kuin recursive division. Se on huoleton vaeltelija, joka hortoilee pitkin labyrinttiä ja aina kohdatessaan uuden solun rikkoo seinän sen ja saapumissolun väliltä. Se pitää kirjaa vierailluista soluista, mutta ei ota sitä huomioon kun arpoo, mihin suuntaan lähtisi seuraavaksi. Se saattaa siis käydä samoissa soluissa vaikka kuinka monta kertaa ja suoritys päättyy vasta, kun ihan joka solussa on käyty.

Olen myös koettanut tehostaa Kruskalin algoritmia, joka tuottaa labyrinttejä varsin hitaasti kavereihinsa verrattuna. Sain neuvon, että settejä yhdistäessä kannattaa aina tarkistaa settien koko ja yhdistää pienempi suurempaan eikä toisinpäin. Tämä ei valitettavasti parantanut keskinopeuksia.

### Miten ohjelma on edistynyt?

Sain kolmannen algoritmin kirjoitettua valmiiksi ja tein siihen samaan syssyyn testitkin. Se tuottaa samalla tavalla ilmaistun labyrintin kuin recursive backtracker, joten testit ovat hyvin samanlaisia. Loin myös tiedostot maze_tools.py ja maze_paths.py auttamaan labyrinttien analysoinnin ja testauksen kanssa, sekä vähentämään koodin toisteisuutta, sillä backtrackerin ja Aldous-Broderin samankaltaisuuden vuoksi ne voivat osin käyttää samoja apufunktioita.

Pylint antaa arvosanan /10.


### Mitä opin tällä viikolla?

Turtle on ongelmallinen testauksen kannalta.


### Mikä jäi epäselväksi tai tuottanut vaikeuksia? 

Tällä hetkellä ei oikein mikään.


### Ensi viikon työlista:

- Dokumentaation viimeistely
- Demoon valmistautuminen
- Release viikon päätteeksi
