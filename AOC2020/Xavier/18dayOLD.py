import os
import sys
import time
import datetime
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot
from string import ascii_lowercase, ascii_uppercase
from collections import deque


import cProfile, io, pstats, os, sys
def doprofile(func, filename, *l):
    pr = cProfile.Profile()
    pr.enable()  # début du profiling
    func(*l)     # appel de la fonction
    pr.disable() # fin du profiling
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    rem = os.path.normpath(os.path.join(os.getcwd(), "..", "..", ".."))
    res = s.getvalue().replace(rem, "")
    res = res.replace(sys.base_prefix, "").replace("\\", "/")
    ps.dump_stats(filename)
    return res


def find_nodes(nodes, instance) :
    file = open(instance, 'r')
    
    # on retient les deux lignes precedentes
    # un noeud de la ligne l_1 est un noeud de branchement si
    l_1 = ""
    l_2 = ""

    # longueur d'une ligne
    size = 0
    crsm_ind = 0
    row = 0
    col = 0
    for line in file :
        size = len( line.rstrip() )
        for elt in line.rstrip() :
            # 1. coordonnees des lettres maj comme min
            if elt not in  ['.','#'] :
                nodes[elt] = [row, col]
            # 2. les noeuds de branchement
            if ( row >= 2 and  0 < col < size-1 ) :
                if l_1[col] != '#' and (  int( l_1[col - 1] != '#' )\
                                        + int( l_1[col + 1]  != '#')\
                                        + int( line.rstrip()[col]  != '#') \
                                        + int( l_2[col]  != '#')) >= 3 :
                    if l_1[col] == '.' :
                         nodes[crsm_ind] = [row-1, col]
                         crsm_ind += 1
                    #print("coisement ", row_cnt-1, col_cnt)
            col += 1
        l_2 = l_1
        l_1 = line.rstrip()
        row += 1
        col = 0
    
    file.close()

def find_key(n,m,nodes) :
    for k in nodes.keys() :
        if nodes[k] == [n,m] :
            return k
    print("ERROR NO KEY AT THOSE COORDINATES")
    return -1

def find_neighboors_and_graph_distances(nodes, voisins, distances, instance) :
    chemins_ouverts = {}

    file = open(instance, 'r')

    lines = [l.rstrip() for l in file.readlines()]
    dist = 1

    for node in nodes :
        n = nodes[node][0]
        m = nodes[node][1]
        #1. creer les chemins (nombre de pas # autour)
        chemins_ouverts[node] = []
        if lines[n+1][m] != '#' :
            chemins_ouverts[node].append([n+1,m,'H'])
        if lines[n-1][m] != '#' :
            chemins_ouverts[node].append([n-1,m,'B'])
        if lines[n][m+1] != '#' :
            chemins_ouverts[node].append([n,m+1,'G'])
        if lines[n][m-1] != '#' :
            chemins_ouverts[node].append([n,m-1,'D'])

        #2. faire avancer chaque chemin jusqua trouver une cle
        while node in chemins_ouverts.keys() :
            #print('coucou', chemins_ouverts[node])
            [n,m,last] = chemins_ouverts[node][0]
            # on trouve le voisin
            if [n,m] in nodes.values() : 
                voisins[node].append( find_key(n,m,nodes) )
                distances[node][find_key(n,m,nodes)] = dist
                dist = 1
                # on supprime le chemin en cours
                if len(chemins_ouverts[node]) > 1 :
                    chemins_ouverts[node] = chemins_ouverts[node][1:]
                else :
                    del chemins_ouverts[node]
            else :
                dist += 1
                if lines[n+1][m] != '#' and last != 'B' :
                    chemins_ouverts[node][0] = ([n+1,m,'H'])
                elif lines[n-1][m] != '#' and last != 'H' :
                    chemins_ouverts[node][0] = ([n-1,m,'B'])
                elif lines[n][m+1] != '#' and last != 'D' :
                    chemins_ouverts[node][0] = ([n,m+1,'G'])
                elif lines[n][m-1] != '#' and last != 'G' :
                    chemins_ouverts[node][0] = ([n,m-1,'D'])
                else :
                    #CUL DE SAC

                    dist = 1
                    if len(chemins_ouverts[node]) > 1 :
                        chemins_ouverts[node] = chemins_ouverts[node][1:]
                    else :
                        del chemins_ouverts[node]

def draw_graph(nodes, voisins) :
    G = nx.Graph()
    G.add_nodes_from(nodes.keys())
    for node in nodes :
        for v in voisins[node] :
            G.add_edge(node, v)

    nx.draw(G, pos=nodes, with_labels=True, )
    plt.savefig("graph.png")

