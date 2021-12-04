from time import time
import unittest
from collections import defaultdict
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip() for i in f.readlines()]

def parse_scheme(scheme: list):
    boards, board_number = defaultdict(list), -1
    for line in scheme:
        if ',' in line:
            drawed_numbers = [int(it) for it in line.split(',')]
        elif ' ' in line:
            for elem in line.split():
                boards[board_number].append(int(elem))
        else:
            board_number += 1
    
    return drawed_numbers, boards

def is_board_done(marked_numbers: list):
    return all(b in marked_numbers for b in [0, 1, 2, 3, 4]) or all(b in marked_numbers for b in [5, 6, 7, 8, 9]) or all(b in marked_numbers for b in [10, 11, 12, 13, 14]) or all(b in marked_numbers for b in [15, 16, 17, 18, 19]) or all(b in marked_numbers for b in [20, 21, 22, 23, 24]) or all(b in marked_numbers for b in [0, 5, 10, 15, 20]) or all(b in marked_numbers for b in [1, 6, 11, 16, 21]) or all(b in marked_numbers for b in [2, 7, 12, 17, 22]) or all(b in marked_numbers for b in [3, 8, 13, 18, 23]) or all(b in marked_numbers for b in [4, 9, 14, 19, 24])
            
def part1(scheme: list):
    drawed_numbers, boards = parse_scheme(scheme)
    marked_numbers = {k:list() for k in boards}
    for elem in drawed_numbers:
        for key, board in boards.items():
            if elem in board:
                marked_numbers[key].append(board.index(elem))
                if is_board_done(marked_numbers[key]):
                    return elem * sum(board[it] for it in range(len(board)) if it not in marked_numbers[key])

def part2(scheme: list):
    drawed_numbers, boards = parse_scheme(scheme)
    marked_numbers = {k:list() for k in boards}
    ended_boards = list()
    for elem in drawed_numbers:
        for key, board in boards.items():
            if elem in board:
                marked_numbers[key].append(board.index(elem))
                if is_board_done(marked_numbers[key]) and key not in ended_boards:
                    ended_boards.append(key)
                    if len(ended_boards) == len(boards):
                        return elem * sum(board[it] for it in range(len(board)) if it not in marked_numbers[key])

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

