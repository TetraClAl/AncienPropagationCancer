from pytest import *
from controleur_utilitaires import *
from controleur_initialisation import *
from vue_univers import *

centre = [2, 2, 2, 1]
env = init_univers(5, 5, centre, Pocc=0)
l = liste_centre(centre)

print(env[0])
print(get_adj(2, 2, env[0]))

fig = plt.figure()
ax = plt.subplot()
display_full(env, centre, ax)


def test_liste_centre():
    A = [(2, 2), (3, 2)]
    assert np.array_equal(l, A)


def tri_voisins():
    vides, tumorales, astrocytes, libres = tri_voisins(2, 2, env[0])
    assert libres == vides
    assert astrocytes == []
    assert tumorales == [(1, 2)]


# def test_migration_aleatoire():
