# Using the sqlite3 built-in package for managing SQLite databases, create a database named app.db.
# Then create a table named category with the given columns (with column constraints):
# category_id - INTEGER PRIMARY KEY
# category_name - TEXT NOT NULL
# Then insert the following records into the category table using the following SQL commands and commit the changes to the database:
# INSERT INTO category (category_name) VALUES ('technology');
# INSERT INTO category (category_name) VALUES ('e-commerce')
# INSERT INTO category (category_name) VALUES ('gaming')
# Create a query to the app.db database by selecting all rows from the category table and assigning them to the list named categories. In response, print the list of categories to the console.

import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

sql = '''
    CREATE TABLE IF NOT EXISTS category (
    category_id  INTEGER PRIMARY KEY,
    category_name  TEXT NOT NULL)
'''

cur.execute(sql)
cur.executescript('''
        INSERT INTO category (category_name) VALUES ('technology');
        INSERT INTO category (category_name) VALUES ('e-commerce');
        INSERT INTO category (category_name) VALUES ('gaming')
''')
conn.commit()

cur.execute('''SELECT * from category ''')
categories = cur.fetchall()
print(categories)