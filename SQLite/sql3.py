# Using the above code in the app.db database, create a customer table. Then insert the following records into the customer table using the executescript() method:
# ('John', 'Smith', 'john.smith@esmartdata.org')
# ('Joe', 'Doe', 'joe.doe@esmartdata.org')
# ('Mike', 'Smith', 'mike.smith@esmartdata.org')
# Commit the changes and close the database connection.


import sqlite3


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
 
conn.commit()
conn.close()