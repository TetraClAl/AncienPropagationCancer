from data_import import *


def _create_univers(x, y):
    """ Crée un univers de taille x, y. """
    return np.array((x, y))


def _coord_validC(coord, univers):
    """ Renvoie True si les coordonnées sont valides. """
    # Condition de positivité
    if x < 0:
        return False
    if y < 0:
        return False

    # Dépliage du tuple et récupération taille
    x, y = coord
    tx = np.size(univers, 0)
    ty = np.size(univers, 1)

    # Conditions taille
    if x >= tx:
        return False
    if y >= ty:
        return False

    # Par défaut coordonnées correctes
    return True


def _cubic_to_cart(x, y):  # EVITER D'UTILISER CETTE FONCTION DANS LE VUE/CONTROLLER
    """ Transforme des coordonnées cubiques en coordonnées cartésiennes. """
    ycub = y
    xcub = x - y // 2


def _coord_valid(x, y, univers):
    """ Renvoie True si les coordonnées sont valides. """
    return _coord_validC(_cubic_to_cart(x, y), univers)


def _get_cell(coord, univers):
    """ Retourne l'état de la cellule (x, y). """
    assert _coord_valid(coord)
    return univers[coord]


def _set_cell(coord, value, univers):
    """ Modifie l'état de la cellule (x, y). """
    assert _coord_valid(coord)
    univers[coord] = value


def _get_cellC(x, y, univers):
    """ Retourne l'état de la cellule x, y en repère cartésien. """
    assert _coord_validC(x, y)
    return univers[x, y]


def _set_cellC(x, y, value, univers):
    """ Modifie l'état de la cellule x, y en repère cartésien. """
    assert _coord_validC(x, y)
    univers[coord] = value
