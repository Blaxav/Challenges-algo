import sys
from collections import defaultdict
from itertools import permutations


def longueur(chaine, arcs):
    total = 0
    for i in range(len(chaine) - 1):
        total += arcs[(chaine[i], chaine[i+1])]
    return total


def compute_chaine(new, i, j, chaine, arc):
    # returns the chain inserting new between index i and j and revert as needed
    print("coucou")


def insert(new, chaine, arcs):
    print("INSERT ", new, "  in ", chaine)
    # In first position
    new_chaine = [new] + [i for i in chaine]
    new_length = longueur(new_chaine, arcs)
    print("    ", new_chaine, " ", new_length)

    # In last position
    if longueur(chaine + [new], arcs) < new_length:
        new_chaine = chaine + [new]
        new_length = longueur(chaine + [new], arcs)
        print("    ", new_chaine, " ", new_length)


if __name__ == '__main__':

    # dict of dict {city1 : {city2 : dist1, city3 : dist 2, ...}, city2 : {...}}
    distances = defaultdict(dict)
    arcs = {}
    vertex = set()

    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        city1 = line.split()[0]
        city2 = line.split()[2]
        dist = line.split()[4]

        distances[city1][city2] = dist
        distances[city2][city1] = dist

        arcs[(city1, city2)] = int(dist)
        arcs[(city2, city1)] = int(dist)

        vertex.add(city1)
        vertex.add(city2)

    log_level = 0
    if log_level > 0:
        for c in distances:
            for d in distances[c]:
                print(c, "  -> ", d, " = ", distances[c][d])

    vertex = [i for i in vertex]
    # A chaque iteration on ajoute un sommet
    chaine = []
    longueur_chaine = 1e9

    chaine = [vertex[0], vertex[1]]
    longueur_chaine = longueur(chaine, arcs)

    best_value = longueur(vertex, arcs)
    best_chaine = vertex
    print("Chaine itit : ", vertex, "  ", best_value)
    for chemin in permutations(vertex):
        if longueur(chemin, arcs) > best_value:
            best_chaine = chemin
            best_value = longueur(chemin, arcs)
            print("Chaine      : ", chemin, "  ", best_value)
