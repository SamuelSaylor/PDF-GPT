CREATE TABLE products (
    id INTEGER,
    name TEXT,
    price REAL
);

INSERT INTO products VALUES (1, 'Pen', 1.5);
INSERT INTO products VALUES (2, 'Book', 5.0);
INSERT INTO products VALUES (3, 'Bag', 20.0);

SELECT * FROM products;

SELECT name FROM products WHERE price > 2;

-- filler queries
SELECT COUNT(*) FROM products;
SELECT AVG(price) FROM products;

SELECT id FROM products;
SELECT price FROM products;

SELECT name, price FROM products WHERE id = 1;