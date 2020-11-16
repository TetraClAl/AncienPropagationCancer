from display import *
from pytest import *

tab = [[0, 1], [1, 0]]


def f_test(x, y, b, d, e):
    assert tab[x][y] == 1


def test_display_universe():
    display_universe(tab, f_test)
