from time import time
from itertools import groupby
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()

def process(num):
    count = 1
    curnum = ''
    result = ''
    for n in num+' ':
        if curnum == n:
            count += 1
        elif curnum == '':
            curnum = n
        else:
            result += str(count) + curnum
            count = 1
            curnum = n

    return result
       
def part1(scheme: str, it: int):
    newScheme = scheme
    for i in range(it):
        newScheme = process(newScheme)
    return newScheme

class Tests(unittest.TestCase):

    def test(self):
        self.assertEqual(process('11'), '21')
        self.assertEqual(process('111221'), '312211')
    

if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme, 40)
    print(f"Part 1: {len(p1)}")
    p2 = part1(scheme, 50)
    print(f"Part 2: {len(p2)}")
    print(time()-a)

