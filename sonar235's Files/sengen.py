import random
import proceduralRandom
import smartDict

subjects = ['he','she','it','Yo Yo Ma','yo mama']
verbs = ['ran','threw up','laughed','exploded']
verbsH = ['pushed','smuggled','threw','helped','hacked']
nouns = ['boy','girl','puppy','cat']
adjectives = ['beautiful','happy','cute','electric','sad','hungry','amazing','incredible','unbelievable','astounding','awesome','huge','funny','bored','detered']
adverbs = ['swiftly','quickly','hastily','sadly','happily','vigourously','brutally']

articles = ['the','a']
vowels = ['a','e','i','o','u','y']

def oneOf(theList,minRange = 1):
    return theList[random.randint(minRange - 1,len(theList)-1)]


def adjs():
    repTimes = proceduralRandom.proceduralRandom()
    if repTimes == 0:
        return ''
    elif repTimes == 1:
        return oneOf(adjectives) + ' '
    else:
        i = 1
        retText = ''
        while i < repTimes:
            retText = retText + oneOf(adjectives)
            retText = retText + ', '
            i += 1
        retText = retText + oneOf(adjectives)
        retText = retText + ' '
        return retText

def sengen():
    genAdj = random.randint(0,1)
    genAdv = random.randint(0,1)
    Noun  = oneOf(nouns)
    Noun2 = oneOf(nouns)
    Adj = adjs()
    Art = oneOf(articles)
    ArtNoun = oneOf(articles)
    typeV = random.randint(1,4)
    if Adj != '' and Art == 'a':
        if vowels.count(Adj[0]) != 0:
            Art = 'an'
    if vowels.count(Noun2[0]) != 0 and ArtNoun == 'a':
        ArtNoun = 'an'
    if typeV == 1:
        string =  oneOf(subjects) + ' ' + oneOf(verbsH) + ' ' + oneOf(articles) + ' ' + Noun
    if typeV == 2:
        string =  Art + ' ' + Adj + Noun + ' ' + oneOf(verbsH) + ' ' + ArtNoun + ' ' + Noun2
    if typeV == 3:
        string = oneOf(subjects) + ' ' + oneOf(verbsH) + ' ' + Art + ' ' + Noun + ', ' + oneOf(adverbs)
    if typeV == 4:
        string = Art + ' ' + Adj + Noun + ' ' + oneOf(verbs) + ' ' + oneOf(adverbs)
    string = capitalize(string)
    return string,typeV


def capitalize(text):
    firstLetter = text[:1]
    text = text[1:]
    firstLetter = firstLetter.title()
    text = firstLetter + text
    return text


