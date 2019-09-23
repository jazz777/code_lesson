import sqlite3
connection = sqlite3.connect('nozomi.db')
cursor = connection.cursor()
#cursor.execute('''CREATE TABLE products (name text,price integer);''')
#cursor.execute('''INSERT INTO products (name,price) VALUES ('apple',198);''')
#cursor.execute('''INSERT INTO products (name,price) VALUES ('orange',100);''')
cursor.execute('''CREATE TABLE products (price integer);''')

i=1
while i < 10:
 cursor.execute('''INSERT INTO products (price) VALUES ('i');''')
 i = i + 1

connection.commit()
cursor.execute('''SELECT * FROM  products;''')
products = cursor.fetchall()
print(type(products))
print(products)

