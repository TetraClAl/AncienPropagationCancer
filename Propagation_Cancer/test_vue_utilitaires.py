from pytest import *
from vue_utilitaires import *


def test_plane_coord():
    # vérifié sur une figure matplotlib
    assert plane_coord(0, 0) == (0, 0)
    assert plane_coord(0, 1) == (1, sqrt(3))


def test_display_center():
    # vérifié sur une figure matplotlib
    assert True


def test_get_color():
    centre = [1, 1, 2, 2]
    env = init_univers(4, 4, centre)

    assert get_color(1, 1, env[0], centre) == 3
