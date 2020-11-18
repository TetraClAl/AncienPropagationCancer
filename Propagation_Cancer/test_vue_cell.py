from pytest import *
from vue_cell import *


univers = np.array([[0, 1, 2], [1, 1, 1], [0, 1, 0]])

# Création d'une figure de référence
fig_ref = plt.figure()
ax = plt.subplot()
plt.axis([-1, 10, -1, 10])
hexagone = patches.RegularPolygon(
    (plane_coord(0, 1)), 6, radius=2/sqrt(3), ec='white', fc='red', alpha=0.5)
ax.add_patch(hexagone)


def test_create_cell():
    # create_cell crée les patchs hexagonaux avec les bonnes caractéristiques et renvoie les dits patches.
    # 3 cas: pas de cellule, tumorale ou astrocyte
    assert create_cell(0, 0, univers) == None
    assert create_cell(0, 1, univers).get_facecolor() == (1, 0, 0, 0.5)
    assert create_cell(0, 2, univers).get_facecolor() == (
        0.5019607843137255, 0.5019607843137255, 0.5019607843137255, 0.5)
