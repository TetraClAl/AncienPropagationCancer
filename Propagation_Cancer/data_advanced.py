from data_import import *
from data_base import *


oddr_directions = [
    [[+1,  0], [0, -1], [-1, -1],
     [-1,  0], [-1, +1], [0, +1]],
    [[+1,  0], [+1, -1], [0, -1],
     [-1,  0], [0, +1], [+1, +1]],
]


def voisin_dir(hex, direction):
    """ Retourne les coordonnées de l'hex situé dans la direction associée. """
    if hex[0] % 2 == 1:
        parity = 1
    else:
        parity = 0
    dir = oddr_directions[parity][direction]
    return hex[1] + dir[0], hex[0] + dir[1]


def s_get_adj(x, y, univers):
    """ Retourne la liste des coordonnées des cellules adjacentes à (x, y). """
    Lc = []
    for direction in range(6):
        x1, y2 = voisin_dir([x, y], direction)
        Lc += [[x1, y2]]
    return s_check_list(Lc, univers)
