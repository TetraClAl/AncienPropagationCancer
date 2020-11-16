import sqlite3
import numpy as np
import copy as c
from seeds_a import *
from utilitaires_a import *

# compte les cellules voisines vivantes


def voisines(univers, x, y):
    # On initialise le comptage
    s = 0

    # Colonne de gauche
    s += get_univers(univers, x + 1, y + 1)
    s += get_univers(univers, x, y + 1)
    s += get_univers(univers, x - 1, y + 1)

    # Colonne du milieu
    s += get_univers(univers, x + 1, y)
    s += get_univers(univers, x - 1, y)

    # Colonne de droite
    s += get_univers(univers, x + 1, y - 1)
    s += get_univers(univers, x, y - 1)
    s += get_univers(univers, x - 1, y - 1)

    # Retour
    return s

# règle du jeu sur une cellule donnée


def survival_cell(universe, x, y):
    s = voisines(universe, x, y)
    v = get_univers(universe, x, y)

    # cellule vivante
    if v == 1:
        if s == 2 or s == 3:
            return 1  # Elle vie
        else:
            return 0  # Elle décède

    # Si la cellule est morte
    else:
        if s == 3:
            return 1  # Elle naît
        else:
            return 0  # Elle reste morte


# règles sur l'ensemble des cellules
def generation(universe):
    # parcourir les cellules
    survival = c.deepcopy(universe)
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            set_univers(survival, i, j, survival_cell(universe, i, j))
    return survival


# init : univers initial, n : nombre d'itérations
def game_life_simulate(init, n):
    animation = []  # stocke les états successifs de l'univers
    univ = init  # univers courant
    for i in range(n):
        # copies indépendantes à chaque fois
        animation.append([c.deepcopy(univ)])
        univ = generation(univ)  # itération suivante
    return animation[n-1]
