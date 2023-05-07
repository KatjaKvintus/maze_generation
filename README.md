# Sokkeloja luovien algoritmien tutkiminen
_Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit, Helsingin yliopisto_

Sovellus generoi, visualisoi ja vertailee kolmen eri satunnaisia labyrinttejä generoivien algoritmin (satunnainen syvyyshaku, Kruskalin algoritmi ja Aldous-Broderin algoritmi) tuloksia. 


### Sovelluksen tilanne 7.5.2023

Vaikka kaikenlaista pientä hiottavaa riittää, pylint ei ole täysin tyytyväinen ja dokumentaatiossakin on vielä kirjoitettavaa, sovellus alkaa olla melko valmis.

Vertaisarviointia varten lyhyt ohje [täällä](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/testausohjeita.md).


### Viikkoraportit

![Viikkoraportti 1](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Viikkoraportti_1.md)

![Viikkoraportti 2](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Viikkoraportti_2.md)

![Viikkoraportti 3](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Viikkoraportti_3.md)

![Viikkoraportti 4](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Viikkoraportti_4.md)

![Viikkoraportti 5](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Viikkoraportti_5.md)

![Viikkoraportti 6](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Viikkoraportti_6.md)

![Viikkoraportti 7](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/Viikkoraportti_7.md)


### Dokumentaatio

![Määrittelydokumentti](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/M%C3%A4%C3%A4rittelydokumentti.md)

![Tuntikirjanpito](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/tuntikirjanpito.md)

![Testausdokumentti](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/testausdokumentti.md) - kesken

![Toteutusdokumentti](https://github.com/KatjaKvintus/maze_generation/blob/main/dokumentaatio/toteutusdokumentti.md) - kesken


### Tiedossa olevat virheet ja ongelmat

- Testi test_drawing_function_returns_file_that_is_not_empty() antaa satunnaisesti hämärän virheilmoituksen Aldous-Broderin algoritmin tuottamasta labyrinttikuvasta
- Sovellus pitää buutata jokaisen ajon välissä, muuten se kaatuu turtle-moduulin käynnistyessä
