# import libs
import os
from flask import Flask, render_template, session, request, redirect, jsonify
from flask_session import Session
from cs50 import SQL
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# init main app
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# connect media database
db = SQL("sqlite:///media.db")

# error page
def apology(message, code=400):
    return render_template("error.html", code=code, msg=message)

# index route
@app.route("/")
def index():
    return render_template("TODO.html")

# register route
@app.route("/register")
def register():
    return render_template("TODO.html")

# login route
@app.route("/login")
def login():
    return render_template("TODO.html")

# logout route
@app.route("/logout")
def logout():
    return render_template("TODO.html")

# add_media route
@app.route("/add_media")
def addMedia():
    return render_template("TODO.html")

# edit_list route
@app.route("/edit_list")
def editList():
    return render_template("TODO.html")

# watched route
@app.route("/watched")
def watched():
    return render_template("TODO.html")

# watching route
@app.route("/watching")
def watching():
    return render_template("TODO.html")

# plan_to_watch route
@app.route("/plan_to_watch")
def planToWatch():
    return render_template("TODO.html")


# auto start flask
if __name__ == "__main__":

    app.run(debug=True, port=9000)