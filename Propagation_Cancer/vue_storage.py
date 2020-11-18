from vue_patch import *
from vue_univers import *
from controleur_initialisation import *
from controleur_choix_uniforme import *
import copy as c
from matplotlib.animation import FuncAnimation


def init_plane_by_state(env):
    "Stocke les patches correspondant à un univers donné par ordre d'état "
    univ = env[0]
    v, t, a = tri_cells(univ)

    plane = []

    # vides
    for (x, y) in v:
        patch = create_patch(x, y, 0)
        ax.add_patch(patch)
        ligne = [patch]
        plane += [ligne]

    # astrocytes
    for (x, y) in a:
        patch = create_patch(x, y, 2)
        ax.add_patch(patch)
        ligne = [patch]
        plane += [ligne]

    # tumorales
    for (x, y) in a:
        patch = create_patch(x, y, 1)
        ax.add_patch(patch)
        ligne = [patch]
        plane += [ligne]

    return plane


def init_plane(univ, ax):
    "Création de l'image initiale et renvoie le tableau des patches, utilisé par les fonctions d'animation"
    n, m = np.shape(univ)

    plane = []

    for x in range(n):
        line = []
        for y in range(m):
            etat = get_cell(x, y, univ)
            patch = create_patch(x, y, etat)
            ax.add_patch(patch)
            line += [patch]

        plane += [line]

    return plane


def animation_init(omega, ax):
    plane = init_plane(omega[0], ax)
    return redim(plane)


def test_init_plane():
    fig = plt.figure(figsize=(6, 6))
    ax1 = fig.add_subplot(1, 1, 1)
    plt.axis([-1, 10, -1, 10])
    plane = init_plane(univers, ax1)

    assert len(plane) == 3
    assert len(plane[0]) == 3

    #assert plane[0][0].get_facecolor == couleur[0]
    #assert plane[1][1].get_facecolor == couleur[1]
