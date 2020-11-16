from data_import import *


def s_create_univers(x, y):
    """ Crée un univers de taille x, y. """
    return np.zeros((x, y), dtype=int)


def s_coord_valid(x, y, univers):
    """ Renvoie True si les coordonnées sont valides. """
    # Condition de positivité
    if x < 0:
        return False
    if y < 0:
        return False

    # Taille
    tx = np.size(univers, 0)
    ty = np.size(univers, 1)

    # Conditions taille
    if x >= tx:
        return False
    if y >= ty:
        return False

    # Par défaut coordonnées correctes
    return True


def s_get_cell(x, y, univers):
    """ Retourne l'état de la cellule x, y en repère cartésien. """
    #assert s_coord_valid(x, y, univers)
    return univers[x, y]


def s_set_cell(x, y, value, univers):
    """ Modifie l'état de la cellule x, y en repère cartésien. """
    #assert s_coord_valid(x, y, univers)
    univers[x, y] = value


def s_check_list(l1, univers):
    LR = []
    for e in l1:
        if s_coord_valid(e[0], e[1], univers):
            LR += [e]
    return LR


oddr_directions = [
    [[+1,  0], [0, -1], [-1, -1],
     [-1,  0], [-1, +1], [0, +1]],
    [[+1,  0], [+1, -1], [0, -1],
     [-1,  0], [0, +1], [+1, +1]],
]


def voisin_dir(hex, direction):
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
