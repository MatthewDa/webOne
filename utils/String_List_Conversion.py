def strToList(string):
    List=[]
    for i in string:
        List.append(i)
    return List

def listToStr(List):
    string=""
    for i in List:
        string=string+i
    return string

if __name__ == "__main__":
    x="Hello world!"
    print x
    print""
    y=strToList(x)
    print y
    print""
    z=listToStr(y)
    print z
    print "\n"
    print x
    print y
    print z
