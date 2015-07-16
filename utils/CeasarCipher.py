#letter1 must come before letter2 in the alphabet at the moment
def ceasarCipher (letter1,letter2,code):
    a=ord(letter1)
    b=ord(letter2)
    rotated=b-a
    cipheredCode=""
    for i in code:
        if ord(i)>=ord("a") and ord(i)<=ord("z"):
            if ord(i)+rotated>ord("z"):
                x=rotated-(ord("z")-ord(i))
                cipheredCode=cipheredCode+chr((ord("a")-1)+x)
            else:
                cipheredCode=cipheredCode+chr(ord(i)+rotated)
        elif ord(i)>=ord("A") and ord(i)<=ord("Z"):
            if ord(i)+rotated>ord("Z"):
                x=rotated-(ord("Z")-ord(i))
                cipheredCode=cipheredCode+chr((ord("A")-1)+x)
            else:
                cipheredCode=cipheredCode+chr(ord(i)+rotated)
        else:
            cipheredCode=cipheredCode+i
    print cipheredCode
    return cipheredCode

def ceasarDecipher (letter1,letter2,code):
    a=ord(letter1)
    b=ord(letter2)
    rotated=b-a
    decipheredCode=""
    for i in code:
        if ord(i)>=ord("a") and ord(i)<=ord("z"):
            if ord(i)-rotated<ord("a"):
                x=rotated-(ord(i)-ord("a"))
                decipheredCode=decipheredCode+chr((ord("z")+1)-x)
            else:
                decipheredCode=decipheredCode+chr(ord(i)-rotated)
        elif ord(i)>=ord("A") and ord(i)<=ord("Z"):
            if ord(i)-rotated<ord("A"):
                x=rotated-(ord(i)-ord("A"))
                decipheredCode=decipheredCode+chr((ord("Z")+1)-x)
            else:
                decipheredCode=decipheredCode+chr(ord(i)-rotated)
        else:
            decipheredCode=decipheredCode+i
    print decipheredCode
    return decipheredCode
