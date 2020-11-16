from utilitaires_univers import *
from pytest import *

tab = [[0, 1], [1, 0]]
tab2 = [[1, 1], [0, 0]]


def test_get_univers():
    assert get_univers(tab, 0, 0) == 0
    assert get_univers(tab, 2, 0) == 0
    assert get_univers(tab, 2, 2) == 0
    assert get_univers(tab, 2, 1) == 1
    assert get_univers(tab, 2, 3) == 1


def test_set_univers():
    set_univers(tab, 0, 0, 1)
    assert get_univers(tab, 0, 0) == 1

    set_univers(tab, 0, 0, 0)
    assert get_univers(tab, 0, 0) == 0


def test_melange_n():
    for i in range(2):
        for j in range(2):
            assert melange_n(i, j) == j


def test_melange_or():
    for i in range(2):
        for j in range(2):
            if i == 0 and j == 0:
                assert melange_or(i, j) == 0
            else:
                assert melange_or(i, j) == 1


def test_ajouter_pattern():
    ajouter_pattern(tab, tab2, 0, 0)
    for i in range(2):
        for j in range(2):
            assert tab[i][j] == tab2[i][j]
