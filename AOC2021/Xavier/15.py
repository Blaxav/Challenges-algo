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


class Path:
    def __init__(self, i, j, dist):
        self.i = i
        self.j = j
        self.dist = dist

    def __gt__(self, other):
        return self.dist > other.dist

    def neighbors(self, n, m):
        if self.i > 0:
            yield(self.i-1, self.j)
        if self.i < n-1:
            yield(self.i+1, self.j)
        if self.j > 0:
            yield(self.i, self.j-1)
        if self.j < m-1:
            yield(self.i, self.j+1)

    def __contains__(self, node):
        return self.i == node[0] and self.j == node[1]


def risk(i, j, grid, n, m):
    k = i % n
    p = j % m
    risk = grid[k][p]
    r = i // n
    e = j // m
    risk += e + r
    '''if ((risk-1) % 10) + 1 != grid[k][p]:
        print("Stop ! ")
        print(grid[k][p])
        print(((risk-1) % 10) + 1)
        exit()'''
    return ((risk-1) % 9) + 1


if __name__ == '__main__':

    grid = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        grid.append([int(i) for i in line.rstrip('\n')])
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
    open_path = deque([(Path(0, 0, 0))])
    it = 0
    already = False
    while open_path:

        current_path = open_path.popleft()

        if current_path.dist < best_dist:
            for (k, p) in current_path.neighbors(n, m):
                already = False
                if (k, p) == (n-1, m-1):
                    best_dist = min(
                        (best_dist, current_path.dist + risk(k, p, grid, n, m)))
                elif current_path.dist + risk(k, p, grid, n, m) <= min((distances[k][p], best_dist)):
                    distances[k][p] = current_path.dist + \
                        risk(k, p, grid, n, m)
                    if (k, p) in open_path:
                        print("coucou")
                        id = open_path.find((k, p))
                    # for id in range(len(open_path)):
                    #    if (k, p) == (open_path[id].i, open_path[id].j):
                        # print("coucou")
                        open_path[id] = Path(
                            k, p, min(open_path[id].dist, current_path.dist + risk(k, p, grid, n, m)))
                        already = True
                        break
                    if not already:
                        open_path.append(
                            Path(k, p, current_path.dist + risk(k, p, grid, n, m)))
        it += 1
        if it % 1000000 == 0:
            print(best_dist, "  ", len(open_path))
    print("Part 1 : ", it, " iterations, val = ", best_dist)
    print("%-10.3fs" % (time() - t0))

    # Algortihm
    open_path = deque([Path(0, 0, 0)])
    it = 0
    best_dist = 100*best_dist
    already = False
    while open_path:

        current_path = open_path.popleft()

        if current_path.dist < best_dist:
            for (k, p) in current_path.neighbors(5*n, 5*m):
                already = False
                # print(k, p, distances[k][p])
                if (k, p) == ((5*n)-1, (5*m)-1):
                    best_dist = min(
                        (best_dist, current_path.dist + risk(k, p, grid, n, m)))
                elif current_path.dist + risk(k, p, grid, n, m) <= min((distances[k][p], best_dist)):
                    distances[k][p] = current_path.dist + \
                        risk(k, p, grid, n, m)
                    for id in range(len(open_path)):
                        if (k, p) == (open_path[id].i, open_path[id].j):
                            # print("coucou")
                            open_path[id] = Path(
                                k, p, min(open_path[id].dist, current_path.dist + risk(k, p, grid, n, m)))
                            already = True
                            break
                    if not already:
                        open_path.append(
                            Path(k, p, current_path.dist + risk(k, p, grid, n, m)))
        it += 1
        if it % 10000 == 0:
            print(best_dist, "  ", len(open_path))
    print("Part 2 : ", it, " iterations, val = ", best_dist)
    print("%-10.3fs" % (time() - t0))
