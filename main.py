import flask
import os
from flask import *
import sqlite3, hashlib, os, requests
from numpy.lib.npyio import save
from flask import request, url_for, redirect, flash
from werkzeug.utils import secure_filename
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

app = flask.Flask(__name__)
app.config.from_envvar('APP_CONFIG')
app.secret_key = app.config['SECRET_KEY']

registration_required = app.config['REGISTER_USER_REQUIRED']

login = LoginManager()

DATABASE_USERS = app.config['DATABASE_USERS']
DATABASE_CHARACTER = app.config['DATABASE_CHARACTER']

# get database and connect
def get_db(database):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db

# get login details
def getLoginDetails():
    with sqlite3.connect(DATABASE_USERS) as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            username = ''
        else:
            loggedIn = True
            cur.execute("SELECT user_id, username FROM users WHERE email = ?", (session['email'],))
            user_id, username = cur.fetchone()
    conn.close()
    return (loggedIn, user_id, username)

# validate password
def is_valid(email, password):
    database = get_db(DATABASE_USERS)
    c = database.cursor()
    c.execute("SELECT EXISTS(SELECT hashed_password FROM users WHERE email=?)", (email,))
    data = c.fetchall()[0][0]
    if c.fetchall() == 0:
        return False
    c.execute("SELECT hashed_password FROM users WHERE email=?", ([email]))
    data = c.fetchall()[0][0]
    if check_password_hash(data, password):
        return True
    else:
        return False

# routes
@app.route("/")
def root():
    return redirect(url_for('index'))

@app.route("/index")
def index():

    LoggedIn = True

    if 'email' not in session:
        LoggedIn = False

    return render_template('index.html', LoggedIn=LoggedIn)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run()