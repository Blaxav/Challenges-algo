# A python module named with an int cannot be imported
from collections import deque

hash = __import__('10')


def hex_to_bin(hex):
    '''
    Convert one hexadecimal character to a 4 bits binary
    '''
    binary = bin(int(hex, 16))[2:]
    binary = [0] * (4 - len(binary)) + [int(i) for i in binary]
    return binary


def hash_to_binary(hash):
    '''
    Convert a hash (a string of hexadecimal characters) to a binary
    '''
    result = []
    for hex in hash:
        result += hex_to_bin(hex)
    return result


class Block_line:
    def __init__(self, row, beg, end):
        self.row = row
        self.beg = beg
        self.end = end


class Region:
    '''
    Region : defines a list of Blocks lines contiguous to each other
    '''

    def __init__(self, blocks):
        self.blocks = blocks


def neighbors(node):
    if node[0] < 127:
        yield (node[0] + 1, node[1])
    if node[0] > 0:
        yield (node[0] - 1, node[1])
    if node[1] < 127:
        yield (node[0], node[1] + 1)
    if node[1] > 0:
        yield (node[0], node[1] - 1)


def path_finding_blocks(memory):
    i = 0
    j = 0
    open_node = deque()
    block_coutner = 0
    while i < 128:
        if j == 128:
            i += 1
            j = 0
        else:
            if memory[i][j] == 1:
                block_coutner += 1
                # print(block_coutner)
                # Begining the block search
                open_node.clear()
                open_node.append((i, j))
                while open_node:
                    node = open_node.popleft()
                    memory[node[0]][node[1]] = 0

                    for (k, p) in neighbors(node):
                        if memory[k][p] == 1:
                            open_node.append((k, p))

            j += 1
    return block_coutner


if __name__ == '__main__':

    # My input
    data = "hfdlxzhv"

    # Example
    data_ex = "flqrgnkx"

    total = 0
    memory = []
    for k in range(128):
        memory.append(hash_to_binary(hash.knot_hash(data + '-' + str(k), 256)))
        total += sum(memory[-1])
    print("Part 1 : ", total)

    # Part 2
    # idea : Create the contiguous regions on each line, and then aggergate them by rows
    # a region is made of two indices [i,j)
    regions = deque()
    line_cnt = 0
    for line in memory:
        id = 0
        regions.append([])
        while id < len(line):
            if line[id] == 1:
                beg = id
                while id < len(line) and line[id] == 1:
                    id += 1
                regions.append(Region([Block_line(line_cnt, beg, id)]))
            else:
                id += 1

        line_cnt += 1

    print("Part 2 : ", path_finding_blocks(memory))
