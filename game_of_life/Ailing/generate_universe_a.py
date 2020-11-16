import sqlite3
import numpy as np
from seeds_a import *
from utilitaires_a import *


def generate_universe_np(size):  # size = (x,y)
    return np.zeros(size)


# type_seed = une clé du dictionnaire seed dont la valeur est le patern


def create_seed(type_seed):
    # prend la valeur de la clé (= le patern)
    seed = np.asarray(seeds[type_seed])
    return seed


def add_seed_to_universe(seed, universe, xstart=0, ystart=0):
    (n, m) = np.shape(seed)
    (a, b) = np.shape(universe)
    if n + xstart < a and m + ystart < b:
        for i in range(n):
            for j in range(m):
                universe[i + xstart][j + ystart] = universe[i +
                                                            xstart][j + ystart] + seed[i][j]
        return universe
    else:
        print('Erreur de dimension')
        return ()


def init_universe(size, type_seed, xstart=0, ystart=0):
    seed = create_seed(type_seed)
    univers = generate_universe_np(size)
    ajouter_pattern(univers, seed, xstart, ystart)
    return univers


""" univers = init_universe((6, 6), 'beacon')
print(univers) """
