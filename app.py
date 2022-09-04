# import libs
import os
from flask import Flask, render_template, session, request, redirect, jsonify
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash

# init main app
app = Flask(__name__)

# connect media database
db = SQL("sqlite:///media.db")

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