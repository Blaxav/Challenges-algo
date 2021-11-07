from sys import argv

if __name__ == '__main__':

    # Part 1
    instrucions = []
    input_data = open(argv[1], 'r')
    for instr in input_data:
        instrucions.append(int(instr.rstrip('\n')))
    input_data.close()

    # id of current instruction
    id = 0
    steps = 0

    while id < len(instrucions):
        steps += 1
        #print(steps, "  ", id, " -> ", id + instrucions[id])
        instrucions[id] += 1
        id += instrucions[id] - 1

    print("Part 1: ", steps)

    # Part 2
    instrucions = []
    input_data = open(argv[1], 'r')
    for instr in input_data:
        instrucions.append(int(instr.rstrip('\n')))
    input_data.close()

    # id of current instruction
    id = 0
    steps = 0

    while id < len(instrucions):
        steps += 1
        #print(steps, "  ", id, " -> ", id + instrucions[id])
        if instrucions[id] >= 3:
            instrucions[id] -= 1
            id += instrucions[id] + 1
        else:
            instrucions[id] += 1
            id += instrucions[id] - 1

    print("Part 2: ", steps)
