# Using the sqlite3 built-in package for managing SQLite databases, a database named app.db was created. A table named customer was created in this database and two records were inserted:
# In the place designated for this, create a query that will extract all records from the customer table and print them to the console.

import sqlite3
 
 

conn = sqlite3.connect('app.db')
cur = conn.cursor()
 

sql = '''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)'''
cur.execute(sql)
 
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org')''')
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Doe', 'mike.doe@esmartdata.org')''')

cur.execute("""SELECT * FROM customer""")
result = cur.fetchall()

print(result)
 