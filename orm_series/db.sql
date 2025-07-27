create table IF NOT EXISTS core_restaurant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(200) NOT NULL,
    website varchar(200),
    date_opened DATE,
    latitude REAL,
    longitude REAL
)
drop table core_restaurant