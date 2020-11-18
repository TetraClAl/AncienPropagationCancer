from math import *
from matplotlib import *
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal
from data_main import *
import numpy as np


def plane_coord(x, y):
    "Retourne les coordonnées dans le plan pour plt"
    yp = (sqrt(3)*y)
    xp = 2*x + y % 2
    return(xp, yp)


def display_center(x, y, fig):
    "Affiche le centre d'un hexagone"
    xp, yp = plane_coord(x, y)
    plt.scatter(xp, yp, s=4)
    plt.text(xp, yp, "(" + str(x) + ","+str(y)+")")


# couleur en RGB, selon l'état:
# #0 = astrocyte = blanc
# 2= astrocyte = gris
# 1= tumorale = rouge
couleur = [(1.0, 1.0, 1.0, 0.5), (1.0, 0.0, 0.0, 0.5), (0.5, 0.5, 0.5, 0.5)]
