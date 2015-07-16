__author__ = 'sonar235'

def multAssociation(dictName,key,value,omitMultiples = True):
    if isinstance(dictName,str):
       dictName = {}
    if key in dictName and (dictName[key].count(value) == 0 or not omitMultiples):
        dictName[key].append(value)
    if key not in dictName:
        newList = [value]
        dictName[key] = newList
    return dictName


def appendDict(mainDict,*dictList):
    print mainDict
    if isinstance(mainDict,str):
        mainDict = {}
    q = 0
    for i in dictList:
        mainDict[q] = i
        q += 1
    return mainDict

def renameDictItems(dictName,toReplace,name):
    dictName[name] = dictName[toReplace]
    dictName.pop(toReplace,None)
    return dictName

def renameDictItemsAll():
    pass



if __name__ == '__main__':
    Hi = {}
    multAssociation(Hi,'Yo','Blah')
    multAssociation(Hi,'Yo','Bloo')
    multAssociation(Hi,'Yo','Bldasdha')
    multAssociation(Hi,'Yoyo','crud')
    multAssociation(Hi,'Yo','Blah')
    multAssociation(Hi,'Yo','Blah',False)
    nonExistant = multAssociation({},'Oh no ','ERROR INCOMING')
    print Hi
    Yo = multAssociation('Yo','Hi','Yo')
    print Yo
    print nonExistant
    cupid = {}
    appendDict(cupid,Hi,Yo,nonExistant)
    print cupid
    renameDictItems(cupid,0,'Hi')
    print cupid
    Blah = {}
    
