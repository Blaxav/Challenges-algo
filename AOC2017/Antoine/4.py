from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().split(' ') for i in f.readlines()]

            
def part1(scheme: list):
    valid_passphrase_amount = 0
    for elem in scheme:
        if len(elem) == len(set(elem)):
            valid_passphrase_amount += 1
    return valid_passphrase_amount



def part2(scheme: list):
    valid_passphrase_amount = 0
    for elem in scheme:
        sorted_passphrases = [''.join(sorted(passphrase)) for passphrase in elem]
        if len(sorted_passphrases) == len(set(sorted_passphrases)):
            valid_passphrase_amount += 1
    return valid_passphrase_amount

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

