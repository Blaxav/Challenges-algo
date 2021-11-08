from time import time
import unittest
from itertools import repeat
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return f.readline().strip()
            
def part1(scheme: str):
    decompressed = ''
    indix = 0
    while indix < len(scheme):
        if scheme[indix].isupper():
            decompressed += scheme[indix]
            indix += 1
        elif scheme[indix] == '(':
            shift = 1
            while scheme[indix+shift] != ')':
                shift += 1
            repetitions = scheme[indix+1:indix+shift].split('x')
            for elem in repeat(scheme[indix+shift+1:indix+shift+1+int(repetitions[0])], int(repetitions[1])):
                decompressed += elem
            indix += shift + 1 + int(repetitions[0])
    return decompressed

# def oneDecompression(scheme: str):
#     decompressed = ''
#     indix = 0
#     while indix < len(scheme):
#         if scheme[indix].isupper():
#             decompressed += scheme[indix]
#             indix += 1
#         elif scheme[indix] == '(':
#             shift = 1
#             while scheme[indix+shift] != ')':
#                 shift += 1
#             repetitions = scheme[indix+1:indix+shift].split('x')
#             for elem in repeat(scheme[indix+shift+1:indix+shift+1+int(repetitions[0])], int(repetitions[1])):
#                 decompressed += elem
#             indix += shift + 1 + int(repetitions[0])
#             decompressed += scheme[indix:]
#             break
#     return decompressed

def extractSubStrings(scheme: str):
    subStrings = list()
    indix = 0
    while indix < len(scheme):
        if scheme[indix].isupper():
            subString = (scheme[indix], 1)
            indix += 1
        elif scheme[indix] == '(':
            shift = 1
            while scheme[indix+shift] != ')':
                shift += 1
            repetitions = scheme[indix+1:indix+shift].split('x')
            totalShift = shift + 1 + int(repetitions[0])
            subString = (scheme[indix+shift+1:indix+totalShift], int(repetitions[1]))
            indix += totalShift
        subStrings.append(subString)
    return subStrings

def part2(scheme: str, res: int):
    subStrings = extractSubStrings(scheme)
    comp = 0
    for subString in subStrings:
        currentString, multiplier = subString
        if '(' in currentString:
            res += part2(currentString, 0) * multiplier
        else:
            res += len(currentString) * multiplier
    return res

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme)
    print(f"Part 1: {len(p1)}")
    # test = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
    test = scheme
    p2 = part2(test, 0)
    print(f"Part 2: {p2}")
    print(time()-a)

