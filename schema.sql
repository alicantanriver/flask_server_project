DROP TABLE IF EXISTS list;
DROP TABLE IF EXISTS item;

CREATE TABLE list (
id INTEGER PRIMARY KEY,
name TEXT UNIQUE NOT NULL,
orderNo INTEGER NOT NULL 
);

CREATE TABLE item (
  id INTEGER PRIMARY KEY,
  list_id INTEGER NOT NULL,
  name TEXT UNIQUE NOT NULL,
  orderNo INTEGER NOT NULL, 
  FOREIGN KEY (list_id) REFERENCES list (id)
);