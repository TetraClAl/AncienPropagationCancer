import numpy as np
import copy as c

from utilitaires_a import *
from generate_universe_a import *
from survival_a import *


# init : univers initial, n : nombre d'itérations
# renvoie le tableau des états de l'univers


def game_life_simulation(init, n):
    animation = []  # stocke les états successifs de l'univers dans une liste
    univ = init  # univers courant
    for i in range(n):
        # copies indépendantes à chaque fois
        animation.append(c.deepcopy(univ))
        univ = generation(univ)  # itération suivante
    return animation


# renvoie l'état final
def game_life_simulation_end(init, n):
    animation = game_life_simulation(init, n)
    return animation[n-1]
