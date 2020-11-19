from random import choice
from random import random

from controleur_jonction_heterotype import *
from controleur_regle_homotype import *


def jonct_duo_evaluation(env, x, y):
    """Classe les voisins en plusieurs listes, avec les deux règles"""

    # voisins vides:
    vides = get_adj_vide(x, y, env)

    # Evaluation heterotype: voisins occupés par un astrocyte
    astros = get_adj_astrocyte(x, y, env)

    # Evaluation homotype: homo_yes = site ayant des voisines cancereuses
    g = get_groupe(x, y, env)
    # sites non occupés par une cellule cancéreuse
    voisins_libres = union_liste(vides, astros)
    homo_yes = liste_voisins_groupe(voisins_libres, g, env)
    homo_no = classe_voisins(voisins_libres, env)[1]

    return vides, astros, homo_yes, homo_no


def jonct_duo_move(env, x, y, p=None, q=None):

    vides, astros, homo_yes, homo_no = jonct_duo_evaluation(env, x, y)

    # choix de la liste de sites eligibles
    t = random()

    # initialement, tous les voisins sont possibles
    possibles = get_adj(x, y, env[0])
    homo = []
    hetero = []
    # pour homotype:
    if p is not None:
        if t < p:
            homo = homo_yes  # la cellule reste en contact avec ses voisines
        else:
            homo = homo_no

    # pour heterotype:
    if q is not None:
        if t < q:
            hetero = astros  # la cellule se déplace sur un astrocyte
        else:
            hetero = vides

    # p=None et q=None : choix uniforme
    if p is not None or q is not None:
        # liste des sites éligibles adaptée
        possibles = union_liste(homo, hetero)
    migration_aléatoire(x, y, possibles, env)


def jonction_duo(env, centre, p, q):
    tumorales = tri_cells(env[0])[1]

    for (x, y) in tumorales:  # a toutes les cellules tumorales, on applique la règle
        jonct_duo_move(env, x, y, p, q)

    # on regenère le centre
    regen_centre(env, centre)
