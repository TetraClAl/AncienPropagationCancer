from controleur_initialisation import *
from random import choice
from random import random

def dep_homotype(univers, i, j, p):
    # p est la probabilité d'aller sur une cellule possédant un voisin infecté : p>0.5 traduit une attraction entre cellules tumorales
    voisins = get_adj(i, j, univers)
    voisins_libres = []
    for v in voisins :
        if get_cell(v[0], v[1], univers) != 1:
            voisins_libres.append(v)
    l1 = []
    l2 = []
    # on sépare les sites libres selon s'ils ont un voisin infecté (autre que la cellule étudiée) ou non
    for coord in voisins_libres:
            r = 0
            nv = get_adj(coord[0], coord[1], univers)
            for x in nv :
                if get_cell(x[0], x[1], univers) == 1:
                    r+= 1
            if r >= 2 :
                l1.append(coord)
            else :
                l2.append(coord)
    # tirage d'un nombre entre 0 et 1 pour décider le type de site sur lequel migrer
    t = random()
    if t <= p :
        
        if l1 != [] :
            choix = choice(l1)
            set_cell(choix[0], choix[1], 1, univers)

    else :

         if l2 != []:
            choix = choice(l2)
            set_cell(choix[0], choix[1], 1, univers)

    return univers
        








