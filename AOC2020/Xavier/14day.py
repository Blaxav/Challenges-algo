import sys
from time import time
from math import ceil

def read_file(transfo, materials, stock) :
    file = open("input.txt", 'r')
    for line in file :
        line = line.rstrip()
        # 1. on separe le produit des reactifs
        reac_line = line.split('=>')[0]

        prod_qtt = int( line.split('=>')[1].split()[0] )
        prod_name = line.split('=>')[1].split()[1]

        print(reac_line , "=>", prod_qtt, prod_name)

        materials[prod_name]    = prod_qtt
        stock[prod_name]        = 0
        transfo[prod_name]      = transformation(prod_name, prod_qtt)
        for elt in reac_line.split(',') :
            transfo[prod_name].add_reactif(elt)

    for t in transfo :
        print(transfo[t].prod_qtt, transfo[t].prod_name, transfo[t].reac)

    stock["ORE"] = 0
    materials["ORE"] = 0


class material :
    def __init__(self, name, qtt) :
        self.name = name
        self.qtt_to_destroy = qtt

class transformation :
    def __init__(self, name, qtt) :
        self.reac = {}
        self.prod_name = name
        self.prod_qtt = qtt
    
    def add_reactif(self, line) :
        qtt  = int( line.split()[0] )
        name = line.split()[1]
        self.reac[name] = qtt

# Effectue number fois la transfo inverse de product (operation de destruction)
def apply_transfo(stock, transformations, materials, prod, number) :
    stock[prod] -= number * materials[prod]
    for elt in transformations[prod].reac :
        stock[elt] += number * transformations[prod].reac[elt]

def apply_all_transfo(stock,transformations, materials) :

    counter = 0

    for mat in stock :
        if mat != "ORE" :
            destruc_times = ceil(stock[mat] / materials[mat])
            apply_transfo(stock, transformations, materials, mat, destruc_times)
            counter += destruc_times

            if destruc_times > 0 :
                print(stock)
    
    return counter

if __name__ == '__main__' :

    # Dictionnaire des transformations
    # La cle du dico est le nom du produit
    transformations = {}
    materials = {}
    stock = {}

    read_file(transformations, materials, stock)

    stock["FUEL"] = 1

    print()
    print("DEBUT")
    print(stock)
    
    counter = 1
    stop = (counter == 0)
    while not stop :
        counter = apply_all_transfo(stock, transformations, materials)
        stop = (counter == 0)