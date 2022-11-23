from sys import argv

if __name__ == '__main__':

    table = []

    input_data = open(argv[1], 'r')
    for line in input_data:
        table.append([int(i) for i in line.rstrip('\n').split()])

    print("Part 1 : ", sum([max(t) - min(t) for t in table]))

    table = [sorted(t)[::-1] for t in table]

    total = 0
    found = False
    for t in table:
        found = False
        id = 0
        while not found:
            for j in range(id + 1, len(t)):
                if int(t[id] / t[j]) == t[id] / t[j]:
                    total += int(t[id] / t[j])
                    found = True
                    #print(t[id], "  ", t[j], "  ", t[id] / t[j], "  ", total)
                    break
            id += 1

    print("Part 2 : ", total)
