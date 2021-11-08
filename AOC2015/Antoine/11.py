from time import time
from collections import defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def nextOrd(char: str):
    offset = defaultdict(lambda: 1)
    offset['z'], offset['h'], offset['k'], offset['n'] = -25, 2, 2, 2
    return chr(ord(char)+offset[char])

def nextString(string: str):
    string = string[::-1]
    for it, char in enumerate(string):
        string = string[:it] + nextOrd(char) + string[it+1:]
        if char != 'z':
            return string[::-1]
    return string[::-1]

def threeIncreasingStraightLetters(string: str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for it in range(len(alphabet)-2):
        if alphabet[it:it+3] in string:
            return True
    return False

def containTwoPairs(string: str):
    pairs = []
    for it in range(len(string)-1):
        if string[it] == string[it+1] and string[it] + string[it+1] not in pairs:
            pairs.append(string[it]+string[it+1])
    return len(pairs) >= 2


def part1(scheme: str):
    scheme = nextString(scheme)
    for it, char in enumerate(scheme):
        if char in ['i', 'l', 'o']:
            scheme = scheme[:it] + nextOrd(char) + 'a'*(len(scheme)-it-1)
            break
    while not (threeIncreasingStraightLetters(scheme) and containTwoPairs(scheme)):
        scheme = nextString(scheme)
    return scheme

class Tests(unittest.TestCase):

    def test(self):
        self.assertEqual(nextString('zzz'), 'aaa')
        self.assertEqual(nextString('azz'), 'baa')
        self.assertEqual(nextString('abc'), 'abd')
        self.assertEqual(nextString('ahz'), 'aja')
        self.assertEqual(nextString('azk'), 'azm')
        self.assertTrue(threeIncreasingStraightLetters('hijklmmn'))
        self.assertFalse(threeIncreasingStraightLetters('abbceffg'))
        self.assertTrue(containTwoPairs('abbceffg'))
        self.assertFalse(containTwoPairs('abbcegjk'))
        self.assertFalse(containTwoPairs('abbbcegjk'))
        self.assertFalse(containTwoPairs('abbcebbk'))
        self.assertEqual(part1('abcdefgh'), 'abcdffaa')
        self.assertEqual(part1('ghijklmn'), 'ghjaabcc')
        


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part1(p1)
    print(f"Part 2: {p2}")
    print(time()-a)

