from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().replace('[','-').replace(']','-') for i in f.readlines()]

def containsAbba(string: str):
    for it in range(1, len(string)-2):
        if string[it] == string[it+1] and string[it-1] != string[it] and string[it-1] == string[it+2]:
            return True
    return False

def part1(scheme: list):
    counter = 0
    for line in scheme:
        line = line.split('-')
        outsideBrackets, insideBrackets = False, True
        for num, string in enumerate(line):
            if num % 2 == 0 and not outsideBrackets:
                outsideBrackets = containsAbba(string)
            if num % 2 == 1 and insideBrackets:
                insideBrackets = not containsAbba(string)
        counter += insideBrackets * outsideBrackets
    return counter

def containsAbaAndBab(insideBrackets: str, outsideBrackets: str):
    for it in range(len(outsideBrackets)-2):
        if outsideBrackets[it] == outsideBrackets[it+2] and outsideBrackets[it+1] != outsideBrackets[it] and '-' not in outsideBrackets[it:it+3]:
            if outsideBrackets[it+1] + outsideBrackets[it] + outsideBrackets[it+1] in insideBrackets:
                return True
    return False

def part2(scheme: list):
    counter = 0
    for line in scheme:
        outsideBrackets, insideBrackets = '', ''
        line = line.split('-')
        for num, string in enumerate(line):
            if num % 2 == 0:
                outsideBrackets += string + '-'
            if num % 2 == 1:
                insideBrackets += string + '-'
        if containsAbaAndBab(insideBrackets, outsideBrackets):
            counter += 1
    return counter

class Tests(unittest.TestCase):

    def testP1(self):
        inputTest = 'abba'
        self.assertTrue(containsAbba(inputTest))
        inputTest = 'abbb'
        self.assertFalse(containsAbba(inputTest))
        inputTest = 'aaaa'
        self.assertFalse(containsAbba(inputTest))
        inputTest = ['abba-mnop-qrst']
        self.assertEqual(part1(inputTest), 1)
        inputTest = ['abcd-bddb-xyyx']
        self.assertEqual(part1(inputTest), 0)
        inputTest = 'aba-bab-xyz'
        self.assertTrue(containsAbaAndBab(inputTest))
        inputTest = 'xyx-xyx-xyx'
        self.assertFalse(containsAbaAndBab(inputTest))
        inputTest = 'aaa-kek-eke'
        self.assertTrue(containsAbaAndBab(inputTest))
        inputTest = 'zazbz-bzb-cdb'
        self.assertTrue(containsAbaAndBab(inputTest))

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

