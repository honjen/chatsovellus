# chatsovellus
Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.


## Sovelluksen ominaisuudet

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Silloin viestiin tulee merkintä "muokattu", jotta muut käyttäjät tietävät, että jotain on muokattu jälkikäteen.
- Käyttäjä voi poistaa oman ketjun tai viestin.
- Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
- Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle

## Ohjeet käyttöä varten  

~~~
HUOM! TÄRKEÄÄ!
Sovelluksessa on tunnettu bugi, että jos on kirjautunut sisään kun poistaa tai tyhjentää tietokannan niin sovellus menee rikki. Joten jos haluat poistaa tai tyhjentää tietokannan käytön aikana, muista kirjautua ulos ensin!
~~~
<br>

 1\. Sovellus ei ole testattavissa Fly.iossa. Siis kloonaa tämä repositorio omalle koneellesi komennolla:

```
git clone git@github.com:honjen/chatsovellus.git
```  
<br>

2\. Siirry repositorion juurikansioon ja luo sinne .env-tiedosto, jonka sisällön määrität seuraavanlaiseksi:
```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
<br>

3\. Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```
<br>

4\. Seuraavan kohdan tietokannan määritys schema1.sql:llä poistaa taulut nimeltä messages, threads, categories, rights ja users ennen kuin tekee taulut uudelleen. Jos sinulla on jo samannimisiä tietokantatauluja ja et halua että niille tapahtuu mitään niin voit luoda Postgresiin oman tietokannan seuraavasti:
<br>

avaa uusi terminaali ja anna komento, joka käynnistää PostgreSQL-palvelimen:
```
start-pg.sh
```

Mene takaisin aikasempaan terminaaliin ja anna komennot:
```
$ psql
user=# CREATE DATABASE <tietokannan-nimi>;
```
Voit nyt määrittää projektin tietokantaskeeman omasta tietokannastasi erilliseen tietokantaan komennoilla:
```
\q
$ psql -d <tietokannan-nimi> < schema1.sql
```
Määritä vielä tietokannan osoite projektille siten, että osoite päättyy luomasi tietokannan nimeen. Esimerkiksi, jos omalla sovelluksellasi osoite on muotoa postgresql:///user ja loit äsken uuden tietokannan nimeltä testi, tulisi uudeksi tietokannan osoitteeksi postgresql:///testi.
<br><br>

5\. Jos et tehnyt kohtaa 4 niin seuravaaksi määritä tietokannan skeema komennolla:
```
$ psql < schema1.sql
```
<br>

6\. Käynnistä sovellus komennolla:
```
$ flask run
```
<br>

7\. Käytä sovellusta selaimessa osoitteessa http://127.0.0.1:5000/.
<br>


8\. Voit luoda käyttäjän ylläpitäjän oikeuksilla antamalla käyttäjän nimeksi "admin".
<br>

---
<br>

**OPTIONAL: lisää tietokantaan sisältöä**
<br>

9\. Jos et ole jo tehnyt niin, mene sovellukseen, paina kirjaudu sisään ja tee sovellukseen käyttäjätunnus.
<br>

10\. Lisää tietokantaan sisältöä komennolla:
```
$ psql < schema2.sql
```
<br>

11\. Päivitä sovelluksen nettisivu niin voit käyttää sovellusta.