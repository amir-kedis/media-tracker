from flask import Flask, render_template, session

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("TODO.html")

# auto start flask
if __name__ == "__main__":

    app.run(debug=True, port=9000)