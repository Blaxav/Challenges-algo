import os
import sys
import itertools
from math import factorial

listes = [[1,3], [0,1,2], [1,2,3]]
nbr_levels = len(listes)
increments = [0 for i in range(nbr_levels)]

gens    = [0 for i in range(len(listes))]
res     = [0 for i in range(len(listes))]
for k in range(len(listes)) :
    gens[k] = (i for i in listes[k])
    res[k] = next(gens[k])

stop = False
while not stop :
    
    # 1. resultat courant
    print(res)

    # 2. on met a jour l'increment final avec retenue
    increments[-1] += 1
    ind = nbr_levels - 1
    while ( ind >= 0 and increments[ind] >= len(listes[ind]) ) :
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
            gens[k] = (i for i in listes[k])
            res[k] = next(gens[k])
            ###############################################################
        # le dernier incremente (equivaut a next)
        res[ind] = next(gens[ind])