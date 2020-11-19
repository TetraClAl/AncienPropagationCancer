from pytest import *
from controleur_utilitaires import *


def test_liste_centre():
    univers = create_univers(5, 5)
    env = create_env(univers)
    l = liste_centre((2, 2, 2, 3))
    A = [[2, 2], [2, 3], [2, 4], [3, 2], [3, 3], [3, 4]]
    assert np.array_equal(l, A)
