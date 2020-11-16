from seeds import *
from utilitaires_univers import *

# https://gitlab-cw5.centralesupelec.fr/victor.lebrun/jeudelavie_groupe5/-/wikis/init_univers.py


def init_univers(tx, ty, seed=seeds["none"], x=0, y=0):
    """ Fonction créant un univers de taille (tx, ty), en plaçant une graine en (x, y) de type seed (envoyée sous forme de tableau 2D binaire). """
    # Initialisation avec des 0
    univers = []
    for i in range(tx):
        L = []
        for j in range(ty):
            L += [0]
        univers += [L]

    # Ajout de l'élément de départ
    ajouter_pattern(univers, seed, x, y)

    # Retour
    return univers


def create_univers():
    """ Fonction pour créer un univers en interragissant avec l'utilisateur via l'interface console. """
    # Gestion de l'interface
    print("== Creation de l'univers ==")
    print("= Taille de l'univers =")
    tx = int(input("Entrez x "))
    ty = int(input("Entrez y "))

    print("= Motif de départ et position =")
    x = int(input("Entrez x "))
    y = int(input("Entrez y "))
    seed = input("Entrez nom motif ")

    # Gestion des données
    return init_univers(tx, ty, seeds[seed], x, y)
