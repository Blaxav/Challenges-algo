import os
import sys
import itertools
from math import factorial

def generate_solutions(permuts, portes, lettres) :
    print(permuts)
    nlv = len(permuts)
    perm = []
    cost = [0 for i in range(nlv)]

    pos = 0
    previous = ''
    for lv in range(nlv) :
        for l in permuts[lv] :
            if previous == '' :
                pos = 0 if not portes[l] else max( [perm.index(x) + 1 for x in portes[l] ] )
            else :
                pos = max( [perm.index(x) + 1 for x in portes[l] + [previous] ] )
            perm.insert(pos, l)
            previous = l
        previous = ''
    print(perm)


if __name__ == '__main__' :
    lettres = ['a','b','j','k','t']
    portes_names = ['a','b','k']

    portes = {'a' : [], 'b' : ['k','a'], 'j' : ['b'], 'k' : [], 't' : ['k']}

    levels = {}
    for x in lettres :
        levels[x] = -1

    cpt = len(lettres)
    lettres_restantes = lettres.copy()

    while cpt > 0 :
        for x in lettres_restantes :
            if len(portes[x]) == 0 :
                levels[x] = 0
                cpt += -1
                lettres_restantes.remove(x)
            else :
                if min( [levels[i] for i in portes[x]] ) > -1 :
                    levels[x] = min( [levels[i] for i in portes[x]] ) + 1
                    cpt += -1
                    lettres_restantes.remove(x)

    print(levels)
    max_lvl = max(levels.values() )

    levelSets = [[] for i in range(max_lvl+1)]
    costSets = [ 0 for i in range(max_lvl+1)]
    solSets = []

    best_sol = []
    best_cost = 0

    current_sol = []

    for x in lettres :
        levelSets[levels[x]].append(x)
    print("LEVEL SETS = ", levelSets)

    nbr_levels = max_lvl + 1
    increments = [0 for i in range(nbr_levels)]
    lvlSize = [ factorial(len(levelSets[i])) for i in range(nbr_levels) ]
    print("SIZES = ", lvlSize)
    print("PORTES = ", portes)

    gens    = [0 for i in range(nbr_levels)]
    res     = [0 for i in range(nbr_levels)]
    for k in range(nbr_levels) :
        gens[k] = itertools.permutations( levelSets[k] )
        res[k] = next(gens[k])

    stop = False
    while not stop :
        
        # 1. On genere toutes les permutations associees resultat courant
        generate_solutions(res, portes, lettres)

        # 2. on met a jour l'increment final avec retenue
        increments[-1] += 1
        ind = nbr_levels - 1
        while ( ind >= 0 and increments[ind] >= lvlSize[ind] ) :
            increments[ind] = 0
            increments[ind - 1] += 1
            ind -= 1

        # Si ind = -1, on a reinitialise le premier element, on est donc arrive au bout
        if ind == -1 :
            stop = True
        # Sinon l'indice est positif, il donne le dernier probleme non reinitialise
        else :
            # tous les reinitialises
            for k in range(nbr_levels-1, ind, -1 ) :
                ###############################################################
                ##################### reinitialiser l'iterateur ici
                gens[k] = itertools.permutations( levelSets[k] )
                res[k] = next(gens[k])
                ###############################################################
            # le dernier incremente (equivaut a next) (quand cest possible)
            res[ind] = next(gens[ind])




    exit()



    cpt = 0
    permut_lvl = [ itertools.permutations( levelSets[k] ) for k in range(max_lvl+1) ]
    stop = False
    while not stop :
        for k in range(max_lvl,-1,-1) :
            print( itertools.permutations( levelSets[k] ) )
