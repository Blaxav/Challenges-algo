import os
import re
import sys
from collections import defaultdict, deque

class Node :
    def __init__(self, val, prof) :
        self.val = val
        self.prof = prof

def generate_all_sons(cnode, nodes, transfo, resultat) :

    result = set()

    for reac in transfo :
        for prod in transfo[reac] :
            taille = len(reac)
            for ind in (m.start() for m in re.finditer(reac, cnode.val)) :
                retour = cnode.val[:ind] + prod + cnode.val[ind+taille:]
                
                if len(retour) <= len(resultat) :
                    if retour == resultat :
                        print("ICI ", cnode.prof + 1)
                        #exit()
                    else :
                        result.add(retour)
    
    for i in result :
        nodes.append( Node(i, cnode.prof + 1) )

def generate_inverse(cnode, nodes, transfo) :

    resultat = "e"

    for reac in transfo :
        for prod in transfo[reac] :
            taille = len(reac)
            for ind in (m.start() for m in re.finditer(reac, cnode.val)) :
                retour = cnode.val[:ind] + prod + cnode.val[ind+taille:]

                if retour == resultat :
                    print("ICI ", cnode.prof + 1)
                else :
                    result.add(retour)
    
    for i in result :
        nodes.append( Node(i, cnode.prof + 1) )



if __name__ == '__main__' :
    input = open("input19.txt", 'r')

    transfo = defaultdict(lambda : [])
    transfoInverse = defaultdict(lambda : [])
    result = set()

    for line in input :
        if len(line) > 0 :
            if "=>" in line :
                line = line.rstrip()
                reac = line.split("=>")[0].split()[0]
                prod = line.split("=>")[-1].split()[-1]
                transfo[reac].append(prod)
                transfoInverse[prod].append(reac)
            
            else :
                molecule = line

    print(transfo)

    for reac in transfo :
        for prod in transfo[reac] :
            #print( [m.start() for m in re.finditer(reac, molecule)] )
            taille = len(reac)
            for ind in (m.start() for m in re.finditer(reac, molecule)) :
                retour = molecule[:ind] + prod + molecule[ind+taille:]
                result.add(retour)
                #print(retour)

    print(len(result))

    #part 2

    nodes = deque()
    nodes.append( Node(molecule,0) )

    cnt = 0

    status = [0]
    sons = []
    val = "e"
    new_stage = True

    while status[0] == 0 :

        # 1. calculer nombre de fils possibles
        if new_stage :

            for reac in transfo :
                for prod in transfo[reac] :
                    taille = len(reac)
                    for ind in (m.start() for m in re.finditer(reac, cnode.val)) :
                        retour = val[:ind] + prod + val[ind+taille:]

                        if len(retour) <= len(molecule) :
                            if retour == resultat :
                                print("ICI ", cnode.prof + 1)
                            else :
                                result.add(retour)
            sons.append( len(result) )
            
            # on ajoute le premier fils
            status.append(0)



        


