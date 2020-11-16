import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# Fonction pour obtenir la valeur d'une cellule
def get_univers(univers, x, y):
    x = int(x) % len(univers)
    y = int(y) % len(univers[0])
    return univers[x][y]


# Fonction pour ajuster la valeur d'une cellule
def set_univers(univers, x, y, value):
    x = int(x) % len(univers)
    y = int(y) % len(univers[0])
    univers[x][y] = value
    return value


# Fonction de mélange n, la cellule est vivante si et seulement si n est vivante
def melange_n(a, n):
    return n


# Fonction de mélange ou, la cellule est vivante si a est vivante ou si n est vivante
def melange_or(a, n):
    if a == 1:
        return 1
    if n == 1:
        return 1
    return 0


def ajouter_pattern(univers, pattern, x, y, fonction_addition=melange_n):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            val = fonction_addition(get_univers(
                univers, x + i, y + j), pattern[i][j])
            set_univers(univers, x + i, y + j, val)


# Toutes ok avec np
