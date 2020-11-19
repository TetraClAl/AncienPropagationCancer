from controleur_initialisation import *
from controleur_regle_homotype import *
from controleur_jonction_heterotype import *
from data_main import *
import numpy as np

def taux_occ_tumeur(univers):
    """ Donne le taux d'occupation des cellules tumorales """
    (n, m) = np.shape(univers)
    total = n*m
    tumeur = 0
    for i in range(n):
        for j in range(m):
            if get_cell(i, j, univers) == 1:
                tumeur += 1
    return tumeur/total

def taux_occ_astro(univers):
    """ Donne le taux d'occupation des astrocytes """
    (n, m) = np.shape(univers)
    total = n*m
    astrocytes = 0
    for i in range(n):
        for j in range(m):
            if get_cell(i, j, univers) == 2:
                astrocytes += 1
    return astrocytes/total

def distance(x, y):
    """ Renvoie la distance entre deux points du plan """
    return np.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def plus_grande_distance(env, centre):
    """ Renvoie la plus grande distance entre les cellules tumorales et le centre, et le point qui le vérifie """
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


def taux_occ_it(env, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):
    """ Renvoie une liste contenant le taux de cellules tumorales et le taux d'astrocytes à chaque itération """
    res = [[taux_occ_tumeur(env[0]), taux_occ_astro(env[0])]]

    for i in range(iterations):
        function(env, centre, p, q)
        res.append([taux_occ_tumeur(env[0]), taux_occ_astro(env[0])])
    return res

def plus_grande_distance_it(env, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):
    """ Renvoie une liste contenant la plus grande distance entre une cellule tumorale et le centre à chaque itération """
    res = [plus_grande_distance(env, centre)]
    for i in range(iterations):
        function(env, centre, p, q)
        res.append(plus_grande_distance(env, centre))
    return res


def moyenne(liste):
    n = len(liste)
    res = 0
    for i in range(n):
        res += liste[i]
    return res/n



def moyenne_occ(env, n, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):
    """ Renvoie la moyenne des taux d'occupations sur n échantillons à chaque itération """
    l = []
    res = []
    for k in range(n):
        newenv = copy_env(env)
        l.append(taux_occ_it(newenv, iterations, centre, function, p, q))
    for i in range(iterations):
        m0 = []
        m1 = []
        for k in range(n):
            m0.append(l[k][i][0])
            m1.append(l[k][i][1])
        res.append([moyenne(m0), moyenne(m1)])
    return res


def moyenne_plus_grande_distance(env, n, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):
    l = []
    res = []
    for k in range(n):
        newenv = copy_env(env)
        l.append(plus_grande_distance_it(newenv, iterations, centre, function, p, q))
    for i in range(iterations):
        m = []
        for k in range(n):
            m.append(l[k][i][0])
        res.append(moyenne(m))
    return res






    


    