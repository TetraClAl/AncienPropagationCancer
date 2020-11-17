from pytest import *
from data_advanced import *
from controleur_initialisation import *


def test_voisin_dir():
    # Tests directs
    # Examen visuel recommandé TODO : Ajouter un code pour vérifier rapidement visuellement que tout est en ordre.
    assert voisin_dir((0, 0), 0) == (1, 0)
    assert voisin_dir((0, 1), 1) == (1, 0)


def test_s_get_adj():
    # Calcul
    uni = s_create_univers(4, 4)
    L1 = s_get_adj(0, 1, uni)
    L2 = s_get_adj(1, 0, uni)

    # Listes de comparaison
    L1c = [[0, 0], [1, 0], [1, 1], [1, 2], [0, 2]]
    L2c = [[0, 0], [0, 1], [1, 1], [2, 0]]

    # Vérification longueur
    assert len(L1c) == len(L1)
    assert len(L2c) == len(L2)

    # Vérification éléments
    for e in L1c:
        # On vérifie si e est dans L1
        test = False
        for c in L1:
            if c[0] == e[0] and c[1] == e[1]:
                test = True
        assert test  # Sinon assert
    for e in L2c:  # Idem, TODO : refactorisation avec fonction
        test = False
        for c in L2:
            if c[0] == e[0] and c[1] == e[1]:
                test = True
        assert test


def test_global():
    univers = create_univers(5, 5)
    env = [univers, []]

    x1 = 1
    y1 = 2
    x2 = 2
    y2 = 2
    x3 = 2
    y3 = 3

    set_cell(x1, y1, 1, env)
    set_cell(x2, y2, 1, env)
    set_cell(x3, y3, 1, env)

    set_cell(x2, y2, 0, env)

    index = s_get_groupe(x1, y1, env)
    adj = env[1][index][1]
    for e in adj:
        univers[e[0], e[1]] = 2

    index = s_get_groupe(x3, y3, env)
    adj = env[1][index][1]
    for e in adj:
        univers[e[0], e[1]] = 2

    """if False:
        from vue_univers import *
        display_univers(univers)
        plt.show()"""

    comp = [np.array([[0, 2, 2, 2, 0],
                      [0, 2, 1, 2, 0],
                      [0, 0, 2, 1, 2],
                      [0, 0, 2, 2, 2],
                      [0, 0, 0, 0, 0]]), [[[[2, 3]], [[3, 3], [3, 2], [2, 2], [1, 3], [2, 4], [3, 4]]], [[[1, 2]], [[2, 2], [1, 1], [0, 1], [0, 2], [0, 3], [1, 3]]]]]

    assert np.array_equal(comp[0], env[0])

    folder = env[1]
    folcomp = comp[1]

    for i in range(len(folder)):
        for j in range(len(folder[0])):
            assert folder[0][j] == folcomp[0][j]
        for j in range(len(folder[1])):
            assert folder[1][j] == folcomp[1][j]
