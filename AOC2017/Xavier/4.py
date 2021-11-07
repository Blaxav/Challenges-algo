from sys import argv

if __name__ == '__main__':

    words = []
    anagrams = []
    total = 0
    totalP2 = 0
    valid = True
    validP2 = True

    input_data = open(argv[1], 'r')
    for line in input_data:
        words.clear()
        anagrams.clear()
        valid = True
        validP2 = True

        passphrase = line.rstrip('\n').split()
        # Part 1
        for w in passphrase:
            if w not in words:
                words.append(w)
            else:
                valid = False
                break
        if valid:
            total += 1

        # Part 2
        for w in passphrase:
            if "".join(sorted(w)) not in anagrams:
                anagrams.append("".join(sorted(w)))
            else:
                validP2 = False
                break
        if validP2:
            totalP2 += 1

    print("Part1: ", total)
    print("Part2: ", totalP2)
