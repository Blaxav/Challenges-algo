from sys import argv


def rotate(l, n):
    return l[n:] + l[:n]


def twist(numbers, length, c_pos):
    # 1. rotate to have c_pos at id 0
    numbers = rotate(numbers, c_pos)
    # 2. twist
    numbers = numbers[:length][::-1] + numbers[length:]
    # 3. rotate back
    numbers = rotate(numbers, -c_pos)
    return numbers


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
    for length in twists:
        numbers = twist(numbers, length, c_pos)
        c_pos = (c_pos + length + skip_size) % N
        skip_size += 1
        #print(numbers, " c_pos = ", c_pos, " skip = ", skip_size)

    print("Part 1 ", numbers[0]*numbers[1])
