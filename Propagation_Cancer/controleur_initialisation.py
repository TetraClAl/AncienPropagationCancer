from data_main import *
import numpy as np
from random import randint
from random import sample

def ajout_astrocytes(univers, Pocc):

    (a, b) = np.shape(univers)

    #nombre réel d'astrocytes
    n = int(Pocc*a*b)

    coords = [[i,j] for i in range(a) for j in range(len(b))]

    #on choisit aléatoirement la répartition des astrocytes
    astro = sample(coords, n) 

    #on remplace les cellules vides par des astrocytes
    for coord in astro:
        if get_cell(coord, univers) == 0:
            set_cell(coord, 2, univers)

    return univers

def init_univers(ts, tq, init_tumor = np.array([[1]]), Pocc = 0.5):

    univers = create_univers(ts, tq)

    # on implémente la tumeur initiale
    (a, b) = np.shape(init_tumor)
    for i in range(a):
        for j in range(b):
            set_cell((i,j), get_cell((i,j), init_tumor), univers)

    #on ajoute les astrocytes
    return ajout_astrocytes(univers, Pocc)




        









