import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Rectangle
import sys

# https://gitlab-cw5.centralesupelec.fr/victor.lebrun/jeudelavie_groupe5/-/wikis/display.py

# Mettre à 0 pour afficher, mettre à 1 pour ne pas afficher pendant les tests
display_debug = 0
if "pytest" in sys.modules:
    display_debug = 1


def display_cell(x, y, ax, xoffset, yoffset):
    """Fonction d'affichage d'une cellule en (x, y), ax correspond au graphe et xoffset, yoffset à la taille du jeu"""
    color = 'r'
    ax.add_patch(Rectangle((x / xoffset, y / yoffset), 1 / xoffset,
                           1 / yoffset, facecolor=color, edgecolor=color))


def display_universe(universe, fdisplay=display_cell):
    """Fonction d'affichage de l'univers"""
    fig, ax = plt.subplots(1)
    xoffset = len(universe)
    yoffset = len(universe[0])

    for i in range(xoffset):
        for j in range(yoffset):
            if universe[i][j] == 1:
                fdisplay(i, j, ax, xoffset, yoffset)

    if display_debug == 0:
        plt.show()
