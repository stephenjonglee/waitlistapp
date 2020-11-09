import sqlite3

#Open database
conn = sqlite3.connect('restaruants.db')

#Create table quiz
# Attributes: title, array of characters, array of questions, and array of options
conn.execute('''CREATE TABLE quiz
     (restId INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT,
     address TEXT,
     city TEXT,
     state TEXT,
     postal code TEXT,
     genre TEXT)
     ''')

conn.close()