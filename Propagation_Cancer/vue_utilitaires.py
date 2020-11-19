from math import *
from matplotlib import *
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal
from data_main import *
import numpy as np
import copy as c
import tkinter as tk

from controleur import *


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


def get_color(x, y, univers, centre):
    c = liste_centre(centre)
    if [x, y] in c:
        return 3
    else:
        return get_cell(x, y, univers)
# couleur en RGB, mi-transparente, selon l'état:
# 0 = vide = blanc
# 1= tumorale = gris
# 2= astrocyte = saumon
# 3= tumorale centrale = rouge foncé


couleur = [(1.0, 1.0, 1.0, 0.5), (0.0, 0.0, 0.0, 0.3), (1.0,0.38823529411764707, 0.2784313725490196, 0.4), (0.0, 0.0, 0.0, 1.0)]
