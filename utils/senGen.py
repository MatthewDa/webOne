#lists of word choices
subjectNouns=["cat","dog","person","program","meme","orange","CSV file"]
presVerbs=["runs","jumps","falls","plays","forgets","walks","crashes"]
adverbs=["quickly","slowly","energetically","a lot"]
adjectives=["fat","tall","intelligent","cowardly","tired","fast","dank"]
articles=["the","a","",""]
places=["home","beach","office","internet"]
prepositions=["in","on","from","to","at","into","around"]
adjectives2=["large","small","shiny","dark","energized","bright","high-altitude","cold","hot","wet"]


#modules
import random
import String_List_Conversion
import fileRead

#reading from big fat nonsensical word list and adding to the original good lists
wordList=fileRead.csvFileReadDict("/data/wordList.csv")
subjectNouns=subjectNouns+wordList["nouns"]
presVerbs=presVerbs+wordList["verbs"]
adjectives=adjectives+wordList["adjectives"]
adverbs=adverbs+wordList["adverbs"]
"""
wordList=fileRead.csvFileReadList("wordList.csv")
i=0
x=len(wordList)
while i<x:
    List=wordList[i]
    if List[0]=="nouns":
        List.pop(0)
        subjectNouns=subjectNouns+List
    elif List[0]=="verbs":
        List.pop(0)
        presVerbs=presVerbs+List
    elif List[0]=="adjectives":
        List.pop(0)
        adjectives=adjectives+List
    elif List[0]=="adverbs":
        List.pop(0)
        adverbs=adverbs+List
    i+=1
"""

def randListElement(List):
    #chooses random element of list
    return List[random.randint(0,(len(List)-1))]

def multAdj1():
    #allows multiple adjectives
    x=random.randint(1,2)
    if x == 1:
        return ""
    else:
        return randListElement(adjectives)+" "+multAdj1()
    
def multAdj2():
    #allows multiple location description adjectives
    x=random.randint(1,2)
    if x == 1:
        return ""
    else:
        return randListElement(adjectives2)+" "+multAdj2()
    
def multAdv():
    #allows multiple adverbs
    x=random.randint(1,2)
    if x == 1:
        return ""
    else:
        return randListElement(adverbs)+" "+multAdv()

def nounPhrase():
    #creates noun phrase
    return randListElement(articles)+" "+multAdj1()+" "+randListElement(subjectNouns)

def verbPhrase():
    #creates verb phrase
    return randListElement(presVerbs)+" "+multAdv()

def locationPhrase():
    #1 in 3 chance of adding a location
    if random.randint(1,3)==2:
        phrase1=randListElement(prepositions)+" "+randListElement(articles)
        phrase2=multAdj2()+" "+randListElement(places)
        phrase1List=String_List_Conversion.strToList(phrase1)
        phrase2List=String_List_Conversion.strToList(phrase2)
        while phrase2List[0]==" ":
            phrase2List.remove(" ")
        if phrase1List[len(phrase1List)-1]=="a":
            if phrase2List[0]=="a" or phrase2List[0]=="e" or phrase2List[0]=="i" or phrase2List[0]=="o" or phrase2List[0]=="u":
                phrase1List.append("n")
        phrase1=String_List_Conversion.listToStr(phrase1List)
        phrase2=String_List_Conversion.listToStr(phrase2List)
        return phrase1+" "+phrase2
    else:
        return ""

def objectPhrase():
    #1 in 3 chance of adding a direct object
    if random.randint(1,3)==2:
        phrase1=randListElement(prepositions)+" "+randListElement(articles)
        phrase2=multAdj1()+" "+randListElement(subjectNouns)
        phrase1List=String_List_Conversion.strToList(phrase1)
        phrase2List=String_List_Conversion.strToList(phrase2)
        while phrase2List[0]==" ":
            phrase2List.remove(" ")
        if phrase1List[len(phrase1List)-1]=="a":
            if phrase2List[0]=="a" or phrase2List[0]=="e" or phrase2List[0]=="i" or phrase2List[0]=="o" or phrase2List[0]=="u":
                phrase1List.append("n")
        phrase1=String_List_Conversion.listToStr(phrase1List)
        phrase2=String_List_Conversion.listToStr(phrase2List)
        return phrase1+" "+phrase2
    else:
        return ""


def senGen ():
    #creates sentence draft
    sentence = nounPhrase()+" "+verbPhrase()+" "+objectPhrase()+" "+locationPhrase()
    #converts to list for editing
    senList=String_List_Conversion.strToList(sentence)
    #removes spaces at the start of the sentence, then capitalizes the first letter
    while senList[0]==" ":
        senList.remove(" ")
    x=ord(senList[0])
    if x>=ord("a") and x<=ord("z"):
        senList[0]=chr(x-(ord("a")-ord("A")))
    #removes double-spaces between words
    index=1
    for i in senList:
        if i==" " and senList[index]==" ":
            senList.pop(index)
        if index != len(senList)-1:
            index=index+1
    #double-check
    index=1
    for i in senList:
        if i==" " and senList[index]==" ":
            senList.pop(index)
        if index != len(senList)-1:
            index=index+1
    #converts "a" to "an" at start of sentence if first word begins with a vowel
    if senList[0]=="A" and senList[1]==" ":
        if senList[2]=="a" or senList[2]=="e" or senList[2]=="i" or senList[2]=="o" or senList[2]=="u":
            senList.insert(1,"n")
    #adds a period at the end of the sentence and removes extra spaces between the period and the last word
    if senList[len(senList)-1]==" ":
        senList[len(senList)-1]="."
    else:
        senList.append(".")
    #converts back to a string for final output
    sentence=String_List_Conversion.listToStr(senList)
    print sentence

if __name__=="__main__":
    #results!
    x=int(input("How many sentences do you want?   "))
    i=1
    while i<=x:
        senGen()
        i=i+1


















#jet fuel can't melt steel beams




















#SW@G MON3Y SW@G MON3Y SW@G LOT$ OV MON3Y-( ! /-\ |? /-\ |\|
