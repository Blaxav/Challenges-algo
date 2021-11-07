import sys
from os import sep


def next(separators, n_portions):
    id = len(separators) - 2

    while id > 0 and separators[id] == n_portions:
        id -= 1

    separators[id] = separators[id] + 1
    for i in range(id + 1, len(separators)-1):
        separators[i] = separators[id]


def display(separators, n_portions):
    sep_id = 0
    for i in range(n_portions):
        while sep_id < len(separators) and separators[sep_id] == i:
            print('|', end="")
            sep_id += 1
        print('*', end='')

    for i in range(sep_id, len(separators)):
        print('|', end='')
    print()


def compute_value(separators, n_portions, ingredients):
    results = [0] * 5
    for i in range(1, 6):
        for j in range(len(separators) - 1):
            portions_ingredient = separators[j+1] - separators[j]
            results[i-1] += portions_ingredient * ingredients[j][i]

    results = [max([0, i]) for i in results]

    total = 1
    for e in results[:-1]:
        total *= e

    # test calories
    if results[-1] != 500:
        total = 0

    return total


if __name__ == '__main__':

    ingredients = []
    input_data = open(sys.argv[1], 'r')
    for line in input_data:
        name = line.split(':')[0]
        ingredients.append([name])
        for id_line in [2, 4, 6, 8, 10]:
            ingredients[-1].append(int(line.split()[id_line].rstrip(',')))

    n_portions = 100
    separators = [0] * len(ingredients)
    separators.append(n_portions)

    print(ingredients)

    best_value = 0
    while separators[1] < 100:
        if compute_value(separators, n_portions, ingredients) > best_value:
            best_value = compute_value(separators, n_portions, ingredients)
            print(best_value, "  ", separators)
        next(separators, n_portions)
