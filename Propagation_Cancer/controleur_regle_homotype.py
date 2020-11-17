from controleur_initialisation import *
from random import choice
from random import random

def dep_homotype(env, i, j, p):
    # p est la probabilité d'aller sur une cellule possédant un voisin infecté : p>0.5 traduit une attraction entre cellules tumorales
    voisins = get_adj(i, j, env[0])
    voisins_libres = []
    for v in voisins :
        if get_cell(v[0], v[1], env[0]) != 1:
            voisins_libres.append(v)
    l1 = []
    l2 = []
    # on sépare les sites libres selon s'ils ont un voisin infecté (autre que la cellule étudiée) ou non
    for coord in voisins_libres:
            r = 0
            nv = get_adj(coord[0], coord[1], env[0])
            for x in nv :
                if get_cell(x[0], x[1], env[0]) == 1:
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
            set_cell(choix[0], choix[1], 1, env)

    else :

         if l2 != []:
            choix = choice(l2)
            set_cell(choix[0], choix[1], 1, env)

    
        

def dep_homotype_all(env, p, centre):

    (n, m) = np.shape(env[0])
    for i in range(n):
        for j in range(m):
            if get_cell(i, j, env[0]) == 1:
                dep_homotype(env, i, j, p)
                if i >= centre[0] and i < centre[0]+centre[1] and j >= centre[2] and j < centre[2] + centre[3] :
                    regen_centre(env, centre[0], centre[1], centre[2], centre[3])

    return env








