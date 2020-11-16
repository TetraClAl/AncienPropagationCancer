from pytest import *
from data_advanced import *


def test_voisin_dir():
    # Tests directs
    # Examen visuel recommandé TODO : Ajouter un code pour vérifier rapidement visuellement que tout est en ordre.
    assert voisin_dir((0, 0), 0) == (1, 0)
    assert voisin_dir((1, 0), 1) == (1, 0)


def test_s_get_adj():
    # Calcul
    uni = s_create_univers(4, 4)
    L1 = s_get_adj(1, 0, uni)
    L2 = s_get_adj(0, 1, uni)

    # Listes de comparaison
    # L1c =

    # Vérification
