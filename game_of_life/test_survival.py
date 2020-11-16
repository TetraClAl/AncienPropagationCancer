from survival import *
from pytest import *

from display import *


def test_evaluer_voisines():
    univers = init_univers(5, 5, seeds["barre2"])

    assert evaluer_voisines(univers, 0, 0) == 2
    assert evaluer_voisines(univers, 1, 0) == 1
    assert evaluer_voisines(univers, 2, 0) == 2

    assert evaluer_voisines(univers, 0, 1) == 3
    assert evaluer_voisines(univers, 1, 1) == 2
    assert evaluer_voisines(univers, 2, 1) == 3

    assert evaluer_voisines(univers, 0, 2) == 2
    assert evaluer_voisines(univers, 1, 2) == 1
    assert evaluer_voisines(univers, 2, 2) == 2


def test_survival():
    # Test principal
    univers = init_univers(5, 5, seeds["barre2"])
    assert survival(univers, 0, 0) == 0
    assert survival(univers, 1, 0) == 0
    assert survival(univers, 2, 0) == 0

    assert survival(univers, 0, 1) == 1
    assert survival(univers, 1, 1) == 1
    assert survival(univers, 2, 1) == 1

    assert survival(univers, 0, 2) == 0
    assert survival(univers, 1, 2) == 0
    assert survival(univers, 2, 2) == 0

    # Cette deuxième partie du test permet de tester le cas où une cellule suffoque
    univers2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert survival(univers2, 1, 1) == 0


def test_generation():
    # le motif barre2 donne le motif barre au tour suivant
    univers = init_univers(5, 5, seeds["barre2"])
    r = generation(univers)

    # display_universe(r)

    comp = seeds["barre"]

    # display_universe(comp)

    for i in range(2):
        for j in range(2):
            assert comp[i][j] == r[i][j]


def test_game_life_simulation():
    # Simulation
    univers = init_univers(5, 5, seeds["barre2"])
    game_life_simulation(univers, 3)

    # Comparaison
    comp = seeds["barre"]
    for i in range(2):
        for j in range(2):
            assert comp[i][j] == univers[i][j]

    # Test cas stable
    univers2 = init_univers(5, 5, seeds["boat"])
    game_life_simulation(univers2, 20)

    # Comparaison
    comp = seeds["boat"]
    for i in range(3):
        for j in range(3):
            assert comp[i][j] == univers2[i][j]


def test_game_life_simulation_animated():
    # Simulation
    univers = init_univers(5, 5, seeds["barre2"])
    anim = game_life_simulation_animated(univers, 4)

    # Comparaison
    for i in range(3):
        for j in range(3):
            assert univers[i][j] == anim[4][i][j]
