#!/usr/bin/python
from flask import Flask, render_template, request
from utils.sengen import sengen
from utils.CeasarCipher import ceasarCipher, ceasarDecipher

derp=Flask(__name__)

@derp.route("/")
def homepage():
    return render_template("homepage.html",height = 400, title = 'Team Serpent - Home')

@derp.route("/senGen/")
def senGenPage():
    return render_template("senGenPage.html",height = 600, title = 'Team Serpent - Sentence Generator',sentence = sengen())

@derp.route("/markov/")
def markovPage():
    return render_template("markovPage.html",height = 400, title = 'Team Serpent - Markov Chains')

@derp.route("/ceasarcipher/", methods=["GET","POST"])
def cipherPage():
    if request.method=="POST":
        results=request.form
        if results["mode"] != "" and results["letter1"] != "" and results["letter2"] != "" and results["message"] != "":
            if results["mode"]=="e":
                modeText="Encrypted"
                resultText=ceasarCipher(results["letter1"], results["letter2"], results["message"])
            if results["mode"]=="d":
                modeText="Decrypted"
                resultText=ceasarDecipher(results["letter1"], results["letter2"], results["message"])
            return render_template("cipherPage.html",height = 400, title = 'Team Serpent - Ceaser Cipher', mode=modeText, result=resultText)
        else:
            return render_template("cipherPage.html",height = 400, title = 'Team Serpent - Ceaser Cipher', mode="Error", result="You must fill out all parts of the form!")
    elif request.method=="GET":
        return render_template("cipherPage.html",height = 400, title = 'Team Serpent - Ceaser Cipher', mode="Encrypted/Decrypted", result="")

if __name__=="__main__":
    derp.debug=True
    derp.run(host="0.0.0.0",port=9999)
