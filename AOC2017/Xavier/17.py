from sys import argv

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

    print("Part 1 : ", buffer[buffer.index(2017) + 1])

    N = 50000000
    buffer = [0]*N
    pos = 0
    for k in range(1, N + 1):
        id = (pos + step) % k + 1
        buffer = buffer[:id] + [k] + buffer[id:]
        pos = id % k
        if k % 1000 == 0:
            print(k)

    print("Part 2 : ", buffer[buffer.index(0) + 1])
