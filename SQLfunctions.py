# Database Functions

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = 'restaruants.db'

# list of add functions
def addWaitlist(restID, name, size, contact):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    sql = '''INSERT INTO WAITLIST (list_id, cust, size, contact) 
    VALUES (?,?,?,?)'''
    c.execute(sql, [restID, name, size, contact])
    conn.commit()
    c.close()
    conn.close()

def addRestaurant(manID, name, loc, phone, hour, price, category):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    sql = '''INSERT INTO RESTAURANT (manager_id, title, loc, contact, hour, price, category) 
    VALUES (?,?,?,?,?,?,?)'''
    c.execute(sql, [manID, name, loc, phone, hour, price, category])
    conn.commit()
    c.close()
    conn.close()

# update methods
def updateRestaurant(name, loc, phone, hour, price, category, rest_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    sql = '''UPDATE RESTAURANT SET title = ?, loc = ?, contact = ?, hour = ?, price = ?, category = ? WHERE rest_id = ?'''
    c.execute(sql, [name, loc, phone, hour, price, category, rest_id])
    conn.commit()
    c.close()
    conn.close()

# list of get methods
def getMyRestaurants(userID):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM RESTAURANT WHERE manager_id = ?', [userID])
    data = c.fetchall()
    c.close()
    conn.close()
    return data

def getRestaurantList():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM RESTAURANT')
    data = c.fetchall()
    c.close()
    conn.close()
    return data

def getWaitlist(restID):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM WAITLIST WHERE list_id = ?', [restID])
    data = c.fetchall()
    c.close()
    conn.close()
    return data

def getRestName(restID):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT title FROM RESTAURANT WHERE rest_id = ?', [restID])
    data = c.fetchone()
    c.close()
    conn.close()
    return data

# delete functions
def deleteRecord():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM WAITLIST')
    data = c.fetchone()
    if data is None:
        c.close()
        conn.close()
    else:
        c.execute('DELETE FROM WAITLIST WHERE cust_id = (SELECT min(cust_id) FROM WAITLIST)')
        conn.commit()
        c.close()
        conn.close()

def deleteRestaurant(rest_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE from RESTAURANT WHERE rest_id = ?', [rest_id])
    conn.commit()
    c.close()
    conn.close()