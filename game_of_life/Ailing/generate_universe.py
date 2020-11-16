import sqlite3


seeds = {"r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]]}


def generate_universe_np(size):  # size = (x,y)
    return np.zeros(size)


# type_seed = une clé du dictionnaire seed dont la valeur est le patern


def create_seed(type_seed):
    """ Prend une str en argument et retourne la seed associée. """
    seed = seeds[type_seed]  # prend la valeur de la clé (= le patern)
    return seed


def add_seed_to_universe(seed, universe, xstart=0, ystart=0):
    """ Ajoute une seed à l'univers. """
    (n, m) = np.shape(seed)
    for i in range(n):
        for j in range(m):
            universe[i + xstart][j + ystart] = universe[i +
                                                        xstart][j + ystart] + seed[i][j]
    return universe


def generate_universe(size):
    """ Crée un univers. """
    s = []
    for i in range(0, size[0]):
        p = []
        for j in range(0, size[1]):
            p.append(0)
        s.append(p)
    return s
