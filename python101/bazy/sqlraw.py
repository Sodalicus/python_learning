#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
example from python101 course
"""
def czytajdane():

    """Funkcja pobiera i wyswierla dane z bazy."""
    cur.execute(
        """
        SELECT uczen.id,imie,nazwisko,nazwa FROM uczen,klasa
        WHERE uczen.klasa_id=klasa.id
        """)
    uczniowie = cur.fetchall()
    for uczen in uczniowie:
        print(uczen['id'],uczen['imie'],uczen['nazwisko'],uczen['nazwa'])
    print()


def pobierz_dane(plikcsv):
    """
    Funkcja zwraca tuple tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """
    dane = []
    if os.path.isfile(plikcsv):
        with open(plikcsv, "r") as zawartosc:
            for linia in zawartosc:
                linia = linia.replace("\n", "")
                linia = linia.replace("\r", "")
                dane.append(tuple(linia.split(",")))
    else:
        print("Plik z danymi", plikcsv, "nie istnieje!")

    return tuple(dane)
def create_db():
    # utworzenie połączenia z bazą przechowywaną na dysku
    # lub w pamięci (':memory:')
    con = sqlite3.connect('test.db')

    #dostę do kolumn przez indeksy i przez nazwy
    con.row_factory = sqlite3.Row

    # utworzenie obiektu kursora
    cur = con.cursor()

    # tworzenie tabel
    cur.execute("DROP TABLE IF EXISTS klasa;")

    cur.execute("""
            CREATE TABLE IF NOT EXISTS klasa (
            id INTEGER PRIMARY KEY ASC,
            nazwa varchar(250) NOT NULL,
            profil varchar(250) DEFAULT ''
            )""")

    cur.executescript("""
            DROP TABLE IF EXISTS uczen;
            CREATE TABLE IF NOT EXISTS uczen (
                id INTEGER PRIMARY KEY ASC,
                imie varchar(250) NOT NULL,
                nazwisko varchar(250) NOT NULL,
                klasa_id INTEGER NOT NULL,
                FOREIGN KEY(klasa_id) REFERENCES klasa(id)
            )""")


    # wstawiamy jeden rekord danych
    cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);',('1A', 'matematyczny'))
    cur.execute('INSERT INTO klasa VALUES(NULL, ?, ?);',('1B', 'humanistyczny'))

    # wykonujemy zapytanie SQL, które pobierze id klasy "1A" z tabeli "klasa"
    cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1A',))
    klasa_id = cur.fetchone()[0]

    # tupla uczniowie zawiera tuple z danymi poszczególnych uczniów
    """
    uczniowie = (
            (None, 'Tomasz', 'Nowak', klasa_id),
            (None, 'Jan', 'Kos', klasa_id),
            (None, 'Piotr', 'Kowalski', klasa_id)
            )
    """
    uczniowie = pobierz_dane("uczniowie.csv")

    # wstawiamy wiele rekordów
    cur.executemany('INSERT INTO uczen VALUES(NULL,?, ?, ?)', uczniowie)

    # zatwierdzamy zmiany w bazie
    con.commit()

    # pobieranie danych z bazy


    # zmiana klasy ucznia o identyfikatorze 2
    cur.execute('SELECT id FROM klasa WHERE nazwa = ?', ('1B', ))
    klasa_id = cur.fetchone()[0]
    cur.execute('UPDATE uczen SET klasa_id=? WHERE id=?', (klasa_id, 2))

    # usunięcie ucznia o identyfikatorze 3
    cur.execute('DELETE FROM uczen WHERE id=?', (3,))
    cur.close()
    con.close()
