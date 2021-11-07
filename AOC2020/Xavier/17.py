import re
import sys
import time
from collections import defaultdict, deque
from copy import deepcopy
from math import sqrt

from utils import add_one, is_prime, prime_numbers


def affiche(grid):
    for w in range(len(grid)):
        print("w=", w - int(len(grid)/2))
        for z in range(len(grid)):
            print("z=", z - int(len(grid)/2))
            for line in grid[w][z]:
                for state in line:
                    print(state, end="")
                print()
            print()
        print()
    print()


def extend(grid):
    size = len(grid[0][0]) + 2

    for w in range(len(grid)):
        for z in range(len(grid)):
            # a chaque ligne on ajoute un '.' a gauche et a droite
            for line in grid[w][z]:
                line.insert(0, '.')
                line.insert(len(line), '.')
            # on ajoute une ligne de '.' en haut et en bas
            grid[w][z].insert(0, ['.' for porc in range(size)])
            grid[w][z].insert(len(grid[w][z]), ['.' for porc in range(size)])

    # on ajoute deux couches de '.' au debut et a la fin en z sur chaque couche en w
    for w in range(len(grid)):
        maxZ = len(grid) + 1
        for index in [0, maxZ]:
            grid[w].insert(index, [])
            for k in range(size):
                grid[w][index].append([])
                for j in range(size):
                    grid[w][index][-1].append('.')

    # on ajoute deux cubes de '.' en w au debut et a la fin
    couches = len(grid[0])
    taille = len(grid[0][0][0])
    cube = [[['.' for y in range(taille)] for x in range(
        taille)] for z in range(couches)]

    grid.insert(0, deepcopy(cube))
    grid.insert(len(grid), deepcopy(cube))


def neighbors(w, z, x, y, nCouches, gridSize):
    for nw in range(max([0, w-1]), min([w+2, nCouches])):
        for nz in range(max([0, z-1]), min([z+2, nCouches])):
            for nx in range(max([0, x-1]), min([x+2, gridSize])):
                for ny in range(max([0, y-1]), min([y+2, gridSize])):
                    if (nw, nz, nx, ny) != (w, z, x, y):
                        yield(nw, nz, nx, ny)


def activate(w, z, x, y, grid):
    neib = neighbors(w, z, x, y, len(grid), len(grid[w][z]))
    active_neighbors = 0
    nbr_nbrs = 0
    for (nw, nz, nx, ny) in neib:
        nbr_nbrs += 1

        if grid[nw][nz][nx][ny] == '#':
            active_neighbors += 1
            if active_neighbors == 4:
                return False

    # print(w, z, x, y, "   ", nbr_nbrs, "     ", len(grid),
    #      len(grid[0]), len(grid[0][0]), len(grid[0][0][0]))
    if active_neighbors == 3:
        return True
    else:
        return False


def desactivate(w, z, x, y, grid):
    neib = neighbors(w, z, x, y, len(grid), len(grid[w][z]))
    active_neighbors = 0
    for (nw, nz, nx, ny) in neib:
        if grid[nw][nz][nx][ny] == '#':
            active_neighbors += 1
            if active_neighbors == 4:
                return True

    if 2 <= active_neighbors <= 3:
        return False
    else:
        return True


def propagate(grid):

    toActivate = []
    toDesactivate = []
    for w in range(len(grid)):
        for z in range(len(grid)):
            for x in range(len(grid[w][z])):
                for y in range(len(grid[w][z])):
                    if grid[w][z][x][y] == '.':
                        if activate(w, z, x, y, grid):
                            toActivate.append((w, z, x, y))
                    elif grid[w][z][x][y] == '#':
                        if desactivate(w, z, x, y, grid):
                            toDesactivate.append((w, z, x, y))

    for (w, z, x, y) in toActivate:
        grid[w][z][x][y] = '#'

    for (w, z, x, y) in toDesactivate:
        grid[w][z][x][y] = '.'


if __name__ == '__main__':
    start = time.time()

    grid = [[[]]]

    fileIn = open(sys.argv[1])
    for line in fileIn:
        # grid[0].append(deque())
        grid[0][0].append([])
        for state in line.rstrip():
            grid[0][0][-1].append(state)

    affiche(grid)

    Nstep = 6
    log = False

    for k in range(Nstep):
        extend(grid)
        propagate(grid)
        if log:
            affiche(grid)

    cnt = 0
    for w in range(len(grid)):
        for z in range(len(grid)):
            for x in range(len(grid[w][z])):
                for y in range(len(grid[w][z][x])):
                    if grid[w][z][x][y] == '#':
                        cnt += 1

    print("Result: ", cnt)

    end = time.time()
    print()
    print("Time: %10.6fs" % (end-start))
