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


def tri_cells(univers):
    "Renvoie les coordonnées des cellules triées par états, en trois listes"
    n, m = np.shape(univers)
    vides = []
    tumorales = []
    astrocytes = []
    for x in range(n):
        for y in range(m):
            etat = get_cell(x, y, univers)
            if etat == 0:
                vides += [(x, y)]
            elif etat == 1:
                tumorales += [(x, y)]
            else:
                astrocytes += [(x, y)]
    return vides, tumorales, astrocytes


def display_full(univers, show=True):

    # création d'une nouvelle figure
    fig = plt.figure(figsize=(6, 6))
    ax = plt.subplot(1, 1, 1)
    # fenêtrage à réflichir pour qu'il soit plus adaptatif
    plt.axis([-1, 20, -1, 20])

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
    display_univers(univers,1)
    plt.show()
