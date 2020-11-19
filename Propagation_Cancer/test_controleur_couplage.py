from controleur_couplage import *
from vue_animation import *
from pytest import *
import numpy as np

centre = [1, 1, 1, 1]


centre2 = [0, 0, 3, 3]
env_no_astros = init_univers(3, 3, centre, Pocc=0)
env_full_astros = init_univers(3, 3, centre, Pocc=1)
env_full_centre = init_univers(6, 6, centre2, Pocc=0)

env_trou = init_univers(4, 4, centre, Pocc=0)
for (x, y) in get_adj(1, 1, env_trou[0])[1:]:
    set_cell(x, y, 2, env_trou)


# Affiche les univers pour vérifier la configuration


def display_init(env, centre):
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    # plt.axis([-1, 10, -1, 10])
    x = 1
    y = 1

    plane = create_plane(env, ax)
    refresh_plane(plane, env[0], centre)
    # display_univers(univers, ax)
    display_center(x, y, fig)
    plt.show()


#jonction_duo(env_full_centre, centre2, 0, None)
#display_init(env_full_centre, centre2)


def test_jonct_duo_evaluation():

    # cellule tumorale isolée
    voisines = get_adj(1, 1, env_no_astros[0])
    assert jonct_duo_evaluation(env_no_astros, 1, 1) == (
        voisines, [], [], voisines)

    # cellule tumorale entourée d'astrocytes
    voisines2 = get_adj(1, 1, env_full_astros[0])
    assert jonct_duo_evaluation(env_full_astros, 1, 1) == (
        [], voisines2, [], voisines2)

    # cellule entourée de tumorales
    assert jonct_duo_evaluation(env_full_centre, 1, 1) == (
        [], [], [], [])


def test_jonct_duo_move():
    # la cellule entourée de tumorale ne peut pas bouger
    jonct_duo_move(env_full_centre, 1, 1, 0.5, 0.5)
    test = np.array(env_full_centre[0] ==
                    init_univers(6, 6, centre2, Pocc=0)[0])
    assert test.all()

    # cellule entourée d'astrocyte. Elle ne doit pas rester à cote de ses voisines cancéreuses ni aller sur un astrocyte. Donc elle ne bouge pas.
    jonct_duo_move(env_full_astros, 1, 1, p=None, q=0)
    test2 = np.array(env_full_astros[0] ==
                     init_univers(3, 3, centre, Pocc=1)[0])
    assert test2.all()

    # cellule entourée d'astrocyte qui doit bouger sur un astrocyte voisin
    jonct_duo_move(env_full_astros, 1, 1, 1, 1)
    voisines = get_adj(1, 1, env_full_astros[0])
    count = 0
    for (x, y) in voisines:
        if get_cell(x, y, env_full_astros[0]) == 1:
            count += 1
    # la cellule a bougé sur une voisine, sans se multiplier
    assert count == 1
    # le site initial est laissé vide
    assert get_cell(1, 1, env_full_astros[0]) == 0
