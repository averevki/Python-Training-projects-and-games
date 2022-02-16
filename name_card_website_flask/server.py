#!/usr/bin/env python3

"""Name card website
Using template and flask
"""
__author__ = "Aleksandr Verevkin"
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def start():
    return render_template("index.html")


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
