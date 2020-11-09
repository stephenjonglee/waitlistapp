import sqlite3

#Open database
conn = sqlite3.connect('waitlist.db')

#Create table quiz
# Attributes: name, size of party, phone number
conn.execute('''CREATE TABLE quiz
     (
     name TEXT,
     size INT,
     phone TEXT,
     FOREIGN KEY (restID) REFERENCES restaurants(restID)
     ''')

conn.close()