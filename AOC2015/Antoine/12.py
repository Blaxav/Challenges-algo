from time import time
import unittest
import json
a = time()

count = 0

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.json", "r") as f:
        return json.load(f)

def part1(scheme):
    global count
    if isinstance(scheme, dict):
        scheme = list(scheme.values())
    for elem in scheme:
        if isinstance(elem, int):
            count += elem
        if isinstance(elem, list):
            part1(elem)
        if isinstance(elem, dict):
            part1(elem)


def part2(scheme: list):
    global count
    if isinstance(scheme, dict):
        if 'red' not in scheme.values():
            scheme = list(scheme.values())
        else:
            scheme = []
    for elem in scheme:
        if isinstance(elem, int):
            count += elem
        if isinstance(elem, list):
            part2(elem)
        if isinstance(elem, dict):
            part2(elem)

class Tests(unittest.TestCase):

    def testP1(self):
        global count
        part1([1,2,3])
        self.assertEqual(count, 6)
        count = 0
        part1({"a":2,"b":4})
        self.assertEqual(count, 6)
        count = 0
        part1([[[3]]])
        self.assertEqual(count, 3)
        count = 0
        part1({"a":{"b":4},"c":-1})
        self.assertEqual(count, 3)
        count = 0
        part1({"a":[-1,1]})
        self.assertEqual(count, 0)
        count = 0
        part1([-1,{"a":1}])
        self.assertEqual(count, 0)
        count = 0
        part1([])
        self.assertEqual(count, 0)
        count = 0
        part1({})
        self.assertEqual(count, 0)

    def testP2(self):
        global count
        part2([1,2,3])
        self.assertEqual(count, 6)
        count = 0
        part2([1,{"c":"red","b":2},3])
        self.assertEqual(count, 4)
        count = 0
        part2({"d":"red","e":[1,2,3,4],"f":5})
        self.assertEqual(count, 0)
        count = 0
        part2([1,"red",5])
        self.assertEqual(count, 6)
        


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    part1(scheme)
    print(f"Part 1: {count}")
    count = 0
    part2(scheme)
    print(f"Part 2: {count}")
    print(time()-a)

