from time import time
from itertools import islice
import unittest
a = time()


def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return int(f.readline().strip())


def one_tour_circle_p1(elf_list: list):
    if len(elf_list) % 2 == 0:
        return [elem for count, elem in enumerate(elf_list) if count % 2 == 0]
    else:
        return [elem for count, elem in enumerate(elf_list) if count % 2 == 0 and count]


def one_tour_circle_p2(elf_list: list):

    passed = list()
    for it in elf_list:
        if it in elf_list and it not in passed:
            passed.append(it)
            # print(it, elf_list)
            elf_list.sort()
            # print(elf_list)
            elf_list = elf_list[elf_list.index(
                it):] + elf_list[:elf_list.index(it)]
            # print(elf_list)
            if len(elf_list) % 2 == 0:
                del elf_list[len(elf_list) // 2]
            else:
                del elf_list[(len(elf_list) - 1) // 2]
            # print(elf_list)
            # print("\n")

    elf_list.sort()

    return elf_list


def part1(elf_amount: int):
    elf_list = list(range(elf_amount))
    while len(elf_list) != 1:
        elf_list = one_tour_circle_p1(elf_list)

    return elf_list[0] + 1


def get_winner_index(elf_amount: int, previous_res_index: int):
    if elf_amount == 1:
        return 0
    else:
        killed_index_after_shift = elf_amount // 2 - 1
        if previous_res_index == elf_amount - 2:
            return 0
        elif previous_res_index >= killed_index_after_shift:
            return previous_res_index + 2
        else:
            return previous_res_index + 1


def part2(elf_amount: int):
    it, previous_res_index = 0, 0
    while it != elf_amount:
        it += 1
        previous_res_index = get_winner_index(it, previous_res_index)

    return previous_res_index + 1



class Tests(unittest.TestCase):

    def testP1(self):
        self.assertEqual(part2(1), 1)
        self.assertEqual(part2(2), 1)
        self.assertEqual(part2(3), 3)
        self.assertEqual(part2(4), 1)
        self.assertEqual(part2(5), 2)
        self.assertEqual(part2(6), 3)
        self.assertEqual(part2(7), 5)
        self.assertEqual(part2(8), 7)
        self.assertEqual(part2(11), 2)


if __name__ == "__main__":
    # unittest.main()
    elf_amount = readFile()
    p1 = part1(elf_amount)
    print(f"Part 1: {p1}")
    p2 = part2(elf_amount)
    print(f"Part 2: {p2}")
    print(time()-a)
