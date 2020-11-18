from pytest import *
from vue_patch import *

univers = np.array([[0, 1, 2], [1, 1, 1], [0, 1, 0]])


def test_create_patch():
    vide = create_patch(0, 0, 0)
    tumor = create_patch(0, 1, 1)
    astroc = create_patch(0, 2, 2)

    # vide: blanc
    assert vide.get_facecolor() == couleur[0]

    # tumoral: rouge
    assert tumor.get_facecolor() == couleur[1]

    # astrocyte: gris, mi transparent
    assert astroc.get_facecolor() == couleur[2]


def test_display_patch():
    # vérifié sous matplotlib
    # TODO
    assert True
