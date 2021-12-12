from sys import argv

codes = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

if __name__ == '__main__':

    screens = []
    outputs = []
    input_data = open(argv[1], 'r')
    for line in input_data:
        screens.append(["".join(sorted(e))
                       for e in line.rstrip('\n').split(' | ')[0].split()])
        outputs.append(["".join(sorted(e))
                       for e in line.rstrip('\n').split(' | ')[1].split()])
    input_data.close()

    total = 0
    for out in outputs:
        for val in out:
            if len(val) in [2, 3, 4, 7]:
                total += 1

    print("Part 1 : ", total)

    id = 0
    total = 0
    for screen in screens:
        nbr_use = {e: len([letter for letter in "".join(
            screen) if letter == e]) for e in "abcdefg"}

        # 4 : e
        # 6 : b
        # 7 : d or g
        # 8 : a or c
        # 9 : f
        candidates = {}
        for e in nbr_use:
            if nbr_use[e] == 9:
                candidates[e] = "f"
            elif nbr_use[e] == 4:
                candidates[e] = "e"
            elif nbr_use[e] == 6:
                candidates[e] = "b"
            elif nbr_use[e] == 8:
                # if in the output of len 2, it  is c
                if e in "".join([out for out in screen if len(out) == 2]):
                    candidates[e] = "c"
                else:
                    candidates[e] = "a"
            elif nbr_use[e] == 7:
                # if in the output of len 4, it  is d
                if e in "".join([out for out in screen if len(out) == 4]):
                    candidates[e] = "d"
                else:
                    candidates[e] = "g"

        # decode
        decode = dict(
            zip(screen, [codes["".join(sorted([candidates[e] for e in s]))] for s in screen]))

        total += int("".join([str(decode[e]) for e in outputs[id]]))

        id += 1

    print("Part 2 :", total)
