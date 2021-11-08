import matplotlib.pyplot as plt
import numpy as np

'''
Approximation grossière du brut vers le net avec un taux de charge de 78%
'''
def brutVersNet(brut: int, ajustement=0):
    return 0.78*(brut - ajustement)

'''
Expression à annuler : la différence entre le net ajusté et le net souhaité. C'est en réalité une 
fonction à un seul paramètre : ajustement, car brut et netSouhaite sont fixés
'''
def differenceEntreNetEtNetSouhaite(brut, ajustement, netSouhaite):
    return netSouhaite - brutVersNet(brut, ajustement)

'''
La méthode de la fausse position est un algorithme permettant de résoudre l'équation f(x) = 0. Dans 
notre cas, elle va permettre d'annuler la fonction differenceEntreNetEtNetSouhaite ci dessus. Voici
le fonctionnement de l'algorithme (un dessin aide fortement) :
1) On trouve deux points de la fonction de part et d'autre de l'axe des abscisses : A (en dessous)
et B (au dessus)
2) On trace la droite entre ces deux points et on relève x1, l'abscisse du point d'intersection de la
droite et de l'axe des abscisses, et y1 son image par la fonction f. Le point A1 (x1, y1) est donc sur la
courbe de f, et on a yA < y1 < 0
3) On itère cette étape jusqu'à ce que yn soit égal à 0, ou au moins inférieur à un certain seuil de
tolérance
'''

'''
On détermine les coordonnées des points A et B qui vont servir à l'algorithme en prenant deux points
extrêmes : on va de 1000 en 1000 et de - 1000 en - 1000 en vérifiant à chaque itération si les images
par f correspondent à ce qu'on voudrait
'''
def parametresSuiteReccurente(brut, netSouhaite):
    xAdepart = -1000
    xBdepart = 1000
    while differenceEntreNetEtNetSouhaite(brut, xAdepart, netSouhaite) > 0:
        xAdepart -= 1000
    pointA = (xAdepart, differenceEntreNetEtNetSouhaite(brut, xAdepart, netSouhaite))
    while differenceEntreNetEtNetSouhaite(brut, xBdepart, netSouhaite) < 0:
        xBdepart += 1000
    pointB = (xBdepart, differenceEntreNetEtNetSouhaite(brut, xBdepart, netSouhaite))

    return pointA, pointB

'''
Définition de la suite convergente de la méthode de la fausse position, il s'agit d'une simple équation
affine à résoudre pour annuler une droite : Xn+1 = Xn - [(xb - Xn)/(f(xb) - f(Xn))]*f(Xn)
'''
def nouvelAjustement(x, y, xb, yb, brut, netSouhaite):
    nouvelAjustement = x - ((xb - x)/(yb - y))*y
    return nouvelAjustement, differenceEntreNetEtNetSouhaite(brut, nouvelAjustement, netSouhaite) 

'''
On lance des itérations de l'algorithme jusqu'à obtenir le net souhaité
'''
def calculAjustementPourNetSouhaite(brut, netSouhaite, precision):
    pointA, pointB = parametresSuiteReccurente(brut, netSouhaite)
    ajustement, netAvecAjustement = pointA
    while abs(netAvecAjustement) > precision:
        ajustement, netAvecAjustement = nouvelAjustement(ajustement, netAvecAjustement, pointB[0], pointB[1], brut, netSouhaite)
    return ajustement

if __name__ == "__main__":
    brut = 3000
    netSouhaite = 20
    precision = 0.01
    ajustement = calculAjustementPourNetSouhaite(brut, netSouhaite, precision)
    verbe = "retrancher" if ajustement > 0 else "ajouter"
    print(f"Vous devez {verbe} {round(abs(ajustement),2)} € au brut pour atteindre le net souhaité")
    

