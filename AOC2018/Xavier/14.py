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
    # Idea : starting from a 1 node, finding its 1 neighbors and setting it to 0
    # iterating until no neighbor is 1 : this is one block
    # going to the next 1 node
    print("Part 2 : ", path_finding_blocks(memory))
