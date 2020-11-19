from controleur_initialisation import *
from controleur_regen import *
from random import choice
from random import random


def classe_voisins(liste, env):
    """ Sépare les elts de liste selon s'ils ont plus de deux voisins infectés ou non """
    l1 = []
    l2 = []
    for coord in liste:
        r = 0
        nv = get_adj(coord[0], coord[1], env[0])
        for x in nv:
            if get_cell(x[0], x[1], env[0]) == 1:
                r += 1
        if r >= 2:
            l1.append(coord)
        else:
            l2.append(coord)

    return l1, l2


def migration_aléatoire(i, j, l, env):
    """ fait migrer la cellule tumorale (i,j) sur un site de l choisit aléatoirement """
    if l != []:
        choix = choice(l)  # choisit aléatoirement un élément de l
        # si ce site n'est pas deja occupé par une cellule tumorale, (i,j) peut bouger
        if get_cell(choix[0], choix[1], env[0]) != 1:
            # on met un 1 sur le site choisit
            set_cell(choix[0], choix[1], 1, env)
            set_cell(i, j, 0, env)  # on remet un 0 sur le site laissé vacant


def dep_homotype(env, i, j, p):
    """ déplace la cellule (i, j) suivant la règle homotype """
    # p est la probabilité d'aller sur une cellule possédant un voisin infecté : p>0.5 traduit une attraction entre cellules tumorales
    voisins = get_adj(i, j, env[0])
    voisins_libres = []
    # on récupère les sites libres parmis les voisins
    for v in voisins:
        if get_cell(v[0], v[1], env[0]) != 1:
            voisins_libres.append(v)

    if voisins_libres != []:
        l1 = classe_voisins(voisins_libres, env)[0]
        l2 = classe_voisins(voisins_libres, env)[1]

    # tirage aléatoire d'un nombre entre 0 et 1 pour décider le type de site sur lequel migrer
        t = random()
        if t <= p:  # migration sur une cellule voisine d'une cellule infectée
            migration_aléatoire(i, j, l1, env)

        else:  # migration sur une cellule isolée
            migration_aléatoire(i, j, l2, env)


def dep_homotype_all(env, centre, p=None, q=None):
    """ Applique la règle de déplacement homotype à toutes les cellules tumorales """

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


def liste_voisins_groupe(liste, g, env):
    """ Donne les éléments de liste qui ont au moins deux voisins infectés du groupe g """
    res = []
    for coord in liste:
        r = 0
        nv = get_adj(coord[0], coord[1], env[0])
        for x in nv:

            if get_cell(x[0], x[1], env[0]) == 1 and get_groupe(x[0], x[1], env) == g:
                r += 1

        if r >= 2:
            res.append(coord)
    return res


def dep_homotype_groupe(env, i, j, p):
    """ déplace la cellule (i, j) suivant la règle homotype prenant en compte les groupes """
    g = get_groupe(i, j, env)

    voisins = get_adj(i, j, env[0])
    voisins_libres = []
    # on récupère les sites libres parmis les voisins
    for v in voisins:
        if get_cell(v[0], v[1], env[0]) != 1:
            voisins_libres.append(v)

    if voisins_libres != []:
        # on sépare les sites libres selon s'ils ont un voisin infecté du même groupe que (i, j) (autre que la cellule étudiée) ou non
        l1 = liste_voisins_groupe(voisins_libres, g, env)
        l2 = classe_voisins(voisins_libres, env)[1]

        # on choisit aléatoirement un élément entre 0 et 1
        t = random()
        if t <= p:  # migration sur une cellule voisine d'une cellule tumorale
            migration_aléatoire(i, j, l1, env)

        else:  # migration sur une cellule isolée
            migration_aléatoire(i, j, l2, env)


def dep_homotype_groupe_all(env, centre, p=None, q=None):
    """ Applique la règle de déplacement homotype prenant en compte les groupes sur toutes les cellules tumorales """

    tumorales = tri_cells(env[0])[1]

    # on applique la règle de déplacement à toutes les cellules tumorales
    for coord in tumorales:
        i = coord[0]
        j = coord[1]
        dep_homotype_groupe(env, i, j, p)

        # on régénère le centre en cas de besoin
        if [i, j] in liste_centre(centre):
            regen_centre(env, centre)
