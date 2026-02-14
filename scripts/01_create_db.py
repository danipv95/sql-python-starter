import sqlite3
from pathlib import Path

DB_PATH = Path("data/sales.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Crear tablas
cur.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_items;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  customer_name TEXT NOT NULL,
  country TEXT NOT NULL
);

CREATE TABLE products (
  product_id INTEGER PRIMARY KEY,
  product_name TEXT NOT NULL,
  category TEXT NOT NULL,
  unit_price REAL NOT NULL
);

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY,
  order_date TEXT NOT NULL,
  customer_id INTEGER NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id INTEGER PRIMARY KEY,
  order_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  unit_price REAL NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

# Insertar datos
customers = [
  (1, "Agro Norte", "CR"),
  (2, "Comercial Pacífico", "CR"),
  (3, "Andes Trading", "PE"),
  (4, "Caribe Foods", "DO"),
]

products = [
  (1, "Maíz", "Granos", 18.50),
  (2, "Arroz", "Granos", 22.00),
  (3, "Aceite", "Abarrotes", 35.00),
  (4, "Atún", "Enlatados", 40.00),
]

orders = [
  (1001, "2025-12-15", 1),
  (1002, "2026-01-05", 2),
  (1003, "2026-01-20", 3),
  (1004, "2026-02-02", 1),
  (1005, "2026-02-08", 4),
]

order_items = [
  (1, 1001, 1, 10, 18.50),
  (2, 1001, 3,  2, 34.00),
  (3, 1002, 2,  5, 22.00),
  (4, 1002, 4,  3, 39.50),
  (5, 1003, 1, 20, 18.00),
  (6, 1003, 2, 10, 21.50),
  (7, 1004, 3,  4, 35.00),
  (8, 1005, 4,  6, 40.00),
]

cur.executemany("INSERT INTO customers VALUES (?,?,?)", customers)
cur.executemany("INSERT INTO products VALUES (?,?,?,?)", products)
cur.executemany("INSERT INTO orders VALUES (?,?,?)", orders)
cur.executemany("INSERT INTO order_items VALUES (?,?,?,?,?)", order_items)

conn.commit()
conn.close()

print(f"✅ Base de datos creada en: {DB_PATH}")
