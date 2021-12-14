from time import time
import unittest
from math import sqrt
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [int(it) for i in f.readlines() for it in i.strip()]

def get_neighbours(position: int, scheme: list):
    scheme_width = int(sqrt(len(scheme)))
    if position % scheme_width == 0:
        return (position + delta for delta in [-scheme_width, -scheme_width + 1, 1, scheme_width, scheme_width + 1] if position + delta in range(len(scheme)))
    elif (position + 1) % scheme_width == 0:
        return (position + delta for delta in [-scheme_width - 1, -scheme_width, -1, scheme_width - 1, scheme_width] if position + delta in range(len(scheme)))
    else:
        return (position + delta for delta in [-scheme_width - 1, -scheme_width, -scheme_width + 1, -1, 1, scheme_width - 1, scheme_width, scheme_width + 1] if position + delta in range(len(scheme)))

def return_to_zero(value: int):
    return 0 if value >= 10 else value

def flash_step(scheme: list):
    flash_iteration_amount = 0
    scheme = [elem + 1 for elem in scheme]
    while 10 in scheme:
        for position, elem in enumerate(scheme):
            if elem == 10:
                for neighbour in get_neighbours(position, scheme):
                    if scheme[neighbour] != 10:
                        scheme[neighbour] += 1
                scheme[position] += 1
                flash_iteration_amount += 1
    scheme = [return_to_zero(elem) for elem in scheme]

    return flash_iteration_amount, scheme


def part1(scheme: list):
    total_flashes = 0
    for it in range(100):
        flash_iteration_amount, scheme = flash_step(scheme)
        total_flashes += flash_iteration_amount

    return total_flashes

def part2(scheme: list):
    flash_iteration_amount, count = 0, 0
    while flash_iteration_amount != len(scheme):
        flash_iteration_amount, scheme = flash_step(scheme)
        count += 1

    return count

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

