from data_base import *

# 0 = Vide
# 1 = Tumeur
# 2 = Astrocyte

# Fonctionnalité 0.1


def create_univers(x, y):
    """ Crée un univers de taille x, y. """
    return s_create_univers(x, y)


def coord_valid(coord, univers):
    """ Renvoie True si les coordonnées sont valides. """
    return s_coord_valid(coord, univers)


def coord_validC(x, y, univers):
    """ Renvoie True si les coordonnées sont valides. """
    return s_coord_validC(x, y, univers)


def cubic_to_cart(coord):  # EVITER D'UTILISER CETTE FONCTION DANS LE VUE/CONTROLLER
    """ Transforme des coordonnées cubiques en coordonnées cartésiennes. """
    return s_cubic_to_cart(coord)


def get_cell(coord, univers):
    """ Retourne l'état de la cellule (x, y). """
    return s_get_cell(coord, univers)


def set_cell(coord, value, univers):
    """ Modifie l'état de la cellule (x, y). """
    s_set_cell(coord, value, univers)


def get_cellC(x, y, univers):
    """ Retourne l'état de la cellule x, y en repère cartésien. """
    return s_get_cellC(x, y, univers)


def set_cellC(x, y, value, univers):
    """ Modifie l'état de la cellule x, y en repère cartésien. """
    return s_set_cellC(x, y, value, univers)


def get_groupe(coord, univers):
    """ Retourne l'index du groupe de la cellule (x, y). """


def get_adj(coord, univers):
    """ Retourne la liste des coordonnées des cellules adjacentes à (x, y). """


def get_adj_groupe(index, univers):
    """ Retourne la liste des coordonnées des cellules adjacentes au groupe index. """


def get_membre_groupe(index, univers):
    """ Retourne la liste des coordonnées des cellules du groupe index. """


def union_liste(l1, l2, univers):
    """ Fait une union de deux listes de cellules. """


def inter_liste(l1, l2, univers):
    """ Fait un inter de deux listes de cellules. """


def prive_liste(l1, l2, univers):
    """ Retourne la liste l1 privée de l2. """


def egal_liste(l1, l2, univers):
    """ Indique si deux listes sont égales. """


def doubl_liste(l1, univers):
    """ Retourne une liste l1 sans doublons. """


def copie_liste(l1, univers):
    """ Retourne une deepcopy de l1. """


def appliquer_fonction(l1, f, univers):
    """ Applique une fonction f(coord) sur l1. """
