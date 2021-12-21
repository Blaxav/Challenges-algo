from time import time
import unittest
from copy import deepcopy
from collections import defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        transformations = dict()
        for line in (line.strip() for line in f.readlines() if line.strip()):
            if '->' in line:
                line = line.split(' -> ')
                transformations[line[0]] = line[1]
            else:
                poylmer = line
        return poylmer, transformations

def transform_polymer(couple_count: dict, transformations: dict):
    new_couple_count = defaultdict(int)
    for couple, count in couple_count.items():
        new_couple_count[couple[0] + transformations[couple]] += count
        new_couple_count[transformations[couple] + couple[1]] += count

    return new_couple_count

def count_letters(polymer: str, couple_count: dict):
    first_letter, last_letter = polymer[0], polymer[-1]
    letter_count = {k:(0.5 if k in (first_letter, last_letter) else 0) for k in set("".join(couple_count.keys()))}
    for couple, count in couple_count.items():
        letter_count[couple[0]] += count / 2
        letter_count[couple[1]] += count / 2
    
    return letter_count

def part1(polymer: str, transformations: dict, iterations: int):
    couple_count = {k:polymer.count(k) for k in (polymer[it:it+2] for it in range(len(polymer) - 1))}
    for it in range(iterations):
        couple_count = transform_polymer(couple_count, transformations)

    letter_count = count_letters(polymer, couple_count)

    return int(max(letter_count.values()) - min(letter_count.values()))

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    polymer, transformations = readFile()
    p1 = part1(polymer, transformations, 10)
    print(f"Part 1: {p1}")
    p2 = part1(polymer, transformations, 40)
    print(f"Part 2: {p2}")
    print(time()-a)

