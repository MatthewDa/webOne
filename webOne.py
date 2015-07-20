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
    book_list = ["grimm","junglebook","oz","tom","wonderland"]
#length = len(book_list) #FOR HTML PURPOSES
    name = ["Grimm's Fairy Tales","The Jungle Book","The Wonderful Wizard of Oz","The Adventures of Tom","Alice's adventures in Wonderland"]
    checked = []
    for i in range(len(book_list)):
        checked += "0"

    if request.method == 'GET':
        return render_template("markovPage.html",height = 400, title = 'Team Serpent - Markov Chains')
    if request.method == 'POST':
        results = request.form
        newList = results.getlist("books")

        for i in range(len(newList)):
            for j in range(len(book_list)):
                if book_list[j] == newList[i]:
                    checked[j] == "1"

        if newList == []:
            return render_template("markovPage.html",text = "ERROR[7]:\n No checkboxes checked",height = 400, title = 'Team Serpent - Markov Chains',checked = checked,book_list = book_list,name = name)
        q = open('data/bookList','w')
        q.write('')
        q.close()
        q = open('data/bookList','a')
        for i in newList:
            q.write(i + '\n')
        q.close()
        writeB()
        return render_template("markovPage.html",text = create("data/","allBooks"),height = 400, title = 'Team Serpent - Markov Chains',checked = checked,book_list = book_list,name = name)


cipher_d_t = ""
cipher_d_l1 = ""#results["letter1"]
cipher_d_l2 = ""#results["letter2"]

@derp.route("/ceasarcipher/", methods=["GET","POST"])
def cipherPage():

    if request.method=="POST":
        results=request.form
        if results["mode"]=="e":
            modeText="Encrypted"
        elif results["mode"]=="d":
            modeText="Decrypted"
        resultText=ceasarDecipher(results["letter1"], results["letter2"], results["message"])
        cipher_d_l1 = results["letter1"]
        cipher_d_l2 = results["letter2"]
        cipher_d_t = results["message"]    
        
        return render_template("cipherPage.html",height = 400, title = 'Team Serpent - Ceaser Cipher', mode=modeText, result=resultText,l1 = cipher_d_l1,l2 = cipher_d_l2,text = cipher_d_t)
    elif request.method=="GET":
        return render_template("cipherPage.html",height = 400, title = 'Team Serpent - Ceaser Cipher', mode="Encrypted/Decrypted", result="",l1 = "",l2 = "",text = "")







if __name__=="__main__":
    derp.debug=True
    derp.run(host="0.0.0.0",port=9999)
