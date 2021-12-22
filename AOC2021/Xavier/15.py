from collections import deque
from sys import argv
from time import time


def neighbors(i, j, n, m):
    if i > 0:
        yield(i-1, j)
    if i < n-1:
        yield(i+1, j)
    if j > 0:
        yield(i, j-1)
    if j < m-1:
        yield(i, j+1)


def risk(i, j, grid, n, m):
    k = i % n
    p = j % m
    risk = grid[k][p]
    r = i // n
    e = j // m
    risk += e + r
    return ((risk-1) % 9) + 1


if __name__ == '__main__':

    grid = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        grid.append([int(i) for i in line.rstrip('\n\r')])
    input_data.close()

    n = len(grid)
    m = len(grid[0])

    distances = []
    for i in range(5*n):
        distances.append([])
        for j in range(5*m):
            distances[-1].append(1e6)
    distances[0][0] = 0

    # Heuristic
    best_dist = sum(grid[0][1:]) + sum([grid[i][m-1] for i in range(1, n)])
    t0 = time()
    print("Heuristic = ", best_dist)

    # Algortihm
    open_path = deque([(0, 0)])
    it = 0
    while open_path:
        (i, j) = open_path.popleft()

        if distances[i][j] < best_dist:
            for (k, p) in neighbors(i, j, n, m):
                if (k, p) == (n-1, m-1):
                    best_dist = min(
                        (best_dist, distances[i][j] + risk(k, p, grid, n, m)))
                elif distances[i][j] + risk(k, p, grid, n, m) <= min((distances[k][p], best_dist)):
                    distances[k][p] = distances[i][j] + risk(k, p, grid, n, m)
                    if (k, p) not in open_path:
                        open_path.append((k, p))
        it += 1
        if it % 1000000 == 0:
            print(best_dist, "  ", len(open_path))
    print("Part 1 : ", it, " iterations, val = ", best_dist)
    print("%-10.3fs" % (time() - t0))

    # Algortihm
    open_path = deque([(0, 0)])
    it = 0
    best_dist = 10*best_dist
    while open_path:
        (i, j) = open_path.popleft()

        if distances[i][j] < best_dist:
            for (k, p) in neighbors(i, j, 5*n, 5*m):
                if (k, p) == ((5*n)-1, (5*m)-1):
                    best_dist = min(
                        (best_dist, distances[i][j] + risk(k, p, grid, n, m)))
                elif distances[i][j] + risk(k, p, grid, n, m) <= min((distances[k][p], best_dist)):
                    distances[k][p] = distances[i][j] + risk(k, p, grid, n, m)
                    if (k, p) not in open_path:
                        open_path.append((k, p))
        it += 1
        if it % 100000 == 0:
            print(best_dist, "  ", len(open_path))
    print("Part 2 : ", it, " iterations, val = ", best_dist)
    print("%-10.3fs" % (time() - t0))
