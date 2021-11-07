import re
import sys
import time
from collections import defaultdict
from math import sqrt

from utils import add_one, is_prime, prime_numbers


class Seat:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.neighbors = []
        self.val = val


class Grid:
    def __init__(self):
        self.seats = []

    def read(self, path):
        fileIn = open(path)
        row = 0
        for line in fileIn:
            self.seats.append([])
            col = 0
            for val in line.strip():
                if val != '.':
                    self.seats[-1].append(Seat(row, col, val))
                col += 1
            row += 1

    def set_neighbors(self):
        for line in self.seats:
            i = line[0].i


def read_file(path):

    grid = [['.']*50]

    fileIn = open(path)
    for line in fileIn:
        grid.append(['.'])
        grid[-1] += [i for i in line.strip()]
        grid[-1].append('.')
    grid[0] = ['.'] * len(grid[1])
    grid.append(['.'] * len(grid[1]))

    return grid


def read_filep2(path):

    fileIn = open(path)
    for line in fileIn:
        grid.append([])
        grid[-1] += [i for i in line.strip()]
    return grid


def printG(grid):
    for t in grid:
        for i in t:
            print(i, end="")
        print()


def neighbors(i, j):
    for k in range(-1, 2):
        yield (i-1, j + k)
    yield (i, j-1)
    yield (i, j+1)
    for k in range(-1, 2):
        yield (i+1, j + k)


def moove(grid):

    toChange = []

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            # print(grid[i][j], end="")
            # Rule 1
            neibrs = neighbors(i, j)
            if grid[i][j] == "L":
                if len([(s, t) for (s, t) in neibrs if grid[s][t] != "#"]) == 8:
                    toChange.append((i, j))

            # Rule 2
            if grid[i][j] == '#':
                if len([(s, t) for (s, t) in neibrs if grid[s][t] == "#"]) >= 4:
                    toChange.append((i, j))

    for (i, j) in toChange:
        if grid[i][j] == 'L':
            grid[i][j] = '#'
        else:
            grid[i][j] = 'L'

    return len(toChange)


def mooveP2(grid, neibrs):

    toChange = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "L":
                if len([(s, t) for (s, t) in neibrs[i][j] if grid[s][t] != "#"]) == len(neibrs[i][j]):
                    toChange.append((i, j))

            # Rule 2
            if grid[i][j] == '#':
                if len([(s, t) for (s, t) in neibrs[i][j] if grid[s][t] == "#"]) >= 5:
                    toChange.append((i, j))

    for (i, j) in toChange:
        if grid[i][j] == 'L':
            grid[i][j] = '#'
        else:
            grid[i][j] = 'L'

    return len(toChange)


def search(i, j, grad_i, grad_j, neighbors):
    t = i + grad_i
    k = j + grad_j
    while t >= 0 and t < len(grid) and k >= 0 and k < len(grid[i]) and grid[t][k] == '.':
        t += grad_i
        k += grad_j
    if t >= 0 and t < len(grid) and k >= 0 and k < len(grid[i]):
        neighbors[i][j].append((t, k))


if __name__ == '__main__':
    start = time.time()

    grid = read_file(sys.argv[1])

    log = False
    count = -1
    while count != 0:

        count = moove(grid)
        if log:
            printG(grid)
            print()

    total = 0
    for line in grid:
        for t in line:
            if t == "#":
                total += 1
    print("Result P1: ", total)

    ########################################
    # P2
    grid.clear()
    grid = read_filep2(sys.argv[1])
    for line in grid:
        for t in line:
            print(t, end="")
        print()

    neighbors = []
    for i in range(len(grid)):
        line = grid[i]
        neighbors.append([])
        for j in range(len(grid[i])):
            neighbors[i].append([])
            if grid[i][j] != '.':
                # on cherche vers le haut
                search(i, j, -1, 0, neighbors)

                # on cherche vers le bas
                search(i, j, 1, 0, neighbors)

                # on cherche ver la gauche
                search(i, j, 0, -1, neighbors)

                # on cherche vers la droite
                search(i, j, 0, 1, neighbors)

                # les diagonales
                search(i, j, 1, 1,      neighbors)
                search(i, j, 1, -1,     neighbors)
                search(i, j, -1, 1,     neighbors)
                search(i, j, -1, -1,    neighbors)

    log = False
    count = -1
    print()
    while count != 0:

        count = mooveP2(grid, neighbors)
        if log:
            printG(grid)
            print()

    total = 0
    for line in grid:
        for t in line:
            if t == "#":
                total += 1
    print("Result P1: ", total)

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
