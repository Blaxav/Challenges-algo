import sys
from collections import defaultdict
from itertools import permutations


def sits(people, relations):
    n_people = len(people)

    value = 0
    best_value = 0
    for plan in permutations(people[1:]):
        value = 0
        plan = [people[0]] + [i for i in plan]

        for i in range(n_people):
            personne = plan[i]
            voisin_gauche = plan[(i+1) % n_people]
            voisin_droite = plan[i-1]
            value += relations[personne][voisin_droite]
            value += relations[personne][voisin_gauche]

        if value > best_value:
            best_value = value
            print(plan, "  ", best_value)


if __name__ == '__main__':

    people = set()
    relations = defaultdict(dict)

    input_data = open(sys.argv[1], 'r')
    for line in input_data:
        people1 = line.split()[0]
        sign = 1 if line.split()[2] == "gain" else -1
        people2 = line.split()[-1][:-1]
        value = int(line.split()[3])

        people.add(people1)
        people.add(people2)

        relations[people1][people2] = sign * value

    # print(people)
    # print(relations)

    people = list(people)

    sits(people, relations)

    print("Part 2")

    for p in people:
        relations[p]["Xavier"] = 0
        relations["Xavier"][p] = 0
    people.append("Xavier")

    sits(people, relations)
