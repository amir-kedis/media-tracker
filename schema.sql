CREATE TABLE users (
    id integer PRIMARY KEY AUTOINCREMENT,
    username text,
    hash text
);

CREATE TABLE media (
    id integer PRIMARY KEY AUTOINCREMENT,
    user_id integer,
    name text,
    type text,
    status text,
    img blob,
    date datetime
);