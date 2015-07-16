def csvFileReadList(fileName):
    File=open(fileName)
    fileLines=File.read()
    File.close()
    fileLines=fileLines.split("\n")
    i=0
    x=len(fileLines)
    while i<x:
        fileLines[i]=fileLines[i].split(",")
        i+=1
    return fileLines


def appendDict(dictName,keyName,value):
    if keyName in dictName:
        dictName[keyName].append(value)
    else:
        newList=[value]
        dictName[keyName]=newList
    return dictName


def csvFileReadDict(fileName):
    File=open(fileName)
    fileLines=File.read()
    File.close()
    dictionary={}
    fileLines=fileLines.split("\n")
    i=0
    x=len(fileLines)
    while i<x:
        fileLines[i]=fileLines[i].split(",")
        key=fileLines[i].pop(0)
        y=len(fileLines[i])
        z=0
        while z<y:
            appendDict(dictionary,key,fileLines[i][z])
            z+=1
        i+=1
    return dictionary

def fileAppend(fileName, text):
    File=open(fileName, "a")
    File.write(str(text))
    File.close

def varStore(variable,varName,varType,fileName):
    fileAppend(fileName,varName+"\n")
    if varType=="dict":
        keyList=variable.keys()
        i=0
        x=len(keyList)
        while i<x:
            fileAppend(fileName,keyList[i]+"\n")
            i2=0
            x2=len(variable[keyList[i]])
            while i2<x2:
                fileAppend(fileName,variable[keyList[i]][i2]+" , ")
                i2+=1
            fileAppend(fileName,"\n")
            i+=1
        fileAppend(fileName,"END")
    elif varType=="list" or varType=="tuple":
        fileName
        i=0
        x=len(variable)
        while i<x:
            fileAppend(fileName,variable[i]+" , ")
            i+=1
    elif varType=="var":
        fileAppend(fileName,variable)
    fileAppend(fileName,"\n")

"""
def varRetrieve(variable,varName,varType,fileName):
    
"""



















