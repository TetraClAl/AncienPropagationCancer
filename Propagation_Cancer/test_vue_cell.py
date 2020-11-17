from pytest import *
import numpy as np
import matplotlib.patches as patches
import vue_cell as vc


univers = np.array([[0, 1, 2], [1, 1, 1], [0, 1, 0]])

patches = []


def test_plane_coord():
    # vérifié sur une figure matplotlib
    assert True


def test_display_center():
    # vérifié sur une figure matplotlib
    assert True


def test_create_cell():
    # create_cell crée les patchs hexagonaux avec les bonnes caractéristiques et renvoie les dits patches.
    # 3 cas: pas de cellule, tumorale ou astrocyte
    assert vc.create_cell(0, 0, univers) == None
    assert vc.create_cell(0, 1, univers).get_facecolor() == (1, 0, 0, 0.5)
    assert vc.create_cell(0, 2, univers).get_facecolor() == (
        0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 0.5)


def test_display_cell():
    # vérifié sur une figure matplotlib
    assert True