def dijkstra(nodes, voisins, distances, dist_mat, portes) :

    alphabet = [i for i in ascii_lowercase]
    keys = [i for i in nodes.keys() if i in alphabet]

    keys.insert(0, '@')

    for v in keys :
        for j in [z for z in keys if z != v] :
            dist_mat[(v,j)] = -1
            dist_mat[(j,v)] = -1
        portes[v] = []
    
    dist_from_key = {}
    current_key = ''
    
    seen_keys       = []
    remaining_keys  = []

    for v in nodes.keys() :
        portes[v] = []

    for k in keys :

        if [v for v in keys if ( v != k and dist_mat[(k,v)] == -1 )] :

            # 1. reinitialisation du dictionnaire
            for i in nodes.keys() :
                dist_from_key[i] = 1e6
            
            remaining_keys = [i for i in nodes.keys() if i != k]
            seen_keys = [k]
            current_key = k
            predecessors = {}
            dist_from_key[k] = 0

            while remaining_keys :
                # 1. on met a jour les distances avec les voisins
                for i in [ z for z in voisins[current_key] if z not in seen_keys ] :

                    if  dist_from_key[current_key] + distances[current_key][i] < dist_from_key[i] :
                        dist_from_key[i] = dist_from_key[current_key] + distances[current_key][i]
                        predecessors[i] = current_key

                if k == '@' :
                    if current_key in [upl for upl in ascii_uppercase] :
                        portes[current_key].append(current_key.lower())
                
                # on se deplace au plus proche
                minD = 1e6
                for z in remaining_keys :
                    if dist_from_key[z] < minD :
                        minD = dist_from_key[z]
                        current_key = z
                
                seen_keys.append(current_key)
                remaining_keys.remove(current_key)

                if k == '@' :
                    portes[current_key] = portes[predecessors[current_key]].copy()

                if current_key in keys :
                    dist_mat[(k, current_key)] = dist_from_key[current_key]
                    dist_mat[(current_key, k)] = dist_from_key[current_key]
    
    return keys
    
class Node :
    def __init__(self) :
        self.longueur = 0
        self.chemin = ['@']
        #self.last = '-1'
        #self.htime = datetime.datetime.now() - datetime.datetime.now()
    
    def set_info(self, father, index, key, dist_mat, portes) :
        #self.index = index
        self.longueur = father.longueur + dist_mat[(key, father.chemin[-1])]
        self.chemin = father.chemin.copy()
        self.chemin.append(key)
        #self.last = key
        #self.father_id = father.index

    def reachable_keys(self, keys, doors, dist) :
        result = deque()
        #print("Cle restantes : ", [ k for k in keys if k not in self.chemin ])
        for v in [ k for k in keys if k not in self.chemin ] :
            #print("   ", v, doors[v], [ z for z in doors[v] if z not in self.chemin ])
            if not doors[v] or not [ z for z in doors[v] if z not in self.chemin ] :
                result.append(v)
        
        reach = deque()
        init = self.chemin[-1]
        for v in result :
            if not [z for z in result if z != v and dist[(init,z)] + dist[(z,v)] == dist[(init,v)] ] :
                reach.append(v)
        
        return reach

    def heuristique(self, tree) :

        noeuds_manquants = len(tree.keys) - len(self.chemin) - 1

        liste_distances = deque()
        liste_noeuds = [z for z in tree.keys if z not in self.chemin ]
        for k in range(len(liste_noeuds)) :
            v = liste_noeuds[k]
            for z in liste_noeuds[k+1:] :
                liste_distances.append(tree.dist[(v,z)])
        
        return sum(  sorted(liste_distances)[:noeuds_manquants]  )

class Tree :
    def __init__(self, keys, dist_mat, portes, UB) :
        # Donnees de l'arbre
        self.nbr_nodes = 1
        first_node = Node()
        #self.nodelist   = [first_node]
        self.open_nodes = deque([first_node])
        self.current_id = 0
        self.best_value = UB
        self.LB = -1e6
        self.dist_min = min(dist_mat.values())
        self.elagage_count = 0
        self.expandTime = 0
        
        # Donnees generales du probleme
        self.dist = dist_mat
        self.doors = portes
        self.keys = keys

    def add_node(self, key, father) :
        self.nbr_nodes += 1
        
        new_node = Node()
        new_node.set_info(father, self.nbr_nodes, key, self.dist, self.doors)

        #self.nodelist.append(new_node)
        self.open_nodes.append(new_node)
    
    def expand_tree(self) :

        # On a plusieurs cas : 
        #   - si le dernier noeuds est un noeud final :
        #           Donc taille de chemin = taille keys
        #           On met a jour la borne superieure, et on enleve le noeud
        #   - si le dernier noeuds a un chemin que l'on peut couper (UB)
        #           on l'enleve des noeuds ouverts
        #   - si le dernier noeud n'est pas terminal, on lui ajoute tous ses enfants
        
        # Pour augmenter l'arbre
        # on prend le dernier noeud (strategie DFS ou LIFO)

        debut = time.time()
        
        current_node = self.open_nodes[-1]
        self.open_nodes.pop()


        if len(current_node.chemin) == len(self.keys) :
            self.best_value = min(self.best_value, current_node.longueur)
            #print("   ", current_node.chemin, self.best_value)

        #elif current_node.longueur + current_node.heuristique(self) < self.best_value :
        else :
            val = current_node.heuristique(self) + current_node.longueur
            # 2. On calcule les reachable keys
            reach = current_node.reachable_keys(self.keys, self.doors, self.dist)

            # 3. Pour chaque reachable key on ajoute un noeud
            
            last = current_node.chemin[-1]
            for v in reach :    
                if val  + self.dist[(last,v)] < self.best_value :
                    #self.nbr_nodes += 1
                    self.add_node(v, current_node)
                    #new_node = Node()
                    #new_node.set_info(current_node, self.nbr_nodes, v, self.dist, self.doors)
                    #self.open_nodes.append(new_node)

        self.expandTime += time.time() - debut

    def compute_LB(self) :
        LBs = []
        for node in self.open_nodes :
            LBs.append( node.longueur + node.heuristique(self.dist, self.dist_min, self.keys) )
        self.LB = min(LBs)

