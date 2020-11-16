# from data_main import *


def get_cell(coord):
    """ Retourne l'état de la cellule (x, y). """


def set_cell(coord, value):
    """ Modifie l'état de la cellule (x, y). """


def get_cellC(x, y):
    """ Retourne l'état de la cellule x, y en repère carthésien. """


def set_cellC(x, y, value):
    """ Modifie l'état de la cellule x, y en repère carthésien. """


def get_groupe(coord):
    """ Retourne l'index du groupe de la cellule (x, y). """


def get_adj(coord):
    """ Retourne la liste des coordonnées des cellules adjacentes à (x, y). """


def get_adj_groupe(index):
    """ Retourne la liste des coordonnées des cellules adjacentes au groupe index. """


def get_membre_groupe(index):
    """ Retourne la liste des coordonnées des cellules du groupe index. """


def union_liste(l1, l2):
    """ Fait une union de deux listes de cellules. """


def inter_liste(l1, l2):
    """ Fait un inter de deux listes de cellules. """


def prive_liste(l1, l2):
    """ Retourne la liste l1 privée de l2. """


def egal_liste(l1, l2):
    """ Indique si deux listes sont égales. """


def copie_liste(l1):
    """ Retourne une deepcopy de l1. """
