#!/usr/bin/python
from flask import Flask, render_template

derp=Flask(__name__)

@derp.route("/")
def homepage():
    return render_template("homepage.html")

@derp.route("/senGen/")
def senGenPage():
    return render_template("senGenPage.html")

@derp.route("/markov/")
def markovPage():
    return render_template("markovPage.html")

@derp.route("/ceasarcipher/letter/encrypt")
def cipherPage():
    return render_template("cipherPage.html")


if __name__=="__main__":
    derp.debug=True
    derp.run(host="0.0.0.0",port=9999)
