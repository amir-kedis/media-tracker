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
import datetime

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
    
    # get user id
    user_id = session["user_id"]

    # select user media 
    planToWatch = db.execute("SELECT * FROM media WHERE user_id = ? AND status = 'planToWatch'", user_id)
    watched = db.execute("SELECT * FROM media WHERE user_id = ? AND status = 'watched'", user_id)
    watching = db.execute("SELECT * FROM media WHERE user_id = ? AND status = 'watching'", user_id)

    # send data to front-end and render the home page
    return render_template("index.html", planToWatch=planToWatch, watched=watched, watching=watching)


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
    """ ADD MEDIA """

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET": 
        return render_template("add_media.html")

    # User reached route via POST (as by submitting a form via POST)
    else:
        user_id = session["user_id"]
        mediaName = request.form.get("media_name")
        status = request.form.get("status")
        type = request.form.get("type")
        img = request.form.get("img")

        # ensure user provide Media Name
        if not mediaName:
            return apology("Must Provide Media Name")

        # ensure user provide Media Name
        if not status:
            return apology("Must Provide Status")

        # ensure user provide Media Name
        if not type:
            return apology("Must Provide Type")

        # if user provided no media put it to NULL
        if not img:
            return apology("Must Provide Image")

        mediaName = mediaName.strip().lower()

        media_db = db.execute("SELECT name FROM media WHERE user_id = ? AND name = ?", user_id, mediaName)

        if len(media_db) != 0:
            return apology("media already exists")

        # get date
        date = date = datetime.datetime.now()

        # insert into database
        db.execute("INSERT INTO media (user_id, name, type, status, img, date) VALUES (?,?,?,?,?,?)",
                        user_id,
                        mediaName,
                        type,
                        status,
                        img,
                        date)

        # redirect the user to add again
        return redirect("/add_media")

        
# edit_list route
@app.route("/edit_list", methods=["GET", "POST"])
@login_required
def editList():
    
    # if user gets by click edit_list link
    if request.method == "GET":

        # get user id
        user_id = session["user_id"]

        # get user list 
        user_list = db.execute("SELECT * FROM media WHERE user_id = ?", user_id)
        
        # send the list to front-end
        return render_template("edit_list.html", medias=user_list)

# edit_list_item route
@app.route("/edit_list_item", methods=["GET", "POST"])
@login_required
def edit_list_item():
    
    # if user gets by click edit form
    if request.method == "GET":

        # get user id
        user_id = session["user_id"]

        # get media id
        media_id = request.args.get("id")

        # check that we got media id
        if not media_id:
            return apology("Something went wrong!")

        # Media .info
        media_info = db.execute("SELECT * FROM media WHERE id = ?", media_id)[0]

        print(media_info)
        
        # send the list to front-end
        return render_template("edit_list_item.html", media=media_info)

    # edit media accept
    else:

        # get user id
        user_id = session["user_id"]

        # get media id
        media_id = request.form.get("id")

        # media_info
        media_name = request.form.get("media_name")
        media_status = request.form.get("status")
        media_type = request.form.get("type")
        media_img = request.form.get("img")

        # ensure all fields are given
        if not media_name or not media_status or not media_type or not media_img:
            return apology("All Felids must be given")

        # update the database
        db.execute("UPDATE media SET name = ?, type = ?, status = ?, img = ? WHERE id = ?", media_name, media_type, media_status, media_img, media_id)

        # redirect the user to edit list
        return redirect("edit_list")

# delete media item route
@app.route("/delete_item", methods=["GET", "POST"])
@login_required
def deleteMedia():
    # get user id
    user_id = session["user_id"]

    # get media id
    media_id = request.form.get("id")

    # check that we got media id
    if not media_id:
        return apology("Something went wrong!")

    # delete selected media from database
    db.execute("DELETE FROM media WHERE id = ?", media_id)

    # redirect the user to edit_list
    return redirect("/edit_list")

# watched route
@app.route("/watched")
@login_required
def watched():

    # get user id
    user_id = session["user_id"]

    # get plan to watch media
    watched = db.execute("SELECT * FROM media WHERE user_id = ? AND status = 'watched'", user_id)

    # send media to front end
    return render_template("watched.html", media=watched)

# watching route
@app.route("/watching")
@login_required
def watching():

    # get user id
    user_id = session["user_id"]

    # get watching media
    watching_rows = db.execute("SELECT * FROM media WHERE user_id = ? AND status = 'watching'", user_id)

    # send media to front end
    return render_template("watching.html", media=watching_rows)

# plan_to_watch route
@app.route("/plan_to_watch")
@login_required
def planToWatch():

    # get user id
    user_id = session["user_id"]

    # get plan to watch media
    planToWatch = db.execute("SELECT * FROM media WHERE user_id = ? AND status = 'planToWatch'", user_id)

    # send media to front end
    return render_template("planToWatch.html", media=planToWatch)


# auto start flask
if __name__ == "__main__":

    app.run(debug=True, port=9000)