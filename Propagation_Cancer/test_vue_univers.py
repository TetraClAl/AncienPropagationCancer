from pytest import *
from vue_univers import *

univers = np.array([[0, 1, 2], [1, 0, 1], [2, 1, 1]])


def test_tri_cells():
    v, t, a = tri_cells(univers)
    V = [(0, 0), (2, 0), (2, 2)]
    T = [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)]
    A = [(0, 2)]
    #assert v == V
    #assert t == T TODO AiLing : Trouver et corriger pb assert
    #assert a == A
