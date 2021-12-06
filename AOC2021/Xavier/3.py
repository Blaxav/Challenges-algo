from sys import argv


def compl(bits):
    return [(i+1) % 2 for i in bits]


def decimal(bits):
    return int(''.join([str(i) for i in bits]), 2)


def filter_most_common(numbers, sub_ids, index, val):
    '''
    Filters a sublist of binary numbers, keeping only those with the most common value 
    at a given index. In case of equality, val is used as most common
    Returns the list of indices to keep in the list, the list itself is not modified
    '''
    keep_ids = []
    zeros = [i for i in range(len(numbers)) if numbers[i]
             [index] == 0 and i in sub_ids]
    ones = [i for i in range(len(numbers)) if numbers[i]
            [index] == 1 and i in sub_ids]

    if (len(ones) > len(sub_ids) / 2) or (val == 1 and len(ones) == len(sub_ids) / 2):
        return ones
    elif len(ones) < len(sub_ids) / 2 or (val == 0 and len(ones) == len(sub_ids) / 2):
        return zeros
    else:
        print("ERROR equality val not 0 or 1")


def filter_least_common(numbers, sub_ids, index, val):
    keep_ids = []
    zeros = [i for i in range(len(numbers)) if numbers[i]
             [index] == 0 and i in sub_ids]
    ones = [i for i in range(len(numbers)) if numbers[i]
            [index] == 1 and i in sub_ids]

    if (len(ones) < len(sub_ids) / 2) or (val == 1 and len(ones) == len(sub_ids) / 2):
        return ones
    elif len(ones) > len(sub_ids) / 2 or (val == 0 and len(ones) == len(sub_ids) / 2):
        return zeros
    else:
        print("ERROR equality val not 0 or 1")


if __name__ == '__main__':

    bits = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        bits.append([int(i) for i in line.rstrip("\n")])
    input_data.close()

    # epsilon is the complementary of gamma
    # only needs to count the ones
    # done by verifying if the sum of elements if larger than half the length
    gamma = [0]*len(bits[0])
    for j in range(len(bits[0])):
        if sum([b[j] for b in bits]) == len(bits)/2:
            print("ERROR : equality between ones and zeros")
        elif sum([b[j] for b in bits]) > len(bits)/2:
            gamma[j] = 1

    print("Part 1 : ", decimal(gamma) * decimal(compl(gamma)))

    index = 0
    oxygen_ids = [i for i in range(len(bits))]
    while len(oxygen_ids) > 1:
        oxygen_ids = filter_most_common(bits, oxygen_ids, index, 1)
        index += 1

    index = 0
    co2_ids = [i for i in range(len(bits))]
    while len(co2_ids) > 1:
        co2_ids = filter_least_common(bits, co2_ids, index, 0)
        index += 1

    print("Part 2 : ", decimal(
        bits[oxygen_ids[0]]) * decimal(bits[co2_ids[0]]))
