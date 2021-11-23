from sys import argv


def dance(programs, move):
    if move[0] == 's':
        programs = spin(programs, move)
    elif move[0] == 'x':
        exchange(programs, move)
    elif move[0] == 'p':
        partner(programs, move)
    else:
        print("ERROR : wrong dance move ", move)
    return programs


def spin(programs, move):
    n = int("".join(move[1:]))
    programs = programs[-n:] + programs[:-n]
    return programs


def exchange(programs, move):
    posA = int(move[1:].split("/")[0])
    posB = int(move[1:].split("/")[1])

    temp = programs[posA]
    programs[posA] = programs[posB]
    programs[posB] = temp


def partner(programs, move):
    eltA = move[1:].split("/")[0]
    posA = programs.index(eltA)

    eltB = move[1:].split("/")[1]
    posB = programs.index(eltB)

    temp = programs[posA]
    programs[posA] = programs[posB]
    programs[posB] = temp


if __name__ == '__main__':

    input_data = open(argv[1], 'r')
    moves = input_data.readline().rstrip('\n').split(',')
    input_data.close()

    programs = [c for c in "abcdefghijklmnop"]
    for move in moves:
        programs = dance(programs, move)

    print("Part 1 : ", "".join(programs))

    programs = [c for c in "abcdefghijklmnop"]
    all_progs = [programs[:]]

    N = 1000000000
    for k in range(N):

        for move in moves:
            programs = dance(programs, move)

        # Searching for a cycle, when we find the first state of programs, we can stop
        if programs == all_progs[0]:
            break

        all_progs.append(programs[:])

    print("Part 2 : ", "".join(all_progs[N % len(all_progs)]))
