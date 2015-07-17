#!/usr/bin/python
from flask import Flask, render_template
from utils.sengen import sengen

derp=Flask(__name__)

@derp.route("/")
def homepage():
    return render_template("homepage.html",title = 'Team Serpent - Home')

@derp.route("/senGen/")
def senGenPage():
    return render_template("senGenPage.html",title = 'Team Serpent - Sentence Generator',sentence = sengen())

@derp.route("/markov/")
def markovPage():
    return render_template("markovPage.html",title = 'Team Serpent - Markov Chains')

@derp.route("/ceasarcipher/letter/encrypt")
def cipherPage():
    return render_template("cipherPage.html",title = 'Team Serpent - Ceaser Cipher')


if __name__=="__main__":
    derp.debug=True
    derp.run(host="0.0.0.0",port=9999)
