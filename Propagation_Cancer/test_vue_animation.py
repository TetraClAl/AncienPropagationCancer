from pytest import *
from vue_animation import *


univers = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
env = create_env(univers)

lis = omega(env, 2)

fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(1, 1, 1)
plt.axis([-1, 10, -1, 10])
plane = create_plane(3, 3, ax1)

l2 = redim(plane)

print(l2[0].get_facecolor())


def test_omega():
    assert len(lis) == 2
    assert lis[0][0][0] == 0
    assert type(lis[0]) == numpy.ndarray

    # il n'y a qu'une cellule, même si elle bouge
    assert np.sum(lis[0]) == 1


def test_create_plane():

    assert len(plane) == 3

    assert len(plane[0]) == 3

    assert plane[0][0].get_facecolor() == couleur[0]


def test_refresh_plane():
    fig = plt.figure(figsize=(6, 6))
    ax1 = fig.add_subplot(1, 1, 1)
    plt.axis([-1, 10, -1, 10])
    plane = create_plane(3, 3, ax1)

    refresh_plane(plane, lis[1])

    assert len(plane) == 3
    assert len(plane[0]) == 3


def test_redim():

    assert type(l2) == list
    assert len(l2) == 9


def test_animation_update():
    up = animation_update(1, lis, plane)

    # le premier element est le patch en (0,0)
    col = up[0].get_facecolor()
    etat = lis[1][0][0]
    assert col == couleur[etat]
