from controleur_initialisation import *
from controleur_regen import *
from random import choice
from random import random


def dep_homotype(env, i, j, p):
    # p est la probabilité d'aller sur une cellule possédant un voisin infecté : p>0.5 traduit une attraction entre cellules tumorales
    voisins = get_adj(i, j, env[0])
    voisins_libres = []
    for v in voisins:
        if get_cell(v[0], v[1], env[0]) != 1:
            voisins_libres.append(v)
    if voisins_libres != []:
        l1 = []
        l2 = []
    # on sépare les sites libres selon s'ils ont un voisin infecté (autre que la cellule étudiée) ou non
        for coord in voisins_libres:
            r = 0
            nv = get_adj(coord[0], coord[1], env[0])
            for x in nv:
                if get_cell(x[0], x[1], env[0]) == 1:
                    r += 1
            if r >= 2:
                l1.append(coord)
            else:
                l2.append(coord)
    # tirage aléatoire d'un nombre entre 0 et 1 pour décider le type de site sur lequel migrer
        t = random()
        if t <= p:

            if l1 != []:
                # on choisit au hasard un site dont l'un des voisins est une cellule tumorale
                choix = choice(l1)
                set_cell(choix[0], choix[1], 1, env)
                set_cell(i, j, 0, env)

        else:

            if l2 != []:
                # on choisit au hasard un site voisin libre
                choix = choice(l2)
                set_cell(choix[0], choix[1], 1, env)
                set_cell(i, j, 0, env)


def dep_homotype_all(env, centre, p=None, q=None):

    tumorales = tri_cells(env[0])[1]

    # on applique la règle de déplacement à toutes les cellules tumorales
    for coord in tumorales:
        i = coord[0]
        j = coord[1]
        dep_homotype(env, i, j, p)

        # on régénère le centre en cas de besoin
        if [i, j] in liste_centre(centre):
            regen_centre(env, centre)


### Prise en compte des groupes de cellules tumorales ###


def dep_homotype_groupe(env, i, j, p):

    g = get_groupe(i, j, env)

    voisins = get_adj(i, j, env[0])
    voisins_libres = []
    for v in voisins:
        if get_cell(v[0], v[1], env[0]) != 1:
            voisins_libres.append(v)

    if voisins_libres != []:
        l1 = []
        l2 = []
    # on sépare les sites libres selon s'ils ont un voisin infecté (autre que la cellule étudiée) ou non
        for coord in voisins_libres:
            r = 0
            nv = get_adj(coord[0], coord[1], env[0])
            for x in nv:

                if get_cell(x[0], x[1], env[0]) == 1 and get_groupe(x[0], x[1], env) == g:
                    r += 1

            if r >= 2:
                l1.append(coord)

            if get_cell(coord[0], coord[1], env[0]) == 0:
                l2.append(coord)

        t = random()
        if t <= p:

            if l1 != []:
                # on choisit au hasard un site dont l'un des voisins est une cellule tumorale
                choix = choice(l1)
                set_cell(choix[0], choix[1], 1, env)
                set_cell(i, j, 0, env)

        else:

            if l2 != []:
                # on choisit au hasard un site voisin libre
                choix = choice(l2)
                set_cell(choix[0], choix[1], 1, env)
                set_cell(i, j, 0, env)


def dep_homotype_groupe_all(env, centre, p=None, q=None):

    tumorales = tri_cells(env[0])[1]

    # on applique la règle de déplacement à toutes les cellules tumorales
    for coord in tumorales:
        i = coord[0]
        j = coord[1]
        dep_homotype_groupe(env, i, j, p)

        # on régénère le centre en cas de besoin
        if [i, j] in liste_centre(centre):
            regen_centre(env, centre)
