from flask import Flask, render_template, session

app = Flask(__name__)

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

# login route
@app.route("/logout")
def logout():
    return render_template("TODO.html")

# auto start flask
if __name__ == "__main__":

    app.run(debug=True, port=9000)