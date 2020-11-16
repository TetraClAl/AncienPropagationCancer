import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from survival import game_life_simulation_animated
import sys
from init_univers import *

# https://gitlab-cw5.centralesupelec.fr/victor.lebrun/jeudelavie_groupe5/-/wikis/animation.py

# Mettre à 0 pour afficher, mettre à 1 pour ne pas afficher pendant les tests
display_animated_debug = 0
if "pytest" in sys.modules:
    display_animated_debug = 1


def create_plane(dimension, ax, couleur='r'):
    """ Créée un plane de dimension (x, y) et retourne le tableau plane[x][y] contenant les patches. """
    # Initialisation des variables
    plane = []
    x, y = dimension
    taillex = 1 / x  # Taille inversée pour avoir une fenêtre sur [0,1]²
    tailley = 1 / y
    color = couleur

    # Boucle de création
    for i in range(x):
        ligne = []
        for j in range(y):
            # Rectangle((coordonnées coin inferieur gauche (tuple)), longueur en x, longueur en y, couleur intérieure, couleur des bordures)
            rectangle = Rectangle(
                (i / x, j / y), taillex, tailley, facecolor=color, edgecolor=color)
            ax.add_patch(rectangle)  # Ajout du patch à l'écran
            rectangle.set_visible(False)  # Les patchs sont cachés par défaut
            ligne += [rectangle]

        plane += [ligne]

    # Retour
    return plane


def refresh_plane(plane, univers):
    """ Ajuste la visibilité des patches de plane en fonction du statut des cellules de univers. """
    for i in range(len(plane)):
        for j in range(len(plane[0])):
            # Permet de cacher ou montrer individuellement chaque cellule
            plane[i][j].set_visible(univers[i][j] == 1)


def redim(plane):
    """ Transforme un tableau 2D en tableau 1D. """
    # Cette fonction sert à transformer le tableau 2D de cellules à afficher en un tableau 1D pour la fonction d'animation.
    liste = []
    for e in plane:
        liste += e
    return liste


def animation_init(animation, plane):
    """ Fonction d'initialisation de l'animation. """
    # TODO : Tester si cette fonction est utile
    refresh_plane(plane, animation[0])
    return redim(plane)


def animation_update(i, animation, plane):
    """ Fonction d'animation. """
    # La fonction va ajuster la visibilité de chaque cellule, elle sélectionna la bonne frame parmis le tableau animation. La variable i indique le numéro de frame.
    refresh_plane(plane, animation[i])
    return redim(plane)


def display_animated_universe(univers, n=20, _interval=300, couleur='r', save=False):
    """Fonction d'affichage de l'univers animé sur n itérations"""
    # Préparation des données
    fig, ax = plt.subplots(1)
    tx = len(univers)
    ty = len(univers[0])

    # Création du plane
    plane = create_plane((tx, ty), ax, couleur)

    # Calcul de l'animation
    animation = game_life_simulation_animated(univers, n)

    # Préparation des lambdas: fonctions d'initialisation et d'itérations pour l'animation
    def f_update(i): return animation_update(i, animation, plane)
    def f_init(): return animation_init(animation, plane)

    # Animation
    ani = FuncAnimation(fig, f_update, frames=(n + 1),
                        init_func=f_init, blit=True, interval=_interval, repeat=True)

    # Affichage
    if display_animated_debug == 0:
        plt.show()

    # Sauvegarde
    if save == True:
        ani.save('animation.gif')





