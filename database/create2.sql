CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    provider_id INTEGER NOT NULL,
    FOREIGN KEY (provider_id) REFERENCES providers(id)
)