from data_base import *
from data_advanced import *

# -------
#
# Présentation des conventions pour les variables TODO : faire un .md ou wiki (.md préférable vu le temps)
#
# Type env :
# [0] => univers (np.array(x, y))
#           -> 0 = vide
#           -> 1 = Tumeur
#           -> 2 = Astrocyte
# [1] => folder ([index] => groupe)
#
# Type groupe :
# [0] => composants ([(x, y)] => coordonnées cellules composants le groupe)
# [1] => connexions ([(x, y)] => coordonnées cellules adjacentes au groupe)
#
# (NB : Les listes de cellules seront sûrement classées à un moment pour accélérer les fusions sans doublons)
# (idée : Algo de tri fusion sélectionné, car il se fera naturellement au fûr et à mesure de la fusion des listes)
# TODO : Se coucher avant 2h du mat
# TODO : Mettre à jour le marquage des fonctionnalités en fonction de
#
# -------


# Fonctionnalité 0.1


def create_univers(x, y):
    """ Crée un univers de taille x, y. """
    return s_create_univers(x, y)


def coord_valid(x, y, univers):
    """ Renvoie True si les coordonnées sont valides. """
    return s_coord_valid(x, y, univers)


def get_cell(x, y, univers):
    """ Retourne l'état de la cellule (x, y). """
    return s_get_cell(x, y, univers)


def set_cell(x, y, value, univers):
    """ Modifie l'état de la cellule (x, y). """
    s_set_cell(x, y, value, univers)


def check_list(l1, univers):
    """ Elimine les éléments non valides de la liste (hors de l'univers) mais pas les doublons. """
    return s_check_list(l1, univers)


# Fonctionnalité 2


def create_env(x, y):
    """ Crée un environnement de taille (x, y). """


def get_groupe(x, y, env):
    """ Retourne l'index du groupe de la cellule (x, y). """


def get_adj(x, y, univers):
    """ Retourne la liste des coordonnées des cellules adjacentes à (x, y). """
    return s_get_adj(x, y, univers)


def get_adj_groupe(index, env):
    """ Retourne la liste des coordonnées des cellules adjacentes au groupe index. """


def get_membre_groupe(index, env):
    """ Retourne la liste des coordonnées des cellules du groupe index. """


def union_liste(l1, l2):
    """ Fait une union de deux listes de cellules. """


def inter_liste(l1, l2, univers):
    """ Fait un inter de deux listes de cellules. """


def prive_liste(l1, l2):
    """ Retourne la liste l1 privée de l2. """


def egal_liste(l1, l2, univers):
    """ Indique si deux listes sont égales. """


def doubl_liste(l1, univers):
    """ Retourne une liste l1 sans doublons. """
