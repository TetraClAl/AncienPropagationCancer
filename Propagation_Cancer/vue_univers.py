from vue_cell import *
from vue_patch import *


def display_univers(univers, ax):
    n, m = np.shape(univers)
    for x in range(n):
        for y in range(m):
            display_cell(x, y, univers, ax)


# univers = np.array([[1, 1, 2, 1, 1], [1, 0, 1, 0, 1], [2, 1, 2, 1, 2]])
# display_univers(univers)
# plt.show()


def display_full(univers, ax, show=True):

    v, t, a = tri_cells(univers)

    # les derniers objets ajoutés sont affichés au premier plan.
    # On veut les tumorales sur les astrocytes sur les vides

    # Sites vides en arrière plan
    for (x, y) in v:
        display_patch(x, y, 0, ax)

    # astrocytes sain en 2nd plan
    for (x, y) in a:
        display_patch(x, y, 2, ax)

    # tumorales en premier plan
    for (x, y) in t:
        display_patch(x, y, 1, ax)

    if show:
        plt.show()


if __name__ == "__main__":
    univers = np.array([[1, 1, 2, 1, 1], [1, 0, 1, 0, 1], [2, 1, 2, 1, 2]])
<<<<<<< HEAD
    display_univers(univers,1)
=======
    display_full(univers)
>>>>>>> master
    plt.show()
