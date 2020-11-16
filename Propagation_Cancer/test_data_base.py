from pytest import *
from data_base import *


def test_s_create_univers():
    # Calcul des données
    uni = s_create_univers(2, 3)

    # Vérification
    for i in range(2):
        for j in range(3):
            assert uni[i][j] == 0


def test_s_coord_valid():
    # Calcul des données
    uni = s_create_univers(2, 3)

    # Vérification False
    assert s_coord_valid(10, 10, uni) == False
    assert s_coord_valid(1, -1, uni) == False
    assert s_coord_valid(-1, 1, uni) == False
    assert s_coord_valid(11, 1, uni) == False
    assert s_coord_valid(1, 11, uni) == False

    # Vérification True
    assert s_coord_valid(1, 2, uni) == True
    assert s_coord_valid(0, 0, uni) == True
    assert s_coord_valid(1, 0, uni) == True
    assert s_coord_valid(0, 2, uni) == True


def test_s_get_cell():
    # Calcul des données
    uni = s_create_univers(3, 3)
    uni[0, 0] = 1

    # Vérification
    assert s_get_cell(0, 0, uni) == 1
    assert s_get_cell(1, 1, uni) == 0


def test_s_set_cell():
    # Calcul des données
    uni = s_create_univers(3, 3)
    s_set_cell(1, 0, 1, uni)

    # Vérification
    assert uni[1, 0] == 1


def test_s_check_list():
    # Calcul des données
    L1 = [[1, 0], [-1, 0], [0, 10], [3, 3], [0, 1]]
    uni = s_create_univers(4, 4)
    L2 = s_check_list(L1, uni)
    L3 = [L1[0], L1[3], L1[4]]

    # Vérification
    assert len(L2) == 3
    for i in range(len(L2)):
        assert (L3[i][0], L3[i][1]) == (L2[i][0], L2[i][1])
