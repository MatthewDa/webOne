dir = "data/"

if __name__=='__main__':
    dir = "../data/"

def writeB():
    q = open(dir + "allBooks",'w')
    q.write('')
    q.close()

    q = open(dir + 'bookList')
    s = q.read()
    q.close()

    books = s.split()


    i = 0
    while i <= len(books) - 1:
        q = open(dir + books[i])
        s = q.read()
        q.close()
        j = open(dir + "allBooks",'a')
        j.write(s)
        j.close()
        i += 1

