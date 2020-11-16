from pytest import *
from vue_cell import *


univers = np.array([[0, 1, 2], [1, 1, 1], [0, 1, 0]])

patches = []


def test_type_cell():
    # renvoie le type de la cellule: "vide", "tumorale", "astrocyte"
    assert type_cell(0, 3, univers) == "tumorale"
    assert type_cell(0, 0, univers) == "vide"
    assert type_cell(0, 1, univers) == "astrocyte"


def test_create_cell():
    # create_cell crée les patchs hexagonaux avec les bonnes caractéristiques et renvoie les dits patches.
    # 3 cas: pas de cellule, tumorale ou astrocyte
