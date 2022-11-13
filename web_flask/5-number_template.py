#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB"

@app.route("/hbnb", strict_slashes=False)
def hdnd():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return f"C {escape(text.replace('_', ' '))}"

@app.route("/python", defaults={"text":"is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def python_is_cool(text):
    return f"Python {escape(text.replace('_', ' '))}"

@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    if type(n) == int:
        return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def is_a_number_template(n):
    if type(n) == int:
        return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
