from sys import argv

datas = []
input_data = open(argv[1], 'r')
for line in input_data:
    datas.append((line.rstrip('\n').split()[
                 0], int(line.rstrip('\n').split()[1])))
input_data.close()

pos = [0, 0]
for (move, val) in datas:
    if move == "forward":
        pos[0] += val
    elif move == "down":
        pos[1] += val
    elif move == "up":
        pos[1] -= val
    else:
        print("ERROR")
        exit()

print("Part 1 : ", pos, "  ", pos[0]*pos[1])


pos = [0, 0]
aim = 0
for (move, val) in datas:
    if move == "forward":
        pos[0] += val
        pos[1] += val*aim
    elif move == "down":
        aim += val
    elif move == "up":
        aim -= val
    else:
        print("ERROR")
        exit()

print("Part 2 : ", pos, "  ", pos[0]*pos[1])
