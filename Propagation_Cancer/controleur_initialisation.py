from controleur_regen import regen_centre
from random import sample
from random import randint
import numpy as np
from data_main import *


def ajout_astrocytes(univers, Pocc):

    (a, b) = np.shape(univers)

    # nombre réel d'astrocytes
    n = int(Pocc*a*b)

    coords = [[i, j] for i in range(a) for j in range(b)]

    # on choisit aléatoirement la répartition des astrocytes
    astro = sample(coords, n)

    # on remplace les cellules vides par des astrocytes
    for coord in astro:
        if get_cell(coord[0], coord[1], univers) == 0:
            set_cell(coord[0], coord[1], 2, univers)

    return univers


def init_univers(tx, ty, centre, init_tumor=np.array([[1]]), Pocc=0.5, cx=None, cy=None):

    univers = create_univers(tx, ty)
    (a, b) = np.shape(init_tumor)

    if cx == None:
        cx = (tx - a)//2
    if cy == None:
        cy = (ty - b)//2

    # on implémente la tumeur initiale (ie la tumeur à t=0)

    for i in range(a):
        for j in range(b):
            set_cell(i + cx, j + cy, get_cell(i, j, init_tumor), univers)

    # on vérifie que le centre est bien composé de cellules tumorales
    regen_centre(univers, centre[0], centre[1], centre[2], centre[3])

    # on ajoute les astrocytes
    return ajout_astrocytes(univers, Pocc)

### A l'état initial, on a un centre composé de cellules tumorales, pouvant être complété par une forme particulière init_tumor ###
