from survival import *
from pytest import *

from display import *
from animation import *


def test_create_plane():
    fig, ax = plt.subplots(1)
    testplane = create_plane((3, 3), ax)

    assert len(testplane) == 3
    assert len(testplane[0]) == 3


def test_refresh_plane():
    fig, ax = plt.subplots(1)
    testplane = create_plane((3, 3), ax)

    univers = [[1, 0, 0], [0, 1, 0], [1, 0, 0]]

    refresh_plane(testplane, univers)

    assert testplane[0][0].get_visible() == True
    assert testplane[1][0].get_visible() == False


def test_redim():
    tab = [[1, 2], [3, 4]]
    tab2 = redim(tab)

    assert len(tab2) == 4

    assert tab2[2] == 3


def test_display_animated_universe():
    univers = init_univers(5, 5, seeds["boat"])

    display_animated_universe(univers)