/*
 * schema.sql
 */

-- todo/schem.sql

-- tabela z uzytkownikami
DROP TABLE IF EXISTS uzytkownik;
CREATE TABLE uzytkownik (
    id integer primary key autoincrement,
    nick varchar(250) not null,
    magic integer not null
);
-- tabela z zadaniami
DROP TABLE IF EXISTS zadania;
CREATE TABLE zadania (
    id integer primary key autoincrement, 
    zadanie text not null,
    zrobione boolean not null,
    data_pub datetime not null,
    uzy_id integer not null,
    foreign key(uzy_id) references uzytkownik(id)

);

-- pierwsze dane
INSERT INTO zadania (id, zadanie, zrobione, data_pub, uzy_id)
VALUES (null, 'Wyrzucić śmieci', 0, datetime(current_timestamp), 1);
INSERT INTO zadania (id, zadanie, zrobione, data_pub, uzy_id)
VALUES (null, 'Opierdalać się', 0, datetime(current_timestamp), 1);

INSERT INTO zadania (id, zadanie, zrobione, data_pub, uzy_id)
VALUES (null, 'Nakarmić psa', 0, datetime(current_timestamp), 2);

INSERT INTO uzytkownik (id, nick, magic)
VALUES (NULL, 'soda', 1234);

INSERT INTO uzytkownik (id, nick, magic)
VALUES (NULL, 'marta', 4321);
