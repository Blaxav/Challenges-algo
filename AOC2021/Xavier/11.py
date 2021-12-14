from collections import deque
from itertools import product
from sys import argv


def neighbors(i, j):
    for (k, p) in product(range(-1, 2), range(-1, 2)):
        if (k, p) != (0, 0):
            yield((i+k, j+p))


if __name__ == '__main__':

    grid = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        grid.append([0] + [int(i) for i in line.rstrip('\n')] + [0])
    input_data.close()

    grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]

    N_steps = 100
    n = len(grid) - 1
    m = len(grid[0]) - 1
    n_lightning = 0
    enlighting_nodes = deque()
    has_lightened = set()

    step = 0
    while len(has_lightened) < (n-1)*(m-1):

        enlighting_nodes.clear()
        has_lightened.clear()

        # Init increasing process
        for (i, j) in product(range(1, n), range(1, m)):
            grid[i][j] += 1
            if grid[i][j] == 10:
                enlighting_nodes.append((i, j))
                has_lightened.add((i, j))
                n_lightning += 1

        # Lightning loop
        while enlighting_nodes:
            c_i, c_j = enlighting_nodes.pop()
            for (k, p) in neighbors(c_i, c_j):
                grid[k][p] += 1
                if grid[k][p] >= 10 and k not in [0, n] and p not in [0, m]:
                    if (k, p) not in has_lightened:
                        enlighting_nodes.append((k, p))
                        has_lightened.add((k, p))
                        n_lightning += 1

        # reinitialization
        for (i, j) in product(range(n), range(m)):
            if grid[i][j] >= 10:
                grid[i][j] = 0
        step += 1
        if step == 100:
            print("Part 1 : ", n_lightning)

    print("Part 2 :", step)
