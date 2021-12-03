from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

            
def part1(scheme: list):
    gamma_rate, epsilon_rate = '', ''
    for it in range(len(scheme[0])):
        number_range = [number[it] for number in scheme]
        if number_range.count('1') >= len(scheme) / 2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def part2(scheme: list):
    it, oxygen_scheme, co2_scheme = 0, scheme[:], scheme[:]
    while len(oxygen_scheme) > 1:
        number_range = [number[it] for number in oxygen_scheme]
        if number_range.count('1') >= len(oxygen_scheme) / 2:
            oxygen_scheme = [number for number in oxygen_scheme if number[it] == '1']
        else:
            oxygen_scheme = [number for number in oxygen_scheme if number[it] == '0']
        
        it += 1

    it = 0
    while len(co2_scheme) > 1:
        number_range = [number[it] for number in co2_scheme]
        if number_range.count('1') >= len(co2_scheme) / 2:
            co2_scheme = [number for number in co2_scheme if number[it] == '0']
        else:
            co2_scheme = [number for number in co2_scheme if number[it] == '1']
        
        it += 1

    return int(oxygen_scheme[0], 2) * int(co2_scheme[0], 2)

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

