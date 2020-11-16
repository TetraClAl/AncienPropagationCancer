from data_main import *
import numpy as np
from random import randint
from random import sample

def ajout_astrocytes(univers, Pocc):

    (a, b) = np.shape(univers)

    #nombre réel d'astrocytes
    n = int(Pocc*a*b)

    coords = [[i,j] for i in range(a) for j in range(b)]

    #on choisit aléatoirement la répartition des astrocytes
    astro = sample(coords, n) 

    #on remplace les cellules vides par des astrocytes
    for coord in astro:
        if get_cell(coord[0], coord[1], univers) == 0:
            set_cell(coord[0], coord[1], 2, univers)

    return univers

def init_univers(tx, ty, init_tumor = np.array([[1]]), Pocc = 0.5, cx = None, cy = None):

    univers = create_univers(tx, ty)
    (a, b) = np.shape(init_tumor)

    if cx == None :
        cx = (tx - a)//2
    if cy == None :
        cy = (ty - b)//2

    # on implémente la tumeur initiale
    
    for i in range(a):
        for j in range(b):
            set_cell(i + cx, j + cy, get_cell(i, j, init_tumor), univers)

    #on ajoute les astrocytes
    return ajout_astrocytes(univers, Pocc)


