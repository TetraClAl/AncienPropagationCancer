from generate_universe import *
import numpy as np
seeds = {"r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]]}


# type_seed = une clé du dictionnaire seed dont la valeur est le patern

def create_seed(type_seed):
    seed = seeds[type_seed]  # prend la valeur de la clé (= le patern)
    return seed

seed = create_seed(type_seed = "r_pentomino")
universe = generate_universe((6, 6))

def add_seed_to_universe(seed, universe, xstart, ystart):
    (a, b) = np.shape(seed)
    for i in range(a):
        for j in range(b):
            universe[i + xstart][j + ystart] = universe[i+ xstart][j+ystart] + seed[i][j]
    return universe


universe = add_seed_to_universe(seed, universe, xstart=1, ystart=1)
print(universe)
