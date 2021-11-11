from functools import reduce
from sys import argv


def rotate(l, n):
    return l[n:] + l[:n]


def convert_to_ascii(data):

    final_data = []
    for character in data:
        final_data.append(ord(character))
    return final_data


def add_suffix(data):
    return data + [17, 31, 73, 47, 23]


def twist(numbers, length, c_pos):
    # 1. rotate to have c_pos at id 0
    numbers = rotate(numbers, c_pos)
    # 2. twist
    numbers = numbers[:length][::-1] + numbers[length:]
    # 3. rotate back
    numbers = rotate(numbers, -c_pos)
    return numbers


def run_hash(numbers, twists, c_pos, skip_size):
    N = len(numbers)

    for length in twists:
        numbers = twist(numbers, length, c_pos)
        c_pos = (c_pos + length + skip_size) % N
        skip_size += 1

    return (numbers, c_pos, skip_size)


if __name__ == '__main__':

    # Part 1
    input_data = open(argv[1], 'r')
    twists = [int(i)
              for i in input_data.readline().rstrip('\n').split(',')]
    input_data.close()

    N = int(argv[2])
    c_pos = 0
    skip_size = 0
    numbers = list(range(N))

    numbers, c_pos, skip_size = run_hash(numbers, twists, c_pos, skip_size)
    print("Part 1 ", numbers[0]*numbers[1])

    #########################################################
    # Part 2
    #########################################################

    input_data = open(argv[1], 'r')
    data = input_data.readline().rstrip('\n')
    input_data.close()
    data = ""
    data = convert_to_ascii(data)
    data = add_suffix(data)
    print(data)

    c_pos = 0
    skip_size = 0

    repeat = 64
    numbers = list(range(N))
    for k in range(repeat):
        numbers, c_pos, skip_size = run_hash(numbers, data, c_pos, skip_size)

    dense_hash = []
    for k in range(16):
        total = numbers[16*k] ^ numbers[16*k + 1]
        for j in range(16*k + 2, 16*(k+1)):
            total ^= numbers[j]
        dense_hash.append(total)

    print(dense_hash)

    result = ''
    for t in dense_hash:
        hexa = hex(t)[2:]
        if len(hexa) == 1:
            hexa = "0" + hexa
        result += hexa

    print(result)
