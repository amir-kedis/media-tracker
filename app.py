from flask import Flask, render_template, session

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("TODO.html")