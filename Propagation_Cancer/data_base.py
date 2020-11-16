from data_import import *


def s_create_univers(x, y):
    """ Crée un univers de taille x, y. """
    return np.zeros((x, y), dtype=int)


def s_coord_validC(x, y, univers):
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


def s_cubic_to_cart(coord):  # EVITER D'UTILISER CETTE FONCTION DANS LE VUE/CONTROLLER
    """ Transforme des coordonnées cubiques en coordonnées cartésiennes. """
    x, y = coord
    yr = y
    xr = x - y // 2

    return yr, xr


def s_coord_valid(coord, univers):
    """ Renvoie True si les coordonnées sont valides. """
    x, y = s_cubic_to_cart(coord)
    return s_coord_validC(x, y, univers)


def s_get_cell(coord, univers):
    """ Retourne l'état de la cellule (x, y). """
    assert s_coord_valid(coord, univers)
    return univers[coord]


def s_set_cell(coord, value, univers):
    """ Modifie l'état de la cellule (x, y). """
    assert s_coord_valid(coord, univers)
    univers[coord] = value


def s_get_cellC(x, y, univers):
    """ Retourne l'état de la cellule x, y en repère cartésien. """
    assert s_coord_validC(x, y, univers)
    return univers[x, y]


def s_set_cellC(x, y, value, univers):
    """ Modifie l'état de la cellule x, y en repère cartésien. """
    assert s_coord_validC(x, y, univers)
    univers[x, y] = value
