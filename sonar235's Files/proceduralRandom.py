import random
def proceduralRandom(likelyhood = 50):
    i = 0
    rand = random.randint(1,100)
    while rand <= likelyhood:
        rand = random.randint(1,100)
        i += 1
    return i
if __name__ == '__main__':
    print proceduralRandom()
