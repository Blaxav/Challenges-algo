from time import time
import unittest
from collections import defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def sortEncryptedName(ecryptedName: str):
    counter = defaultdict(int)
    for char in ecryptedName:
        counter[char] -= 1
    sort = sorted(counter.items(), key=lambda x: (x[1],x[0]))
    sortedString = ''
    for it in range(5):
        sortedString += sort[it][0]
    return sortedString
            
def part1(scheme: list):
    idSum = 0
    for elem in scheme:
        ecryptedName, number, check = elem[:-11].replace('-', ''), int(elem[-10:-7]), elem[-6:-1]
        idSum += (sortEncryptedName(ecryptedName) == check) * number
    return idSum

def rotateLetters(ecryptedName: str, number: int):
    newString = ''
    number = number % 26
    for elem in ecryptedName:
        if elem.islower():
            newString += chr(ord(elem) + number - (ord(elem)+number > 122)*26)
        else:
            newString += ' '
    return newString


def part2(scheme: list):
    for elem in scheme:
        ecryptedName, number, check = elem[:-11], int(elem[-10:-7]), elem[-6:-1]
        if 'north' in rotateLetters(ecryptedName, number):
            return number

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

