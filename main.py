from flask import *
import sqlite3, hashlib, os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# display root
@app.route('/')
def root():
    return redirect(url_for("index"))

# display home page
@app.route('/index')
def index():
    return render_template("index.html")

# display login page
@app.route('/login')
def login():
    return render_template("login.html")

# display register page
@app.route('/register')
def register():
    return render_template("register.html")

# display restaurants
@app.route('/restaurant')
def restaurant():
    return render_template("index.html")

# display restaurants
@app.route('/add')
def add():
    return render_template("add_rest.html")



if __name__ == '__main__':
    app.run(debug=True)