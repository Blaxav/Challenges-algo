import sys


def apply(action, first, last, data):
    if action == "toggle":
        toggle(first, last, data)
    elif action == "turnon":
        turn_on(first, last, data)
    elif action == "turnoff":
        turn_off(first, last, data)
    else:
        print("ERROR Unknown action : ", action)


def toggle(first, last, data):
    for line in range(first[0], last[0] + 1):
        for column in range(first[1], last[1] + 1):
            data[line][column] = (data[line][column] + 1) % 2


def turn_on(first, last, data):
    for line in range(first[0], last[0] + 1):
        data[line][first[1]:last[1]+1] = [1]*(last[1] - first[1] + 1)


def turn_off(first, last, data):
    for line in range(first[0], last[0] + 1):
        data[line][first[1]:last[1]+1] = [0]*(last[1] - first[1] + 1)


def apply2(action, first, last, data):
    bright_diff = 0
    if action == "toggle":
        bright_diff = 2
    elif action == "turnon":
        bright_diff = 1
    elif action == "turnoff":
        bright_diff = -1
    else:
        print("ERROR Unknown action : ", action)

    for line in range(first[0], last[0] + 1):
        for column in range(first[1], last[1] + 1):
            data[line][column] = max(0, data[line][column] + bright_diff)


def toggle2(first, last, data):
    for line in range(first[0], last[0] + 1):
        for column in range(first[1], last[1] + 1):
            data[line][column] += 2


def turn_on2(first, last, data):
    for line in range(first[0], last[0] + 1):
        for column in range(first[1], last[1] + 1):
            data[line][column] += 2


def turn_off2(first, last, data):
    for line in range(first[0], last[0] + 1):
        data[line][first[1]:last[1]+1] = [0]*(last[1] - first[1] + 1)


if __name__ == '__main__':

    input_file = open(sys.argv[1], 'r')

    n = 1000
    data = []
    data2 = []
    for i in range(n):
        data.append([0] * n)
        data2.append([0] * n)

    action = ""
    first = (0, 0)
    last = (0, 0)
    for instruction in input_file:
        instruction = instruction.replace('turn on', 'turnon')
        instruction = instruction.replace('turn off', 'turnoff')
        action = instruction.split()[0]

        first = (int(instruction.split()[1].split(',')[0]),
                 int(instruction.split()[1].split(',')[1]))
        last = (int(instruction.split()[3].split(',')[0]),
                int(instruction.split()[3].split(',')[1]))

        apply(action, first, last, data)
        apply2(action, first, last, data2)
        #print(action, first, last, sum([sum(data[i]) for i in range(n)]))

    # checking result
    total = sum([sum(data[i]) for i in range(n)])
    print("Total lit : ", total)

    print("Total part 2 : ", sum([sum(data2[i]) for i in range(n)]))
