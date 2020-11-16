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
    assert s_coord_valid(x, y, univers)
    return univers[x, y]


def s_set_cell(x, y, value, univers):
    """ Modifie l'état de la cellule x, y en repère cartésien. """
    assert s_coord_valid(x, y, univers)
    univers[x, y] = value
