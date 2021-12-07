from sys import argv
from time import time


def fuel_cost(positions, place):
    return sum([abs(p-place) for p in positions])


def fuel_cost_p2(positions, place):
    return int(sum([abs(p-place)*(abs(p-place) + 1)/2 for p in positions]))


def int_middle(a, b):
    return int((a+b)/2)


if __name__ == '__main__':

    t0 = time()

    if len(argv) < 2:
        print("Usage : python3 6.py file_path")
        print("   ex : python3 6.py input/6.txt")
        exit()

    input_data = open(argv[1], 'r')
    positions = [int(i)
                 for i in input_data.readline().rstrip('\n').split(',')]
    input_data.close()

    positions.sort()
    # The fonction to minimize is convex (sum(abs(s-place)))
    # Can stop whenever the function starts increasing
    c_pos = positions[0]
    current_val = fuel_cost(positions, positions[0])

    decrease = True
    while decrease:
        previous_val = current_val

        c_pos += 1
        current_val = fuel_cost(positions, c_pos)

        if current_val > previous_val:
            decrease = False

    print("Part 1 : ", previous_val)

    c_pos = positions[0]
    current_val = fuel_cost_p2(positions, positions[0])
    decrease = True
    while decrease:
        previous_val = current_val

        c_pos += 1
        current_val = fuel_cost_p2(positions, c_pos)

        if current_val > previous_val:
            decrease = False

    print("Part 2 : ", previous_val)

    print("Time %1.3es" % (time() - t0))
