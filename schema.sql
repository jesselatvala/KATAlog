CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
); 

CREATE TABLE katas (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    developer TEXT NOT NULL DEFAULT '',
    style TEXT NOT NULL DEFAULT '',
    techniques TEXT NOT NULL DEFAULT '',
    user_id INTEGER NOT NULL REFERENCES users(id)
);