from controleur_initialisation import *
from controleur_regle_homotype import *
from controleur_jonction_heterotype import *
import numpy as np

def taux_occupation_tumeur(univers):
    (n, m) = np.shape(univers)
    total = n*m
    tumeur = 0
    for i in range(n):
        for j in range(m):
            if get_cell(i, j, univers) == 1:
                tumeur += 1
    return tumeur/total

def taux_occupation_astrocytes(univers):
    (n, m) = np.shape(univers)
    total = n*m
    astrocytes = 0
    for i in range(n):
        for j in range(m):
            if get_cell(i, j, univers) == 2:
                astrocytes += 1
    return astrocytes/total

def distance(x, y):
    return np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def plus_grande_distance(env, centre):
    dx = centre[0]
    dy = centre[1]
    tx = centre[2]
    ty = centre[3]
    m = ((dx + dx + tx)//2, (dy + dy + ty)//2) #coordonnées du milieu du centre de la tumeur
    tumorales = tri_cells(env[0])[1]
    res = 0
    point = m
    for coord in tumorales:
        d = distance(m, coord)
        if d > res :
            res = d
            point = coord
    return res, point

    