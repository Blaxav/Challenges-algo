from sys import argv


def compl(bits):
    return [(i+1) % 2 for i in bits]


def decimal(bits):
    return int(''.join([str(i) for i in bits]), 2)


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
