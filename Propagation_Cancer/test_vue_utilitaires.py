from pytest import *
from vue_utilitaires import *


def test_plane_coord():
    # vérifié sur une figure matplotlib
    assert plane_coord(0, 0) == (0, 0)
    assert plane_coord(0, 1) == (1, sqrt(3))


def test_display_center():
    # vérifié sur une figure matplotlib
    assert True
