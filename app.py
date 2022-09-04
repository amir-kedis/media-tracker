# ----------------------------------
# ------: import libs and functions
# ----------------------------------

# import libs
from crypt import methods
import os
from flask import Flask, render_template, session, request, redirect, jsonify
from flask_session import Session
from cs50 import SQL
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

# ----------------------------------
# ------: configurations
# ----------------------------------

# init main app
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# disable cache
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# connect media database
db = SQL("sqlite:///media.db")

# ----------------------------------
# ------: Helper functions
# ----------------------------------

# error page
def apology(message, code=400):
    return render_template("error.html", code=code, msg=message)

def login_required(f):
    """
    Decorate routes to require login.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# ----------------------------------
# ------: Routes
# ----------------------------------

# index route
@app.route("/")
@login_required
def index():
    return render_template("TODO.html")

# register route
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a user"""

    # Forget any user_id
    session.clear()

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET": 
        return render_template("register.html")

    # User reached route via POST (as by submitting a form via POST)
    else:

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ensure user provided username
        if not username:
            return apology("must provide username", 403)
            
        # ensure user provided password
        if not password:
            return apology("must provide password", 403)

        # ensure user confirm password
        if not confirmation:
            return apology("must confirm password", 403)

        # ensure password and confirmation are the same
        if password != confirmation:
            return apology("password and confirmation must be the same", 403)

        # make a password hash
        hash = generate_password_hash(password)

        # insert user into database
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username already taken")

        # remember the user
        session["user_id"] = new_user

        # redirect user to home page
        return redirect("/")

# login route
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET": 
        return render_template("login.html")

    # User reached route via POST (as by submitting a form via POST)
    else:

        # ensure user provided username
        if not request.form.get("username"):
            return apology("must provide username", 403)
            
        # ensure user provided password
        if not request.form.get("password"):
            return apology("must provide password", 403)

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # remember which user logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect("/")

# logout route
@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# add_media route
@app.route("/add_media", methods=["GET", "POST"])
@login_required
def addMedia():
    return render_template("TODO.html")

# edit_list route
@app.route("/edit_list")
@login_required
def editList():
    return render_template("TODO.html")

# watched route
@app.route("/watched")
@login_required
def watched():
    return render_template("TODO.html")

# watching route
@app.route("/watching")
@login_required
def watching():
    return render_template("TODO.html")

# plan_to_watch route
@app.route("/plan_to_watch")
@login_required
def planToWatch():
    return render_template("TODO.html")


# auto start flask
if __name__ == "__main__":

    app.run(debug=True, port=9000)