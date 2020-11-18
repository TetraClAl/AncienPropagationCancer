from controleur_regle_homotype import *
import numpy as np



def test_dep_homotype():

    # test où ca ne bouge pas car pas de cellules tumorales voisines
    env = init_univers(3, 3, (1, 1, 1, 1), 0)
    p = 1
    dep_homotype(env, 1, 1, p)
    A = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert np.array_equal(env[0], A)

    # test pas de voisins libres
    env2 = init_univers(3,3, (0,0,3,3), 0)
    dep_homotype(env2, 1, 1, p)
    B = np.array([[1,1,1],[1,1,1],[1,1,1]])
    assert np.array_equal(env2[0], B)

    # test déplacement aléatoire 
    p = 0
    env3 = init_univers(3, 3, (1, 1, 1, 2), 0)
    dep_homotype(env3, 1, 1, p)
    C = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 1]])
    D = np.array([[0, 0, 0], [1, 0, 1], [0, 0, 0]])
    F = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    res = False
    for x in [C, D, F]:
        if np.array_equal(x, env3[0]):
            res = True
    
    assert res


def test_dep_homotype_all():

    env = init_univers(3, 3, (1, 1, 1, 1), 0)
    p = 0
    # liste des issues possibles
    A = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 0]])
    B = np.array([[0, 0, 0], [1, 1, 0], [0, 0, 0]])
    C = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0]])
    D = np.array([[0, 0, 0], [0, 1, 0], [0, 1, 0]])
    E = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]]) 
    F = np. array([[0, 0, 0], [0, 1, 2], [0, 0, 0]])

    env = dep_homotype_all(env, p, (1, 1, 1, 1))
    res = False
    # on voit si ce qu'on obtient fait bien partie des issues
    for x in [A, B, C, D, E, F]:
        if np.array_equal(env[0], x):
            res = True
    
    assert res








