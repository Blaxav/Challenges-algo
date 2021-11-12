from sys import argv


def cost(t0, layers, valueToAdd):
    cost = 0
    for depth in layers:
        if (t0 + depth) % (2*(layers[depth]-1)) == 0:
            cost += depth * layers[depth] + valueToAdd

    return cost


if __name__ == '__main__':

    layers = {}

    input_data = open(argv[1], 'r')
    for line in input_data:
        layers[int(line.split(": ")[0])] = int(line.split(": ")[1])

    print(cost(0, layers, 0))

    t0 = 0
    while cost(t0, layers, 1) > 0:
        t0 += 1
    print("Part 2 : ", t0)
