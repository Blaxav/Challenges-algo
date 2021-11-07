import collections
import sys
from datetime import datetime as timestamp
from itertools import combinations


def next(taken, n_bags):

    c_id = 1
    while taken[-c_id] + 1 == n_bags - c_id + 1:
        c_id += 1

        # if no one can moove to the right, initialize list of size n + 1
        if c_id == len(taken) + 1:

            return [i for i in range(len(taken) + 1)]

    return taken[:-c_id] + \
        [taken[-c_id] + i for i in range(1, c_id + 1)]


if __name__ == '__main__':

    containers = []
    input_data = open(sys.argv[1], 'r')
    for line in input_data:
        containers.append(int(line.rstrip('\n')))

    containers = sorted(containers)

    N = 150
    n_bags = len(containers)

    n_repeat = 1
    t = timestamp.now()
    for i in range(n_repeat):
        total = 0
        taken = [0]
        while len(taken) < n_bags:
            taken = next(taken, n_bags)
            if sum([containers[i] for i in taken]) == N:
                total += 1
    print("Time by hand  : ", timestamp.now() - t)
    print("Total by hand : ", total)

    t = timestamp.now()
    for i in range(n_repeat):
        total = 0
        for k in range(1, n_bags):
            for perm in combinations(containers, k):
                if sum(perm) == N:
                    total += 1

            if total > 0:
                break
    print("Time by hand  : ", timestamp.now() - t)
    print("Total itertools : ", total)
