# For a record with category_id = 2, modify the category_name to 'online shop'. Then commit the replacements and display all rows of the category table as shown below.
# (1, 'technology')
# (2, 'online shop')
# (3, 'gaming')


import sqlite3
 
 
conn = sqlite3.connect('apps.db')
cur = conn.cursor()
 
cur.execute('''DROP TABLE IF EXISTS category''')
conn.commit()
 
cur.execute('''CREATE TABLE category (
    category_id   INTEGER,
    category_name TEXT    NOT NULL,
    PRIMARY KEY (category_id));''')
 
cur.execute(
    "INSERT INTO category (category_name) VALUES ('technology')"
)
cur.execute(
    "INSERT INTO category (category_name) VALUES ('e-commerce')"
)
cur.execute(
    "INSERT INTO category (category_name) VALUES ('gaming')"
)
 
conn.commit()


cur.execute('''UPDATE category
                SET category_name = 'online shop' 
                WHERE category_id = 2; ''')
conn.commit()
result = cur.execute('''SELECT * FROM category''').fetchall()
for i in result:
    print(i)

cur.close()
conn.close()