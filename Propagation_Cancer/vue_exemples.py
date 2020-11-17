from controleur_initialisation import *
from vue_cell import *
from vue_patch import *
from vue_univers import *

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
    #plt.axis([-1, 10, -1, 10])
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
