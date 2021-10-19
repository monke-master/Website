CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);