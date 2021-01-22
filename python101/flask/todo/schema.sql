/*
 * schema.sql
 */

-- todo/schem.sql

-- tabela z zadaniami
DROP TABLE IF EXISTS zadania;
CREATE TABLE zadania (
    id integer primary key autoincrement, 
    zadanie text not null,
    zrobione boolean not null,
    data_pub datetime not null
);

-- pierwsze dane
INSERT INTO zadania (id, zadanie, zrobione, data_pub)
VALUES (null, 'Wyrzucić śmieci', 0, datetime(current_timestamp));
INSERT INTO zadania (id, zadanie, zrobione, data_pub)
VALUES (null, 'Nakarmić psa', 0, datetime(current_timestamp));
