import sys
from collections import defaultdict


def apply(action, wires):
    if len(action[0].split()) == 1:
        if action[0] in wires:
            wires[action[1]] = int(wires[action[0]])
            return True
        elif action[0].isdigit():
            if action[1] == 'b':
                return True
            wires[action[1]] = int(action[0])
            return True
        else:
            return False
    # Not operator
    elif len(action[0].split()) == 2:
        if action[0].split()[1] in wires:
            wires[action[1]] = 65535 - wires[action[0].split()[1]]
            return True
        else:
            return False
    # Gates
    elif len(action[0].split()) == 3:
        if action[0].split()[0] in wires:
            a = wires[action[0].split()[0]]
        elif action[0].split()[0].isdigit():
            a = int(action[0].split()[0])
        else:
            return False

        if action[0].split()[2] in wires:
            b = wires[action[0].split()[2]]
        elif action[0].split()[2].isdigit():
            b = int(action[0].split()[2])
        else:
            return False

        operator = action[0].split()[1]
        if operator == "AND":
            wires[action[1]] = a & b
            return True
        elif operator == "OR":
            wires[action[1]] = a | b
            return True
        elif operator == "RSHIFT":
            wires[action[1]] = a >> b
            return True
        elif operator == "LSHIFT":
            wires[action[1]] = a << b
            return True

        #print(a, " ", operator, " ", b)
        return False
    else:
        return False


if __name__ == "__main__":

    wires = defaultdict(int)
    wires['b'] = 3176

    actions = []

    input_file = open(sys.argv[1], 'r')
    # saving all action as [what to do, whose to send]
    for instruction in input_file:
        actions.append([
            instruction.split(" -> ")[0],
            instruction.split(" -> ")[1].rstrip("\n")
        ])
    input_file.close()

    # index of remaining actions
    actions_to_remove = []
    while actions:
        print(len(actions))
        actions_to_remove = []
        for action in actions:
            # print(action)
            if apply(action, wires):
                actions_to_remove.append(action)

        for action in actions_to_remove:
            actions.remove(action)

    print("Result : ", wires['a'])

    ####################################################################################
    # PART 2
    ####################################################################################
    savedValue = wires['a']
    wires.clear()
    wires['b'] = savedValue

    input_file = open(sys.argv[1], 'r')
    # saving all action as [what to do, whose to send]
    for instruction in input_file:
        actions.append([
            instruction.split(" -> ")[0],
            instruction.split(" -> ")[1].rstrip("\n")
        ])
    input_file.close()
    actions_to_remove = []

    while actions:
        print(len(actions))
        actions_to_remove = []
        for action in actions:
            # print(action)
            if apply(action, wires):
                actions_to_remove.append(action)

        for action in actions_to_remove:
            actions.remove(action)

    print("Result : ", wires['a'])
