from collections import defaultdict
from operator import itemgetter
from sys import argv

if __name__ == '__main__':

    first_part = True
    molecule = ""
    template = {}
    pairs_counter = defaultdict(int)
    letters = defaultdict(int)

    input_data = open(argv[1], 'r')
    for line in input_data:
        if line == "\n":
            first_part = False
        elif first_part:
            molecule = line.rstrip("\n")
            for k in range(len(molecule) - 1):
                pairs_counter[molecule[k:k+2]] += 1
        else:
            template[line.split(" -> ")[0]
                     ] = line.rstrip("\n").split(" -> ")[1]
    input_data.close()

    n_steps = 40

    # saving initial and final atom for counting
    init = molecule[0]
    final = molecule[-1]

    # To appear count for each pair of letters the number to appear next iteration
    to_appear = defaultdict(int)
    for k in range(n_steps):
        to_appear.clear()
        for pair in pairs_counter:
            # Creating new pairs
            if pair in template:
                to_appear[pair[0] + template[pair]] += pairs_counter[pair]
                to_appear[template[pair] + pair[1]] += pairs_counter[pair]
                # Setting back to 0 as those pairs created new ones
                pairs_counter[pair] = 0

        # Adding the new pairs of letters in molecule
        for pair in to_appear:
            pairs_counter[pair] += to_appear[pair]

        # Counting letters from pairs, with a different way for first and last letter
        letters.clear()
        for pair in pairs_counter:
            letters[pair[0]] += pairs_counter[pair]
            letters[pair[1]] += pairs_counter[pair]
        letters[init] += 1
        letters[final] += 1
        for l in letters:
            letters[l] = int(letters[l] / 2)

        if k == 9:
            print("Part 1 : ", max(letters.values()) - min(letters.values()))

    print("Part 2 : ", max(letters.values()) - min(letters.values()))
