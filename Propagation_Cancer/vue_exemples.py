from vue_univers import *
from vue_animation import *

from vue_storage import *


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
# display_vue_cell()


def display_init():
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    # plt.axis([-1, 10, -1, 10])
    x = 3
    y = 0
    centre = [x, y, 2, 2]

    env = init_univers(6, 6, centre)

    display_univers(univers, ax)
    display_center(x, y, fig)
    plt.show()

# display_init()


def display_vue_patch():
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    plt.axis([-1, 10, -1, 10])
    univers = np.array([[0, 1, 2], [1, 0, 1], [2, 1, 2]])
    c = [(0, 1)]
    display_patch(0, 0, 0, ax)
    display_patch(0, 1, 1, ax, centre=((0, 1) in c))
    display_patch(1, 0, 1, ax)
    plt.show()


# display_vue_patch()


def exemple_display_full():
    """affiche un univers avec une couche d'astrocytes, et un centre de 4 cellules"""
    centre = [2, 2, 2, 2]
    env = init_univers(6, 6, centre)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    plt.axis([-1, 10, -1, 10])
    display_full(env, centre, ax1)


# exemple_display_full()


def display_uniforme():
    """affiche 3 images: l univers vide; l'univers avec des astrocytes et le centre; l'univers avec des astros, le centre, et des cellules ayant migré (choix uniforme)"""
    centre = [2, 2, 2, 2]
    env = init_univers(6, 6, centre)
    omeg = omega(env, centre, 3)
    # print(omeg)
    print(liste_centre(centre))

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 3, 1)
    plt.axis([-1, 10, -1, 10])
    plane = create_plane(env, centre, ax1)
    # refresh_plane(plane, omeg[0],centre)

    ax2 = fig.add_subplot(1, 3, 2)
    plt.axis([-1, 10, -1, 10])
    plane2 = create_plane(env, centre, ax2)
    refresh_plane(plane2, omeg[0], centre)

    ax3 = fig.add_subplot(1, 3, 3)
    plt.axis([-1, 10, -1, 10])
    plane3 = create_plane(env, centre, ax3)
    refresh_plane(plane3, omeg[1], centre)

    plt.show()


display_uniforme()


def display_plane():
    fig = plt.figure()
    # plt.scatter(15, 7*sqrt(3))

    centre = [7, 7, 2, 2]
    env = init_univers(14, 14, centre)
    omeg = omega(env, centre, 100, dep_homotype_all,
                 p=0.5)

    ax1 = fig.add_subplot(1, 2, 1)
    plt.axis([-1, 10, -1, 10])
    plane = create_plane(env, centre, ax1)

    ax2 = fig.add_subplot(1, 2, 2)
    plt.axis([-1, 10, -1, 10])
    plane2 = create_plane(env, centre, ax2)
    refresh_plane(plane2, omeg[0], centre)

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

    animation(env, centre, 100, dep_homotype_all,
              p=0.5, fig=figure, interv=1900)


# display_homotype()
