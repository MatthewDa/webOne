import random
import proceduralRandom
import smartDict
from reader import read_file as read


#The text directory
TEXT_DIR = '../data/'


subjects = read(TEXT_DIR + 'senSubjects').split(',')
verbs = read(TEXT_DIR + 'senVerbs').split(',')
verbsH = read(TEXT_DIR + 'senVerbsH').split(',')
nouns = read(TEXT_DIR + 'senNouns').split(',')
adjectives = read(TEXT_DIR + 'senAdjectives').split(',')
adverbs = read(TEXT_DIR + 'senAdverbs').split(',')

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
    if subjects[-1][-1:] == '\n':
        subjects[-1] = subjects[-1][:-1]
    if verbs[-1][-1:] == '\n':
        verbs[-1] = verbs[-1][:-1]
    if verbsH[-1][-1:] == '\n':
        verbsH[-1] = verbsH[-1][:-1]
    if nouns[-1][-1:] == '\n':
        nouns[-1] = nouns[-1][:-1]
    if adjectives[-1][-1:] == '\n':
        adjectives[-1] = adjectives[-1][:-1]
    if adverbs[-1][-1:] == '\n':
        adverbs[-1] = adverbs[-1][:-1]
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
    return string


def capitalize(text):
    firstLetter = text[:1]
    text = text[1:]
    firstLetter = firstLetter.title()
    text = firstLetter + text
    return text


