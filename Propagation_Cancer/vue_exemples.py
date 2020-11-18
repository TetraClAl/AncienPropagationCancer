from controleur_initialisation import *
from vue_cell import *
from vue_patch import *
from vue_univers import *
from vue_animation import *
from controleur_choix_uniforme import *
from vue_storage import *
import copy as c
from controleur_regle import *

univers = np.array([[1, 1, 2], [1, 1, 1], [2, 1, 2]])


def display_vue_cell():
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    plt.axis([-1, 10, -1, 10])
    univers = np.array([[1, 1, 2], [1, 1, 1], [2, 1, 2]])
    for y in range(3):
        display_cell(0, y, univers, ax)
        display_center(1, y, fig)
    plt.show()


def display_init():
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    # plt.axis([-1, 10, -1, 10])
    x = 3
    y = 0
    centre = [x, y, 2, 2]

    univers = init_univers(6, 6, centre)

    display_univers(univers, ax)
    display_center(x, y, fig)
    plt.show()


def display_vue_patch():
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    plt.axis([-1, 10, -1, 10])
    univers = np.array([[0, 1, 2], [1, 0, 1], [2, 1, 2]])
    for x in range(3):
        for y in range(3):
            display_patch(x, y, univers, ax)
            display_center(1, y, fig)
    plt.show()


def exemple_display_full():
    univ = np.eye(10)
    for x in range(10):
        univ[0][x] = 1
        univ[5][x] = 2
    # print(univ)
    display_full(univ)


def display_uniforme():
    univers = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    env = create_env(univers)
    omeg = omega(env, 3)
    print(omeg)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 3, 1)
    plt.axis([-1, 10, -1, 10])
    plane = init_plane(omeg[0], ax1)

    ax2 = fig.add_subplot(1, 3, 2)
    plt.axis([-1, 10, -1, 10])
    plane2 = init_plane(omeg[0], ax2)
    refresh_plane(plane2, omeg[1])

    ax3 = fig.add_subplot(1, 3, 3)
    plt.axis([-1, 10, -1, 10])
    plane3 = init_plane(omeg[0], ax3)
    refresh_plane(plane3, omeg[2])

    plt.show()


# display_uniforme()


def display_plane():
    fig = plt.figure(figsize=(6, 6))

    univers = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    env = create_env(univers)
    omeg = omega(env, 2)

    ax1 = fig.add_subplot(1, 2, 1)
    plt.axis([-1, 10, -1, 10])
    plane = init_plane(omeg[0], ax1)

    ax2 = fig.add_subplot(1, 2, 2)
    plt.axis([-1, 10, -1, 10])
    plane2 = init_plane(omeg[0], ax2)
    refresh_plane(plane2, omeg[1])

    print(omeg)
    plt.show()


# display_plane()


def display_animation():
    univers = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    env = create_env(univers)

    animation(env, 10)


# display_animation()

def test_display_cell():
    fig_test = plt.figure()
    ax2 = plt.subplot()
    plt.axis([-1, 10, -1, 10])
    display_cell(0, 1, univers, ax2)
    assert check_figures_equal(fig_ref, fig_test)


def display_homotype():
    centre = [7, 7, 2, 2]
    env = init_univers(14, 14, centre)

    figure = plt.figure()
    plt.scatter(15, 7*sqrt(3))
    animation(env, centre, 100, fig=figure, interv=1900)
