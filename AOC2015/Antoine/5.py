from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[0] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def threeVowels(string: str):
    comp = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        comp += string.count(vowel)
    return (comp >= 3)

def adjacentLetters(string: str):
    for it in range(len(string)-1):
        if string[it] == string[it+1]:
            return True
    return False

def naughtyStrings(string: str):
    naughtyStrings = ['ab', 'cd', 'pq', 'xy']
    for naughtyString in naughtyStrings:
        if naughtyString in string:
            return False
    return True


def part1():
    scheme = readFile()
    return len([a for a in scheme if threeVowels(a) and adjacentLetters(a) and naughtyStrings(a)])

def twoPairs(string: str):
    for it in range(len(string)-1):
        if string.count(string[it] + string[it+1]) >= 2:
            return True
    return False

def sandwich(string: str):
    for it in range(len(string)-2):
        if string[it] == string[it+2]:
            return True
    return False

def part2():
    scheme = readFile()
    return len([a for a in scheme if twoPairs(a) and sandwich(a)])

class Tests(unittest.TestCase):

    def testTwoPairs(self):
        self.assertTrue(twoPairs('qjhvhtzxzqqjkmpb'))
        self.assertTrue(twoPairs('xxyxx'))
        self.assertTrue(twoPairs('uurcxstgmygtbstg'))
        self.assertFalse(twoPairs('ieodomkazucvgmuy'))

    def testSandwich(self):
        self.assertTrue(sandwich('qjhvhtzxzqqjkmpb'))
        self.assertTrue(sandwich('xxyxx'))
        self.assertFalse(sandwich('uurcxstgmygtbstg'))
        self.assertTrue(sandwich('ieodomkazucvgmuy'))

if __name__ == "__main__":
    p1 = part1()
    print(f"Part 1: {p1}")
    # unittest.main()
    p2 = part2()
    print(f"Part 2: {p2}")
    print(time()-a)

