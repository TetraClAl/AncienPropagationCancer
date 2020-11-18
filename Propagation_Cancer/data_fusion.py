from data_import import *
from data_base import *


# ------ Fonctions fusion


def comp_coord(c1, c2):
    """ Renvoie True si c1 >= c2. """
    if c1[0] > c2[0]:
        return True
    if c1[0] < c2[0]:
        return False
    elif c1[1] >= c2[1]:
        return True
    return False


def compstrict_coord(c1, c2):
    if c1[0] > c2[0]:
        return True
    elif c1[0] == c2[0] and c1[1] > c2[1]:
        return True
    return False


def egal_coord(c1, c2):
    """ Renvoie True si c1 == c2. """
    if c1[0] == c2[0]:
        if c1[1] == c2[1]:
            return True
    return False


def tri_liste(l1):
    """ Fonction de tri de listes basique, à ne pas utiliser pour des listes de plus d'une dizaine d'éléments, préférer une approche par fusions successives. """
    Lr = []

    while len(l1) > 0:
        # Initialisation à 0 de l'index
        index = 0

        # On prend le plus petit élément restant dans la liste
        for i in range(1, len(l1)):
            if comp_coord(l1[index], l1[i]):
                index = i

        # On l'ajoute à Lr
        Lr += [l1[index]]
        del l1[index]

    return Lr


def union_tri(l1, l2):
    """ Effectue une fusion tri. """
    # Initialisation des variables
    Lf = []
    index1 = 0
    index2 = 0

    # Boucle de fusion principale
    while index1 < len(l1) and index2 < len(l2):
        if compstrict_coord(l1[index1], l2[index2]):  # 2 > 1
            Lf += [l2[index2]]
            index2 += 1
        elif egal_coord(l2[index2], l1[index1]):  # 2 = 1
            Lf += [l1[index1]]
            index1 += 1
            index2 += 1
        else:  # 2 < 1
            Lf += [l1[index1]]
            index1 += 1

    # Fusion restantes
    while index1 < len(l1):
        Lf += [l1[index1]]
        index1 += 1
    while index2 < len(l2):
        Lf += [l2[index2]]
        index2 += 1

    # Retour
    return Lf


def prive_tri(l1, l2):
    """ Renvoie l1 privée de l2. """
    # Initialisation
    index2 = 0
    index1 = 0
    Ls = []

    # Boucle principale
    for index1 in range(len(l1)):
        # On avance l'indice jusqu'à ce que l1[index1] <= l2[index2]
        while compstrict_coord(l1[index1], l2[index2]):
            index2 += 1
            if index2 >= len(l2):
                return Ls

        # Si égalité on supprime l'élément, sinon on augmente l'index
        if egal_coord(l1[index1], l2[index2]) == False:
            Ls += [l1[index1]]

    # Retour
    return Ls


if __name__ == "__main__":
    l1 = [[1, 0], [0, 7], [2, 2], [2, 0], [3, 1]]
    l2 = [[6, 7], [2, 1], [3, 0], [1, 6], [0, 0], [1, 0], [2, 2]]

    l1 = tri_liste(l1)
    print(l1)
    l2 = tri_liste(l2)
    print(l2)

    l3 = union_tri(l1, l2)
    print(l3)

    l4 = prive_tri(l1, l2)
    print(l4)

    l5 = prive_tri(l2, l1)
    print(l5)
