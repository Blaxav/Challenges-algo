from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def jie(num: int, comp: int, offset: int):
    if num % 2 == 0:
        return comp+offset
    else:
        return comp+1

def jio(num: int, comp: int, offset: int):
    if num == 1:
        return comp+offset
    else:
        return comp+1

def part1(scheme: list):
    limit = len(scheme)
    comp = 0
    res = {'a': 0, 'b': 0}
    while comp < limit:
        instruction = scheme[comp].split()
        if instruction[0] == 'hlf':
            res[instruction[1]] /= 2
            comp += 1
        elif instruction[0] == 'tpl':
            res[instruction[1]] *= 3
            comp += 1
        elif instruction[0] == 'inc':
            res[instruction[1]] += 1
            comp += 1
        elif instruction[0] == 'jmp':
            comp += int(instruction[1])
        elif instruction[0] == 'jie':
            comp = jie(res[instruction[1][0]], comp, int(instruction[2]))
        elif instruction[0] == 'jio':
            comp = jio(res[instruction[1][0]], comp, int(instruction[2]))
    return res['b']

def part2(scheme: list):
    limit = len(scheme)
    comp = 0
    res = {'a': 1, 'b': 0}
    while comp < limit:
        instruction = scheme[comp].split()
        if instruction[0] == 'hlf':
            res[instruction[1]] /= 2
            comp += 1
        elif instruction[0] == 'tpl':
            res[instruction[1]] *= 3
            comp += 1
        elif instruction[0] == 'inc':
            res[instruction[1]] += 1
            comp += 1
        elif instruction[0] == 'jmp':
            comp += int(instruction[1])
        elif instruction[0] == 'jie':
            comp = jie(res[instruction[1][0]], comp, int(instruction[2]))
        elif instruction[0] == 'jio':
            comp = jio(res[instruction[1][0]], comp, int(instruction[2]))
    return res['b']

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

