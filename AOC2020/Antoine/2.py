from time import time
import re
import unittest
a = time()


def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]


def getPasswordInfo(instruction: str, part: int):
    lowerBound, upperBound, char, password = re.split('-|: | ', instruction)
    return range(int(lowerBound), int(upperBound)+1) if part == 1 else [int(lowerBound)-1, int(upperBound)-1], char, password


def isValidPasswordP1(instruction: str):
    occurenciesRange, charToCount, password = getPasswordInfo(instruction, 1)
    if password.count(charToCount) in occurenciesRange:
        return True

def isValidPasswordP2(instruction: str):
    occurenciesRange, charToFind, password = getPasswordInfo(instruction, 2)
    if (password[occurenciesRange[0]] == charToFind and password[occurenciesRange[1]] != charToFind) or (password[occurenciesRange[0]] != charToFind and password[occurenciesRange[1]] == charToFind):
        return True

def part1(scheme: list):
    validPasswordsAmount = 0
    for instruction in scheme:
        validPasswordsAmount += 1 if isValidPasswordP1(instruction) else 0
    return validPasswordsAmount


def part2(scheme: list):
    validPasswordsAmount = 0
    for instruction in scheme:
        validPasswordsAmount += 1 if isValidPasswordP2(instruction) else 0
    return validPasswordsAmount


class Tests(unittest.TestCase):

    def testP1(self):
        testInput = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(part1(testInput), 2)
        self.assertEqual(part2(testInput), 1)


if __name__ == "__main__":
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme)
    print(f"Part 2: {p2}")
    print(time()-a)

