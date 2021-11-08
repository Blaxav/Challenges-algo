from time import time
import unittest
import hashlib
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline()

def hexHash(doorId: str, number: str):
    toHash = doorId + number
    return hashlib.md5(toHash.encode()).hexdigest()
            
def part1(scheme: list):
    password = '********'
    number = 0
    while '*' in password:
        currentHash = hexHash(scheme, str(number))
        if currentHash.startswith('00000'):
            password = password.replace('*', currentHash[5], 1)
            print(password)
        number += 1
    return password

def part2(scheme: list):
    password = '********'
    number = 0
    while '*' in password:
        currentHash = hexHash(scheme, str(number))
        if currentHash.startswith('00000') and currentHash[5].isdigit() and int(currentHash[5]) in range(8) and password[int(currentHash[5])] == '*':
            password = password[:int(currentHash[5])] + currentHash[6] + password[int(currentHash[5])+1:]
            print(password)
        number += 1
    return password

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

