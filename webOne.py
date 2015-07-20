#!/usr/bin/python
from flask import Flask, render_template, request
from utils.sengen import sengen
from utils.CeasarCipher import ceasarCipher, ceasarDecipher
from utils.booksWrite import writeB
from utils.markov import create

derp=Flask(__name__)

@derp.route("/")
def homepage():
    return render_template("homepage.html",height = 400, title = 'Team Serpent - Home')

@derp.route("/senGen/")
def senGenPage():
    return render_template("senGenPage.html",height = 600, title = 'Team Serpent - Sentence Generator',sentence = sengen())

@derp.route("/markov/",methods = ['POST','GET'])
def markovPage():
    if request.method == 'GET':
        return render_template("markovPage.html",height = 400, title = 'Team Serpent - Markov Chains')
    if request.method == 'POST':
        results = request.form
        newList = results.getlist("books")
        if newList == []:
            return render_template("markovPage.html",text = "ERROR[7]:\n No checkboxes checked",height = 400, title = 'Team Serpent - Markov Chains')
        q = open('data/bookList','w')
        q.write('')
        q.close()
        q = open('data/bookList','a')
        for i in newList:
            q.write(i + '\n')
        q.close()
        writeB()
        return render_template("markovPage.html",text = create("data/","allBooks"),height = 400, title = 'Team Serpent - Markov Chains')
        

@derp.route("/ceasarcipher/", methods=["GET","POST"])
def cipherPage():
    if request.method=="POST":
        results=request.form
        if results["mode"]=="e":
            modeText="Encrypted"
            resultText=ceasarCipher(results["letter1"], results["letter2"], results["message"])
        if results["mode"]=="d":
            modeText="Decrypted"
            resultText=ceasarDecipher(results["letter1"], results["letter2"], results["message"])
        return render_template("cipherPage.html",height = 400, title = 'Team Serpent - Ceaser Cipher', mode=modeText, result=resultText)
    elif request.method=="GET":
        return render_template("cipherPage.html",height = 400, title = 'Team Serpent - Ceaser Cipher', mode="Encrypted/Decrypted", result="")

if __name__=="__main__":
    derp.debug=True
    derp.run(host="0.0.0.0",port=9999)
