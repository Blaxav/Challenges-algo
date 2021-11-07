import re
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers


########################################################################################
#       Part 1
########################################################################################
def ascii_test():
    fileIn = open("input_4.txt")
    somme = 0
    okPass = 0
    keys = []
    for line in fileIn:
        
        if line != "\n":
            pasprtElts = [entry.split(":")[0] for entry in line.split()]
            for code in pasprtElts:
                #on somme le code ascii de chaque caractere des cles des passeports
                for c in code:
                    somme += ord(c)

        # passeport suivant        
        else:
            if somme in [2572, 2268]:
                okPass += 1
            somme = 0
    
    #dernier passeport
    if somme in [2572, 2268]:
        okPass += 1

    print("Valid passports: ", okPass)
    fileIn.close()


########################################################################################
#           Part 2
########################################################################################

formatKey = {
    'byr':'19[2-9][0-9]|200[0-2]',
    'iyr':'201[0-9]|2020',
    'eyr':'202[0-9]|2030',
    'hgt':'^1[5-8][0-9]cm$|^19[0-3]cm$|^59in$|^6[0-9]in$|^7[0-6]in$',
    'hcl':'^#[0-9a-f]{6}$',
    'ecl':'^amb|blu|brn|gry|grn|hzl|oth$',
    'pid':'^[0-9]{9}$'
}

def validentries():

    fileIn = open("input_4.txt")

    somme = 0
    okPass = 0

    for line in fileIn:
        
        if line != "\n":
            for entry in line.split():
                code, val = entry.split(":")

                if code in formatKey:
                    if re.search(formatKey[code], val):
                        somme += 1
                    

        # passeport suivant        
        else:
            if somme == 7:
                okPass += 1
            somme = 0

    if somme == 7:
        okPass += 1

    print("Valid: ", okPass)
    

########################################################################################
#           Main 
########################################################################################
if __name__ == '__main__' :
    #Part 1 ascci mod
    start = time.time()

    ascii_test()

    end = time.time()
    print("Time: %10.6fs" % (end-start))

    #Part 2
    start = time.time()

    validentries()

    end = time.time()
    print("Time: %10.6fs" % (end-start))
