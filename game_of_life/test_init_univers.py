from init_univers import *
from pytest import *


def test_init_univers():
    uni = init_univers(4, 4, seeds["boat"], 0, 0)

    comp = [[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]

    for i in range(len(uni)):
        for j in range(len(uni[0])):
            assert comp[i][j] == uni[i][j]
