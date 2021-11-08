from time import time
from collections import defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    passportDict, comp = defaultdict(dict), 0
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                if ' ' in line:
                    for elem in line.split():
                        key, value = elem.split(":")
                        passportDict[comp][key] = value
                else:
                    key, value = line.split(":")
                    passportDict[comp][key] = value
            else:
                comp += 1

    return passportDict

            
def part1(scheme: dict):
    validPassportAmount = 0
    for passport in scheme.values():
        if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
            validPassportAmount += 1
    return validPassportAmount

def part2(scheme: list):
    validPassportAmount = 0
    for passport in scheme.values():
        if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
            if 1920 <= int(passport['byr']) <= 2002:
                if 2010 <= int(passport['iyr']) <= 2020:
                    if 2020 <= int(passport['eyr']) <= 2030:
                        if (passport['hgt'][-2:] == 'cm' and len(passport['hgt']) == 5 and 150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == 'in' and len(passport['hgt']) == 4 and 59 <= int(passport['hgt'][:-2]) <= 76):
                            if len(passport['hcl']) == 7 and passport['hcl'].startswith('#') and not [char for char in passport['hcl'] if not char.isdigit() and char > 'f']:
                                if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                                    if len(passport['pid']) == 9:
                                        validPassportAmount += 1
    return validPassportAmount

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

