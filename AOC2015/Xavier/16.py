import sys

if __name__ == '__main__':

    aunts = []
    current_aunt = {}

    input_data = open(sys.argv[1], 'r')
    for line in input_data:
        current_aunt.clear()

        aunt_possessions = [i.rstrip(':').rstrip(',')
                            for i in line.split()]
        for i in range(0, len(aunt_possessions), 2):
            current_aunt[aunt_possessions[i]] = aunt_possessions[i+1]

        aunts.append(current_aunt.copy())

    searched_sue = {
        'children': '3',
        'cats': '7',
        'samoyeds': '2',
        'pomeranians': '3',
        'akitas': '0',
        'vizslas': '0',
        'goldfish': '5',
        'trees': '3',
        'cars': '2',
        'perfumes': '1'
    }

    greaters = ['cats', 'trees']
    smallers = ['pomeranians', 'goldfish']

    possible_sue = True
    for sue in aunts:
        possible_sue = True
        for poss in sue:
            if poss in searched_sue:
                if poss in greaters and searched_sue[poss] < sue[poss]:
                    print("G ", sue)
                    possible_sue = False
                    break
                elif poss in smallers and searched_sue[poss] > sue[poss]:
                    print("L ", sue)
                    possible_sue = False
                    break
                elif searched_sue[poss] != sue[poss]:
                    possible_sue = False
                    break

        if possible_sue:
            print("Final sue : ", sue)
