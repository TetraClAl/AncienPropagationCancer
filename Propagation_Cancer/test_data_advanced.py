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
    L1c = [[0, 0], [1, 0], [1, 1], [1, 2], [0, 2]]
    L2c = [[0, 0], [0, 1], [1, 1], [2, 0]]

    # Vérification longueur
    assert len(L1c) == len(L1)
    assert len(L2c) == len(L2)

    # Vérification éléments
    for e in L1c:
        # On vérifie si e est dans L1
        test = False
        for c in L1:
            if c[0] == e[0] and c[1] == e[1]:
                test = True
        assert test  # Sinon assert
    for e in L2c:  # Idem, TODO : refactorisation avec fonction
        test = False
        for c in L2:
            if c[0] == e[0] and c[1] == e[1]:
                test = True
        assert test
