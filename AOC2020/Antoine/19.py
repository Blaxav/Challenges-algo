from time import time
import re
from collections import deque
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def parseScheme(scheme: list):
    rulesDict = dict()
    while scheme[0]:
        ruleNumber, ruleContent = scheme[0].split(': ')
        rulesDict[ruleNumber] = ruleContent.replace('"', '').split(' ')
        del scheme[0]
    del scheme[0]

    return rulesDict, scheme

def ruleDoesNotContainNumbers(rule: list):
    for elem in rule:
        if elem.isdigit():
            return False
    
    return True

def elemsAreExplicited(rule: list, explicitedRules: dict):
    for elem in rule:
        if elem != '|' and elem not in explicitedRules:
            return False
    
    return True

def explicitRule(rule: list, explicitedRules: dict):
    explicitedRule = '('
    for elem in rule:
        if elem != '|':
            explicitedRule += explicitedRules[elem]
        else:
            explicitedRule += '|'
    explicitedRule += ')'

    return explicitedRule

def explicitAllRules(rulesDict: dict):
    explicitedRules = {k:v[0] for k, v in rulesDict.items() if ruleDoesNotContainNumbers(v)}
    explicitableRules = deque([k for k, v in rulesDict.items() if elemsAreExplicited(v, explicitedRules) and k not in explicitedRules])
    while '0' not in explicitedRules:
        newRule = explicitableRules.popleft()
        explicitedRules[newRule] = explicitRule(rulesDict[newRule], explicitedRules)
        for k, v in rulesDict.items():
            if elemsAreExplicited(v, explicitedRules) and k not in explicitedRules and k not in explicitableRules:
                explicitableRules.append(k)

    return explicitedRules


def part1(scheme: list):
    rulesDict, scheme = parseScheme(scheme)
    regexZero = '^' + explicitAllRules(rulesDict)['0'] + '$'
    res = 0
    for elem in scheme:
        if re.match(regexZero, elem):
            res += 1
    
    return res

def part2(scheme: list):
    rulesDict, scheme = parseScheme(scheme)
    explicitedRules = explicitAllRules(rulesDict)
    res = 0
    for m in range(1, 6):
        for n in range(1, 6):
            regexZero = '^' + explicitedRules['42'] * m + explicitedRules['42'] * n + explicitedRules['31'] * n + '$'
            for elem in scheme:
                if re.match(regexZero, elem):
                    res += 1
    
    return res

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = readFile()
    p1 = part1(scheme[:])
    print(f"Part 1: {p1}")
    p2 = part2(scheme[:])
    print(f"Part 2: {p2}")
    print(time()-a)

