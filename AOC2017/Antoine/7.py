from time import time
from collections import defaultdict
import unittest
a = time()

def readFile():
    # On renvoie le fichier d'entrée sous forme d'une liste de string
    with open(__file__[:-3] + "-" + "input.txt", "r") as f:
        return [i.strip().replace(',', '').split() for i in f.readlines()]

def parse_scheme(scheme: list):
    result_dict = dict()
    for elem in scheme:
        result_dict[elem[0]] = {'weight': int(elem[1][1:-1])}
        if len(elem) > 2:
            result_dict[elem[0]]['sons'] = elem[3:]
    
    return result_dict
            
def part1(scheme: dict):
    elems_with_parents = list(set([son for elem in scheme.values() if 'sons' in elem for son in elem['sons'] ]))
    for elem in scheme:
        if elem not in elems_with_parents:
            return elem

def calculate_weight(scheme: dict, elem: str):
    if 'sons' not in scheme[elem]:
        return scheme[elem]['weight']
    else:
        return scheme[elem]['weight'] + sum(calculate_weight(scheme, son) for son in scheme[elem]['sons'])

def part2(scheme: dict, first_elem: str):
    sons_weight, weight_occurences = {k: {'own_weight': scheme[k]['weight'], 'total_weight': 0} for k in scheme[first_elem]['sons']}, defaultdict(int)
    for elem in scheme[first_elem]['sons']:
        sons_weight[elem]['total_weight'] = calculate_weight(scheme, elem)
        weight_occurences[sons_weight[elem]['total_weight']] += 1
    branch_weights = [min(weight_occurences, key=weight_occurences.get), max(weight_occurences, key=weight_occurences.get)]
    while len(list(set(branch_weights))) != 1:
        for elem, weight in sons_weight.items():
            if weight['total_weight'] == branch_weights[0]:
                unbalanced_elem, unbalanced_weights = elem, branch_weights
                sons_weight, weight_occurences = {k: {'own_weight': scheme[k]['weight'], 'total_weight': 0} for k in scheme[elem]['sons']}, defaultdict(int)
                for son in scheme[elem]['sons']:
                    sons_weight[son]['total_weight'] = calculate_weight(scheme, son)
                    weight_occurences[sons_weight[son]['total_weight']] += 1
                branch_weights = [min(weight_occurences, key=weight_occurences.get), max(weight_occurences, key=weight_occurences.get)]

    return scheme[unbalanced_elem]['weight'] - unbalanced_weights[0] + unbalanced_weights[1]

class Tests(unittest.TestCase):

    def testP1(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    scheme = parse_scheme(readFile())
    p1 = part1(scheme)
    print(f"Part 1: {p1}")
    p2 = part2(scheme, p1)
    print(f"Part 2: {p2}")
    print(time()-a)

