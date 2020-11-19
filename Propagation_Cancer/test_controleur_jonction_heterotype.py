from controleur_jonction_heterotype import *
from pytest import *

import numpy as np


def test_jonction_heterotype_site():

    # cas où un seul astrocyte avec proba d'aller dans un astrocyte de 1
    univers = np.array([[0, 1, 2], [1, 1, 1], [0, 1, 0]])
    env = create_env(univers)
    jonction_heterotype_site(env, 1, 2, 1)
    A = np.array([[0, 1, 1], [1, 1, 0], [0, 1, 0]])
    assert np.array_equal(env[0], A)
    print('premier test avec astrocyte ok ')

    # cas où un seul site vide avec proba d'aller dans un site vide de 1 (donc q = 0)
    univers = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 0]])
    env = create_env(univers)
    jonction_heterotype_site(env, 1, 1, 0)
    A = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert np.array_equal(env[0], A)
    print('premier test avec site vide ok')


def test_jonction_heterotype():
    # premier test si on a pas de centre
    centre = (0, 0, 0, 0)
    univers = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
    env = create_env(univers)
    jonction_heterotype(env, centre, 0)
    A = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 2]])
    B = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
    C = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 2]])
    D = np.array([[0, 1, 0], [0, 0, 0], [0, 0, 2]])
    res = False
    for x in [A, B, C, D]:
        if np.array_equal(x, env[0]):
            res = True
    assert res


test_jonction_heterotype()
