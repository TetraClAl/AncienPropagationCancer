from math import *
from matplotlib import *
import matplotlib.patches as patches
import matplotlib.pyplot as plt
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
