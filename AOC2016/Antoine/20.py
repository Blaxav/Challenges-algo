from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [[int(bound) for bound in i.strip().split('-')] for i in f.readlines()]
            
def part1(scheme: list):
    sorted_bounds = sorted(scheme, key=lambda x: x[0])
    lower_bound, upper_bound = sorted_bounds[0][0], sorted_bounds[0][1]
    for elem in sorted_bounds:
        if elem[1] <= upper_bound:
            continue
        elif elem[0] <= upper_bound + 1 and elem[1] >= upper_bound + 1:
            upper_bound = elem[1]
        else:
            return upper_bound + 1


def part2(scheme: list, max_bound: int):
    sorted_bounds = sorted(scheme, key=lambda x: x[0])
    res, lower_bound, upper_bound = 0, sorted_bounds[0][0], sorted_bounds[0][1]
    for elem in sorted_bounds:
        if elem[1] <= upper_bound:
            continue
        elif elem[0] <= upper_bound + 1 and elem[1] >= upper_bound + 1:
            upper_bound = elem[1]
        else:
            res += elem[0] - upper_bound - 1
            lower_bound, upper_bound = elem[0], elem[1]
    
    return res + max_bound - upper_bound

class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part1([[5, 8], [0, 2], [4, 7]]), 3)
        self.assertEqual(part2([[5, 8], [0, 2], [4, 7]], 9), 2)


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme, 4294967295)
    print(f"Part 2: {p2}")
    print(time()-a)