def Nearest_neighbor_heuristic(keys, dist_mat, portes) :

    nearest_neighbour_cost = 0
    chemin = ['@']
    remaining_keys = keys.copy()
    current_key = '@'
    remaining_keys.remove(current_key)
    reachable_keys = [v for v in remaining_keys if not portes[v] ]

    futur = ''

    while remaining_keys :
        Dmin = 1e9
        for v in reachable_keys :
            # 1. on cherche le plus proche
            if dist_mat[(current_key, v)] < Dmin :
                Dmin = dist_mat[(current_key, v)]
                futur = v

        # 2. on ajoute au chemin
        chemin.append(futur)
        nearest_neighbour_cost += Dmin
        remaining_keys.remove(futur)
        reachable_keys.remove(futur)

        current_key = futur

        # 3. on met a jour les reachables
        for z in [vt for vt in keys if vt not in chemin] :
            if not [puerta for puerta in portes[z] if puerta not in chemin] :
                if not z in reachable_keys :
                    reachable_keys.append(z)

    print("Chemin NN :" , chemin)
    return nearest_neighbour_cost

####################################################################################
#####################################   MAIN   #####################################
####################################################################################

def run_tree_search(instance) :
    ##instance = sys.argv[1]

    #alphabet = [i for i in ascii_lowercase ]

    # Tous les noeuds de l'arbre
    # Deux cas : soit une lettre, maj ou min, soit un croisement numéroté
    timer = datetime.datetime.now() 

    nodes = {}
    find_nodes(nodes, instance)

    distances   = {}
    voisins     = {}
    for elt in nodes :
        distances[elt]  = {}
        voisins[elt]    = []

    find_neighboors_and_graph_distances(nodes, voisins, distances, instance)

    timer = datetime.datetime.now() - timer
    print("%-20s%-25s" %  ("Lecture : ", timer) )

    dist_mat    = {}
    portes      = {}
    timer = datetime.datetime.now()
    keys = dijkstra(nodes, voisins, distances, dist_mat, portes)
    timer = datetime.datetime.now() - timer
    print("%-20s%-25s" %  ("Dijkstra : ", timer))

    #print(dist_mat)

    for v in [z for z in nodes.keys() if z not in keys] :
        del portes[v]

    ################################################
    ################ DebutRecherche ################
    ################################################

    timer = datetime.datetime.now()
    nearest_neighbour_cost = Nearest_neighbor_heuristic(keys, dist_mat, portes)
    timer = datetime.datetime.now() - timer
    print("%-20s%-25s" %  ("NN HEUR : ", timer))

    print("Solution NN", nearest_neighbour_cost)

    timer = datetime.datetime.now()

    tree = Tree(keys, dist_mat, portes, nearest_neighbour_cost)
    

    print()

    ite = 0
    while tree.open_nodes :
    #for k in range(800000) :
        ite += 1
        tree.expand_tree()
        
        if ite % 100000 == 0 :
            print("%-15i%-15i%-5i%-10i%-10s%-20.8s" %
                    ( ite, 
                    tree.nbr_nodes, 
                    len(tree.open_nodes), 
                    tree.best_value,
                    tree.open_nodes[-1].chemin[1],
                    tree.expandTime ) )


    print()
    print("NOMBRE DE NOEUDS : ", tree.nbr_nodes)
    for node in tree.open_nodes :
        print(node.chemin, node.longueur)
    print("SOL : ", tree.best_value)

    timer = datetime.datetime.now() - timer
    print("%-20s%-25s" %  ("Arbre : ", timer))


if __name__ == '__main__' :

    run_tree_search(sys.argv[1])
    exit()

    #r = doprofile(run_tree_search, "arbre.prof", sys.argv[1])
    #print(r)