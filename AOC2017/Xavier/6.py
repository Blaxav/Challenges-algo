from sys import argv


def distrib(blocks):
    id = blocks.index(max(blocks))
    elems = blocks[id]
    blocks[id] = 0

    while elems > 0:
        id = (id + 1) if id + 1 < len(blocks) else 0
        blocks[id] += 1
        elems -= 1


if __name__ == '__main__':

    # Part 1
    instrucions = []
    input_data = open(argv[1], 'r')
    blocks = [int(i) for i in input_data.readline().rstrip('\n').split()]
    input_data.close()

    blocks_seen = []
    steps = 0
    while True:
        steps += 1
        distrib(blocks)
        if blocks not in blocks_seen:
            blocks_seen.append([i for i in blocks])
        else:
            break

    print("Part 1 : ", steps)
    print("Part 2 : ", len(blocks_seen) - blocks_seen.index(blocks))
