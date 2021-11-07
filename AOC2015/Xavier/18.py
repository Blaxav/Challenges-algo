import sys


def display(lights):
    for l in lights[1:-1]:
        for elt in l[1:-1]:
            print(elt, end='')
        print()


def count_on_neighbors(lights, i, j):
    total = 0
    for k in [-1, 0, 1]:
        for p in [-1, 0, 1]:
            if (k, p) != (0, 0) and lights[i+k][j+p] == '#':
                total += 1
    return total


def change_state(lights, i, j):
    if lights[i][j] == '.':
        if count_on_neighbors(lights, i, j) == 3:
            return '#'
    else:
        if count_on_neighbors(lights, i, j) not in [2, 3]:
            return '.'
    return lights[i][j]


def next(lights):
    n = len(lights)

    # Init new state
    new = list()
    for i in range(n):
        new.append(['.'] * n)

    for i in range(1, n-1):
        for j in range(1, n-1):
            new[i][j] = change_state(lights, i, j)

    new[1][1] = '#'
    new[1][n-2] = '#'
    new[n-2][1] = '#'
    new[n-2][n-2] = '#'

    return new


if __name__ == '__main__':

    input_data = open(sys.argv[1], 'r')
    n = int(sys.argv[2])
    lights = [['.'] * (n + 2)]
    for line in input_data:
        lights.append(['.'] + [elt for elt in line.rstrip('\n')] + ['.'])
    lights.append(['.'] * (n+2))

    lights[1][1] = '#'
    lights[1][n] = '#'
    lights[n][1] = '#'
    lights[n][n] = '#'

    for k in range(100):
        lights = next(lights)

    total = 0
    for l in lights:
        total += sum([1 for t in l if t == '#'])
    print("Total ", total)
