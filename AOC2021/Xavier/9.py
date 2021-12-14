from collections import deque
from functools import reduce
from sys import argv


def has_lower_neighbor(grid, i, j):
    for (k, p) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if grid[k][p] <= grid[i][j]:
            return True
    return False


def neighbors(i, j):
    for (k, p) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        yield((k, p))


if __name__ == '__main__':

    # Grid representation with 10 values around
    grid = []
    basins = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        grid.append([10] + [int(i) for i in line.rstrip('\n')] + [10])
        basins.append([0]*len(grid[-1]))
    input_data.close()

    basins.append([0]*len(grid[-1]))
    basins.append([0]*len(grid[-1]))
    grid = [[10 for i in grid[0]]] + grid + [[10]*len(grid[0])]

    n = len(grid)
    m = len(grid[0])

    total = 0
    local_mins = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not has_lower_neighbor(grid, i, j):
                total += 1 + grid[i][j]
                local_mins.append((i, j))
    print("Part 1 ", total)

    basin_sizes = []
    for (i, j) in local_mins:
        next_position = deque([(i, j)])
        basin_sizes.append(0)
        while next_position:
            basin_sizes[-1] += 1
            (c_i, c_j) = next_position.pop()
            for (k, l) in neighbors(c_i, c_j):
                if grid[k][l] < 9 and grid[k][l] > grid[c_i][c_j]:
                    if basins[k][l] == 0:
                        basins[k][l] = 1
                        next_position.append((k, l))
    print(basin_sizes)
    print("Part 2 : ", reduce(lambda x, y: x*y, sorted(basin_sizes)[-3:]))
