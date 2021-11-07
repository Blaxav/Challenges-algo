import sys
from collections import defaultdict


def moove_position(position, moove):
    if moove == '^':
        return (position[0], position[1] + 1)
    elif moove == 'v':
        return (position[0], position[1] - 1)
    elif moove == '>':
        return (position[0] + 1, position[1])
    elif moove == '<':
        return (position[0] - 1, position[1])
    else:
        print("Error, ", moove, " is not a valid moove.")


if __name__ == "__main__":
    input_file = open(sys.argv[1], 'r')
    line = input_file.readline()
    input_file.close()

    # Dictionnary of positions (x,y) -> Number of presents
    houses = defaultdict(int)

    position = (0, 0)
    houses[position] += 1

    for moove in line:
        position = moove_position(position, moove)
        houses[position] += 1

    print("Number of houses with a present : ", len(houses))

    housesY2 = defaultdict(int)
    positionSanta = (0, 0)
    positionRobot = (0, 0)

    housesY2[positionSanta] += 1
    housesY2[positionRobot] += 1
    #print(0, " ", positionSanta, "  ", positionRobot, " ", housesY2)

    for k in range(len(line)):
        moove = line[k]
        if k % 2 == 0:
            positionSanta = moove_position(positionSanta, moove)
            housesY2[positionSanta] += 1
        else:
            positionRobot = moove_position(positionRobot, moove)
            housesY2[positionRobot] += 1
        #print(k, " ", positionSanta, "  ", positionRobot, " ", housesY2)

    print("Number of houses with a present : ", len(housesY2))
