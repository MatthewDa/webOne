import reader
import random
dic = {}
books = ["tom","grimm","wonderland","junglebook","oz"]
text = ""
keynum = 3

gutenReformat = True


def gutenreform(t): # USE string.find(HEADER) and string.find(LASTLINE)
    header = " ***"
    footer = "End of Project"
    return t[t.find(header) + len(header):t.find(footer)]

def customsplit(t,v,knum):
    result = []
    t = t.split(v)
    cword = ""
    for i in range(len(t)+1-knum):
        for j in range(knum):
            cword += t[i + j] + " "
        result.append(cword[:-1])
        cword = ""

    return result




def readText(f,knum):
    t = reader.read_file(f)
    if gutenReformat:
        t = gutenreform(t)
    #print t

    t = t.replace("\n"," ")
    t = t.replace("\t","")
    
    lstCut = customsplit(t," ",knum)
    lst = customsplit(t," ",1)
    
    for i in range(len(lstCut) - 1):
        if not(lstCut[i] in dic):
            dic[lstCut[i]] = []#If key doesn't exist, make a new one
            
        dic[lstCut[i]].append(lst[i + knum])

    return dic
        

def choose(a,text):
    text = text.split(" ")
    #print text
    return random.choice(a[text[-1]])


#######################YOU CAN MAKE IT MORE SIMPLE IF YOU MAKE THE ELEMENTS IN THE ARRAY HAVE n NUMBER OF WORDS AND REPEAT DIRECT ASSIGNMENT.####################

def generate(t,limit):
    cword = random.choice(dic.keys()) #Starting pair of words, that serves as the result

    for i in range(limit):
        prevword = ""
        if (keynum != 1):
            for j in range(keynum - 1):
                prevword += cword.split(" ")[-keynum + j + 1] + " "
                #Sets prevword to be evey word in cword except for the first one, so that a new element can be added to the key.
        cword = random.choice(dic[cword])#Sets cword to be a random word within its index.
        t += cword #Adds the word within the index
        #print "New cword pre ish: " + cword
        cword = prevword + cword #Makes a new key index.
        #print "New cword: " + cword
        t += " "
    
    return t   


def structurize(t):
    reverse = t[::-1]
    lastindex = len(t)- reverse.find(".")
    return t[t.find(".") + 1:lastindex]

def create(dir,book):
    text = ""
    if book in books:
        readText(dir + book,keynum)
    
    #for i in book:
    #    readText(i,keynum)
        text = generate(text,300)
        text = structurize(text)
    else:
        text = "-1"
    #reader.write_file("masterpiece.txt",text)
    #print "File saved"
    return text

if __name__ == '__main__':
    print create("../utils/data/books/","historyofafrica")
