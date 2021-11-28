from time import time
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return tuple([int(i.strip().split(' ')[-1]) for i in f.readlines()])

            
def sixteen_digit_binary_representation(n: int):
    return str(bin(n)).replace('0b', '').zfill(32)[-16:]

def part1(scheme: tuple):
    generator_A_value, generator_B_value = scheme
    generator_A_factor, generator_B_factor, divider = 16807, 48271, 2147483647
    judge_value = 0
    for it in range(40_000_000):
        generator_A_value, generator_B_value = (generator_A_value * generator_A_factor) % divider, (generator_B_value * generator_B_factor) % divider
        if sixteen_digit_binary_representation(generator_A_value) == sixteen_digit_binary_representation(generator_B_value):
            judge_value += 1

    return judge_value

def part2(scheme: tuple):
    generator_A_value, generator_B_value = scheme
    generator_A_factor, generator_B_factor, divider = 16807, 48271, 2147483647
    judge_value = 0
    for it in range(5_000_000):
        generator_A_value, generator_B_value = (generator_A_value * generator_A_factor) % divider, (generator_B_value * generator_B_factor) % divider
        while generator_A_value % 4 != 0:
            generator_A_value = (generator_A_value * generator_A_factor) % divider

        while generator_B_value % 8 != 0:
            generator_B_value = (generator_B_value * generator_B_factor) % divider

        if sixteen_digit_binary_representation(generator_A_value) == sixteen_digit_binary_representation(generator_B_value):
            judge_value += 1

    return judge_value

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

