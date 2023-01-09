# Using the sqlite3 built-in package for managing SQLite databases, a database named app.db was created. A table called customer was created in this database and several records were inserted.
# In the place designated for this, create a query that will determine the number of all records from the customer table and print it to the console.

import sqlite3


conn = sqlite3.connect('app.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)''')

cur.executescript('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org');

INSERT INTO customer (first_name, last_name, email)
VALUES ('Joe', 'Doe', 'joe.doe@esmartdata.org');

INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Smith', 'mike.smith@esmartdata.org');''')

# Enter your solution here
cur.execute('''SELECT COUNT(*) from customer''')
result = cur.fetchall()
print(result[0][0])

conn.commit()
conn.close()