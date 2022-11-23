from sys import argv

if __name__ == '__main__':

    relations = {}
    input_data = open(argv[1], 'r')
    for line in input_data:
        relations[int(line.split()[0])] = [int(i.rstrip(','))
                                           for i in line.rstrip('\n').split()[2:]]
    input_data.close()

    all_programs = [r for r in relations]
    reachables = set([0])
    to_see = [0]
    while to_see:
        c_prog = to_see[0]
        to_see = to_see[1:]
        for neigh in relations[c_prog]:
            if neigh not in reachables:
                reachables.add(neigh)
                to_see.append(neigh)

    print("Part 1 : ", len(reachables))

    counter = 0
    while all_programs:
        counter += 1
        reachables = set([all_programs[0]])
        to_see.append(all_programs[0])
        while to_see:
            c_prog = to_see[0]
            to_see = to_see[1:]
            for neigh in relations[c_prog]:
                if neigh not in reachables:
                    reachables.add(neigh)
                    to_see.append(neigh)
        print(reachables)
        all_programs = list(set(all_programs) - reachables)

    print("Part 2 : ", counter)
