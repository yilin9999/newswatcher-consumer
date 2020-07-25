CREATE TABLE newsinfo (
    sk SERIAL PRIMARY KEY,
    publish_date TIMESTAMPTZ NOT NULL,
    title TEXT NOT NULL,
    media varchar(80),
    abstract TEXT,
    link TEXT NOT NULL UNIQUE,
    img TEXT
);