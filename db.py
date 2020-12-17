# Creating tables for database

import sqlite3

#Open database
conn = sqlite3.connect('restaruants.db')

cur = conn.cursor()

sql_file = open("db_script.sql")

sql_as_string = sql_file.read()

cur.executescript(sql_as_string)

# testing for table creation
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())

conn.close()