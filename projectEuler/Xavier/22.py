import time
from utils import prime_numbers
from utils import add_one
from math import sqrt


ABC = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def val(letter):
    return ABC.index(letter)

def valW(word):
    res = 0
    for let in word[1:-1]:
        res += val(let)
    return res

if __name__ == '__main__' :
    start = time.time()

    nameFile = open("names.txt")
    names = sorted( nameFile.readlines()[0].split(",") )

    total = 0
    for i in range(len(names)):
        #print(names[i])
        id = i+1
        cval = valW(names[i]) 
        total += id * cval
        if id == 938:
            print(names[i], cval)

    print("Result: ", total)
    end = time.time()
    print()
    print("Time: %10.3fs" % (end-start))