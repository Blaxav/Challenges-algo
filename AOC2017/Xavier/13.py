from sys import argv
from time import time


def cost(t0, layers, valueToAdd):
    cost = 0
    for depth in layers:
        if (t0 + depth) % (2*(layers[depth]-1)) == 0:
            cost += depth * layers[depth] + valueToAdd

    return cost


def caught(t0, layers):
    cost = 0
    for depth in layers:
        if (t0 + depth) % (2*(layers[depth]-1)) == 0:
            return True

    return False


if __name__ == '__main__':

    layers = {}

    input_data = open(argv[1], 'r')
    for line in input_data:
        layers[int(line.split(": ")[0])] = int(line.split(": ")[1])

    print("Part 1 : ", cost(0, layers, 0))

    timer = time()
    t0 = 0
    while caught(t0, layers):
        t0 += 1
    print("Part 2 : ", t0)
    print("Time with caught fct %-3.3fs" % (time() - timer))

    timer = time()
    t0 = 0
    while cost(t0, layers, 1) > 0:
        t0 += 1
    print("Part 2 : ", t0)
    print("Time with cost fct  %-3.3fs" % (time() - timer))
