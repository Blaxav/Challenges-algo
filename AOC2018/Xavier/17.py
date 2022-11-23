from sys import argv


def algo_list(N, searched_value, step):
    buffer = [0]

    pos = 0
    for k in range(1, N):
        #print((pos, step, k, (pos + step) % k), (pos + step) % k + 1)
        id = (pos + step) % k + 1
        buffer.insert(id, k)
        pos = id
        # print(buffer[k])
        if k % 500000 == 0:
            print(k)

    return buffer[buffer.index(searched_value) + 1]


def part2(N, step):
    '''
    The algorithm never insert before 0, then 0 stays at index 0 during all the process
    Searching the value after 0 is equivalent to search the last value inserted at 
    index 1, no buffer is needed
    '''
    pos = 0
    result = -1
    for k in range(1, N):
        id = (pos + step) % k + 1
        if id == 1:
            result = k
        pos = id

    return result


if __name__ == '__main__':

    if len(argv) < 2:
        print("Usage : sys.argv[1] == step_size")
        exit()
    else:
        step = int(argv[1])

    buffer = [0]
    pos = 0
    for k in range(1, 2018):
        id = (pos + step) % len(buffer) + 1
        buffer = buffer[:id] + [k] + buffer[id:]
        pos = id % len(buffer)

    print("Exemple : ", algo_list(2018, 2017, 3))
    print("Part 1 : ", algo_list(2018, 2017, step))
    print("Part 2 : ", part2(int(5e7+1), step))
