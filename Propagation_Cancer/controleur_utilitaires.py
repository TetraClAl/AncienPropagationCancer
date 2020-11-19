import random as rd
import numpy as np
from random import randint
from random import sample
from random import choice
from data_main import *


def liste_centre(centre):
    """permet d'obtenir les coordonnées (x,y) de tous les sites occupant le centre 
    centre est un quadruplet donnant les coordonées du centre du centre, la largeur selon x puis y"""
    liste_centre = []
    x, y, l, L = centre
    for i in range(l):
        for j in range(L):
            liste_centre.append((x+i, y+j))
    return liste_centre


def migration_aléatoire(i, j, l, env):
    """ fait migrer la cellule tumorale (i,j) sur un site de l choisit aléatoirement. l est une liste de coordonnées (x,y) """
    if l != []:
        choix = choice(l)  # choisit aléatoirement un élément de l
        # si ce site n'est pas deja occupé par une cellule tumorale, (i,j) peut bouger
        if get_cell(choix[0], choix[1], env[0]) != 1:
            # on met un 1 sur le site choisit
            set_cell(choix[0], choix[1], 1, env)
            set_cell(i, j, 0, env)  # on remet un 0 sur le site laissé vacant


def tri_voisins(x, y, univers):
    """Réparti les voisins entre 4 listes selon leur état: vides, tumorales, astrocytes, libres """
    vides = []
    tumorales = []
    astrocytes = []
    libres = []  # les sites vides ou occupés par un astrocyte
    for direction in range(6):
        i, j = voisin_dir([x, y], direction)
        etat = get_cell(i, j, univers)

        if etat == 0:
            vide += [(i, j)]
            libres += [(i, j)]
        elif etat == 1:
            tumorales += [(i, j)]
        else:
            astrocytes += [(i, j)]
            libres += [(i, j)]

    return vides, tumorales, astrocytes, libres
