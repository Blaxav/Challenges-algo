from time import time
import unittest
from copy import deepcopy
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return {counter:[i.strip()[:3], int(i.strip()[4:])] for counter, i in enumerate(f.readlines())}

            
def part1(scheme: dict):
    accumulator, seenStates, ind = 0, list(), 0
    while ind < len(scheme):
        if ind not in seenStates:
            seenStates.append(ind)
        else:
            return "!end", accumulator
        if scheme[ind][0] == 'nop':
            ind += 1
        elif scheme[ind][0] == 'acc':
            accumulator += scheme[ind][1]
            ind += 1
        else:
            ind += scheme[ind][1]
    
    return "end", accumulator


def part2(scheme: dict):
    gen = (k for k, v in scheme.items() if v[0] != 'acc' and v[1] != 0)
    for elem in gen:
        copyScheme = deepcopy(scheme)
        copyScheme[elem][0] = 'nop' if copyScheme[elem][0] == 'jmp' else 'jmp'
        typeOfEnd, accumulator = part1(copyScheme)
        if typeOfEnd == "end":
            return accumulator


class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1[1]}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

