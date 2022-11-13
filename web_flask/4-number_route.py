#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hdnd():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>")
def python_is_cool(text):
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    if type(n) == int:
        return "{} is a number".format(n)
    return 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
