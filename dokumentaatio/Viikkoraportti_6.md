# Viikkoraportti 6

### Mitä olen tehnyt tällä viikolla?

Olen enimmäkseen debugannut omaa koodiani.


### Miten ohjelma on edistynyt?

Vähänlaisesti. Turtle käy yli 20 x 20 ruudukkujen kanssa tosi hitaaksi, joten kokeilin erilaisia tapoja tuottaa labyrintin visualisointi. En kuitenkaan saanut mitään toimimaan tarpeeksi hyvin. Turtlella siis mennään.

Kokeilin myös rukata apin käyttöliittymää niin, että se loisi yhden labyrintin kerrallaan ja näyttäisi tulokset samalla sivulla. Universumi tarjosi minulle kasvattavia kokemuksia ja tuki kykyäni sietää pettymyksiä (= en saanut sitä toimimaan). Koska käyttöliittymällä ei tällä kurssilla ole (pisteiden suhteen) isoa merkitystä ja aikaa ei enää ole paljoa, taidan tyytyä nykyiseen käyttöliittymään.

Suurin edistys on testien siirtäminen omaan alakansioon.

Pylint antaa arvosanan 8.06/10.


### Mitä opin tällä viikolla?

Ehjää ei kannata korjata.


### Mikä jäi epäselväksi tai tuottanut vaikeuksia? 

Rekursiivinen jakoalgoritmi tuottaa edelleen vaikeuksia. Se tuottaa vaillinaisen labyrintin. En kerta kaikkiaan ymmärrä, onko vika rekursiiviselle funktiolle annettavista parametreistä  funktion lopussa vai ehdosta, jolla rekursio päättyy. Tiedosto recursive_division.py sisältää tällä hetkellä paljon debuggauksessa käyttämiäni välitulostuksia.


### Mitä teen seuraavaksi?

Korjaan rekursiivisen jakoalgoritmin ja kirjoitan sille testit ja visualisoinnin. Satunnaiselle syvyyshaulle kirjoittamani visualisointialgoritmin pitäisi itse asiassa toimia tämänkin kanssa, koska se tuottaa samanlaisen kaksiulotteisen taulukon, jonka jokainen solu sisältää neljän alkion listan.


### Ensi viikon työlista:

- rekursiivisen jakoalgoritmin korjaus
- Dokumentaation viimeistely
