from data_import import *
from data_base import *

# Note to self (TODO) : utiliser des listes de coordonnées triées selon l'ordre alphabétique pourrait permettre d'accélérer les fusions de listes en éléminant les doublons.
# Les propriétés de ces éléments (coordonnées ne se répétant pas) pourraient permettre d'obtenir un algo très rapide.

# ----- Ce code pourrait nécessiter du refactoring

hex_directions = [
    [[+1,  0], [0, -1], [-1, -1],
     [-1,  0], [-1, +1], [0, +1]],
    [[+1,  0], [+1, -1], [0, -1],
     [-1,  0], [0, +1], [+1, +1]],
]


def voisin_dir(hex, direction):
    """ Retourne les coordonnées de l'hex situé dans la direction associée. """
    # Calcul de parité
    if hex[0] % 2 == 1:
        parity = 1
    else:
        parity = 0

    # Récupération de la direction à effectuer
    direction_calc = hex_directions[parity][direction]

    # Calcul des nouvelles coordonnées ajoutant nos coordonnées d'origine comme offset
    # Mauvaise inversion ? TODO : Vérifier que les coordonnées ne sont pas inversées (update : normalement c'est bon, les tests sont corrects)
    return hex[1] + direction_calc[0], hex[0] + direction_calc[1]


def s_get_adj(x, y, univers):
    """ Retourne la liste des coordonnées des cellules adjacentes à (x, y). """
    Lc = []
    for direction in range(6):
        x1, y2 = voisin_dir([x, y], direction)
        Lc += [[x1, y2]]
    return s_check_list(Lc, univers)

# ----- Fin de la section cible refactoring
