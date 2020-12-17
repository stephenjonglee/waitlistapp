import sqlite3, hashlib, os
from flask import *
from SQLfunctions import *

app = Flask(__name__)

app.secret_key = 'ft\x8a\xd9\x04\xd8\xed\xd2A\n\xd7\xc6cL\xf9\x89\xccr\xf5\x9c\xe6\xb6\x85\xc6'
DATABASE = 'restaruants.db'

def get_db(database):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db

def getLoginDetails():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
        else:
            loggedIn = True
            cur.execute("SELECT user_id FROM USER WHERE email = ?", (session['email'],))
            user_id = cur.fetchone()
    conn.close()
    return (loggedIn, user_id)

def is_valid(email, password):
    database = get_db(DATABASE)
    c = database.cursor()
    c.execute('SELECT * from USER WHERE email=?', [email])
    data = c.fetchone()
    if data is None:
        return False
    else:
        c.execute("SELECT pswd FROM USER WHERE email=?", [email])
        data = c.fetchone()[0]
        if check_password_hash(data, password):
            return True
        else:
            return False

# display root
@app.route('/', methods=['GET', 'POST'])
def root():
    return redirect(url_for("index"))

# display home page
@app.route('/index', methods=['GET', 'POST'])
def index():
    LoggedIn = True

    if 'email' not in session:
        LoggedIn = False
    
    return render_template("index.html", LoggedIn=LoggedIn)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        if is_valid(email, password):
            session['email'] = email
            return redirect(url_for('account'))
        else:
            error = 'Invalid email/password'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

# display register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["pass"]
        hashed = generate_password_hash(password, "sha512")

        database = get_db(DATABASE)
        c = database.cursor()
        
        c.execute('SELECT * from USER WHERE email=?', [email])
        data = c.fetchone()
        if data is None:
            c.execute("INSERT INTO USER (email, pswd) VALUES (?,?)", (email, hashed))
            database.commit()
            c.close()
            database.close()
            return redirect(url_for('login'))
        
        else:
            c.close()
            database.close()
            error = 'Email already exists'
            return render_template('register.html', error=error)
        
    else:
        return render_template('register.html')

# display restaurants
@app.route('/restaurant', methods=['GET', 'POST'])
def restaurant():
    # get all restaurants from database
    restuarants = getRestaurantList()
    return render_template("restaurant.html", restuarants=restuarants)

# display add restaurant form
@app.route('/add_rest', methods=['GET', 'POST'])
def add_rest():
    if request.method == 'POST':
        # get form inputs
        name = request.form['name']
        address = request.form['address']
        hours = request.form['hours']
        price = request.form['price']
        phone = request.form['phone']
        category = request.form['category']

        loggedIn, users_id = getLoginDetails()
        user_id = users_id[0]

        # store into database
        addRestaurant(user_id, name, address, phone, hours, price, category)
        return redirect(url_for('account'))
    else:    
        return render_template("add_rest.html")

# display reserve form
@app.route('/reserve', methods=['GET', 'POST'])
def reserve():
    if request.method == 'POST':
        # get parameter
        rest_id = request.args['rest_id']
        # get form inputs
        name = request.form['name']
        phone = request.form['phone']
        size = request.form['size']
        # insert into db
        addWaitlist(rest_id, name, size, phone)
        return redirect(url_for('waitlist', rest_id=rest_id))
    else:
        return render_template("reserve.html")

# display waitlist
@app.route('/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'POST':
        # get all restaurants from database
        rest_id = request.args['rest_id']
        return redirect(url_for('reserve', rest_id=rest_id))
    else:
        # get all restaurants from database
        rest_id = request.args['rest_id']
        name = getRestName(rest_id)[0]
        cust_list = getWaitlist(rest_id)
        return render_template("waitlist.html", cust_list=cust_list, name=name)

@app.route("/account", methods=['GET', 'POST'])
def account():
    return render_template("account.html")

@app.route("/myRest", methods=['GET', 'POST'])
def my_rest():
    # get list of user's restaurants
    loggedIn, users_id = getLoginDetails()
    user_id = users_id[0]
    myrestaurants = getMyRestaurants(user_id)

    return render_template("myRest.html", myrestaurants=myrestaurants)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # get form inputs
        name = request.form['name']
        address = request.form['address']
        hours = request.form['hours']
        price = request.form['price']
        phone = request.form['phone']
        category = request.form['category']

        # get param
        rest_id = request.args['rest_id']

        # update into database
        updateRestaurant(name, address, phone, hours, price, category, rest_id)
        return redirect(url_for('my_rest'))
    else:
        return render_template("edit.html")

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    rest_id = request.args['rest_id']
    deleteRestaurant(rest_id)
    return redirect(url_for('my_rest'))

@app.route("/myWait", methods=['GET', 'POST'])
def my_wait():
    if request.method == 'POST':
        # get all restaurants from database
        rest_id = request.args['rest_id']
        name = getRestName(rest_id)[0]
        deleteRecord()
        cust_list = getWaitlist(rest_id)
        return render_template("myWait.html", cust_list=cust_list, name=name)
    else:
        # get all restaurants from database
        rest_id = request.args['rest_id']
        name = getRestName(rest_id)[0]
        cust_list = getWaitlist(rest_id)
        return render_template("myWait.html", cust_list=cust_list, name=name)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)