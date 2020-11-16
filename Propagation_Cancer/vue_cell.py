from math import *
from matplotlib import *
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from data_main import *
import numpy as np

fig = plt.figure(figsize=(6, 6))
# # necessite l'appel à une sous figure
ax = plt.subplot(1, 1, 1)
plt.axis([-1, 10, -1, 10])


def plane_coord(x, y):
    "Retourne les coordonnées dans le plan pour plt"
    yp = (sqrt(3)*y)
    xp = 2*x + y % 2
    return(xp, yp)


def create_cell(x, y, univers):
    """Crée le patch correspondant à la cellule, si le site occupé. Si le site est libre, elle retourne None"""
    value = get_cell(x, y, univers)
    xp, yp = plane_coord(x, y)
    if value == 0:
        return None
    elif value == 1:
        # rouge pour les tumorales
        hexagone = patches.RegularPolygon(
            (xp, yp), 6, radius=2/sqrt(3), ec='white', fc='red', alpha=0.5)
    else:
        hexagone = patches.RegularPolygon(
            (xp, yp), 6, radius=2/sqrt(3), ec='white', fc='gray', alpha=0.5)
    return hexagone


def display_center(x, y):
    "Affiche le centre d'un hexagone"
    xp, yp = plane_coord(x, y)
    plt.scatter(xp, yp, s=4)
    plt.text(xp, yp, "(" + str(x) + ","+str(y)+")")


def display_cell(x, y, univers):
    patch = create_cell(x, y, univers)
    if patch != None:
        ax.add_patch(patch)


# pour l'affichage de l'univers entier
""" def pavage_hex_center(n, m, univers):
    "Pavage hexagonal de n*m patches, avec les centres"
    for x in range(n):
        for y in range(m):
            display_center(x, y)
            if create_cell(x, y, univers) != None:
                hexagone = create_cell(x, y, univers)
                ax.add_patch(hexagone) """


# univers = np.array([[1, 1, 2], [1, 1, 1], [2, 1, 2]])
# for y in range(3):
#     display_cell(0, y, univers)


# plt.show()
