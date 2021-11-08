# un matrice de taille 5*5 avec que des 0
mylist = [[0 for porc in range(5)] for cuisseDeCanardConfit in range(5)]

for line in mylist:
    for elt in line:
        print(elt, end=" ")
    print()

# on ajoute 1 en haut a gauche
mylist[0][0] += 1

print()
print()

for line in mylist:
    for elt in line:
        print(elt, end=" ")
    print()
exit()