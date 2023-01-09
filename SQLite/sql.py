# Using the sqlite3 built-in package for managing SQLite databases, create a database named app.db.
# The following SQL snippet creates a table named customer with the columns customer_id, first_name, last_name, and email.
# CREATE TABLE IF NOT EXISTS customer (
#     customer_id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     email TEXT
# )
# Using the above code in the app.db database, create a customer table. Then insert the following record into the customer table:
# ('John', 'Smith', 'john.smith@esmartdata.org')

import sqlite3


# Create connection here
conn = sqlite3.connect("app.db")

# Create table
sql = '''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)'''

cur = conn.cursor()
cur.execute(sql)

sql_insert = """
            INSERT INTO customer (first_name, last_name, email) VALUES
            ('John', 'Smith', 'john.smith@esmartdata.org')
"""
cur.execute(sql_insert)
conn.commit()
cur.close()
conn.close()