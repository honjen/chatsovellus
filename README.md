# chatsovellus
Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.


**Sovelluksen ominaisuudet**

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Silloin viestiin tulee merkintä "edit", jotta muut käyttäjät tietävät, että jotain on muokattu jälkikäteen.
- Käyttäjä voi poistaa oman ketjun tai viestin.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
- Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle

**Sovelluksen nykyinen tilanne**

Tähän palautukseen keskityin saamaan valmiiksi seuraavat toiminnot:
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. (puuttuu: Silloin viestiin tulee merkintä "edit", jotta muut käyttäjät tietävät, että jotain on muokattu jälkikäteen.)
- Käyttäjä voi poistaa oman ketjun tai viestin.
- Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
- Ylläpitäjä voi luoda salaisen alueen (puuttuu: ja määrittää, keillä käyttäjillä on pääsy alueelle)

Sovelluksesta puuttuvat vielä seuraavat toiminnot:
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.

TLDR:
Tässä vaiheessa on valmiina sovelluksen pohjarakenne, iso osa toiminnoista sekä ulkonäköä on hiottua ihan vähän. Aion myöhemmin lisätä puuttuvan toiminnon, parantaa sovelluksen tietoturvaa, sen käytettävyyttä sekä ulkonäköä.


**Käynnistysohjeet**

**HUOM!! TÄRKEÄÄ!!** 

**1. Sovelluksessa on tunnettu bugi, että jos on kirjautunut sisään kun poistaa tai tyhjentää tietokannan niin sovellus menee rikki. Joten jos haluat poistaa tai tyhjentää tietokannan käytön aikana, muista kirjautua ulos ensin!**

**2. schema1.sql poistaa taulut nimeltä messages, threads, categories, rights ja users ennen kuin tekee taulut uudelleen. Jos sinulla on samannimisiä tauluja ja et halua että niille tapahtuu mitään niin tee tällä sivulla olevan ohjeen mukaan: https://hy-tsoha.github.io/materiaali/vertaisarviointi/**

**3.Komento "psql < schema2.sql" luo tietokannan keskustelualueisiin joitain viestiketjuja ja viestejä, jos haluat tietokantaan valmista täytettä. Koodissa oletetaan, että sovelluksessa on ainakin yksi käyttäjä ennen kuin schema2.sql ajetaan, jotta se toimisi. Jos unohdat tehdä käyttäjän sovellukseen ennen schema2.sql ajoa niin aloita uudestaan kohdasta 3.**

**HUOM!! TÄRKEÄÄ!!**

1. Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
DATABASE_URL="tietokannan-paikallinen-osoite"
SECRET_KEY="salainen-avain"


2. Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt


3. Määritä tietokannan skeema komennolla:

$ psql < schema1.sql


4. käynnistä sovellus komennolla:

$ flask run


5. käytä sovellusta selaimessa

6. voit luoda käyttäjän ylläpitäjän oikeuksilla antamalla käyttäjä nimeksi "admin"


OPTIONAL: schema2.sql käyttö

7. mene sovellukseen, paina kirjaudu sisään ja tee sovellukseen käyttäjätunnus

8. lisää tietokantaan sisältöä komennolla:

$ psql < schema2.sql

9. päivitä sovelluksen nettisivu, jonka jälkeen voit lisätä viestiketjuihin viestejä