from controleur_regen import regen_centre
from controleur_utilitaires import *


def ajout_astrocytes(env, Pocc):
    """Crée la couche statique d'astrocytes sains, aléatoirement avec une densité Pocc"""
    (a, b) = np.shape(env[0])

    # nombre réel d'astrocytes
    n = int(Pocc*a*b)

    coords = [[i, j] for i in range(a) for j in range(b)]

    # on choisit aléatoirement la répartition des astrocytes
    astro = sample(coords, n)

    # on remplace les cellules vides par des astrocytes
    for coord in astro:
        if get_cell(coord[0], coord[1], env[0]) == 0:
            set_cell(coord[0], coord[1], 2, env)

    return env


def init_univers(tx, ty, centre, Pocc=0.5, init_tumor=None, cx=None, cy=None):
    """Initie un environnement de taille tx*ty avec Pocc caractérisant la couche d'astrocyte. init_tumor rajoute une forme en plus du centre, dont le coin haut gauche est placée en (cx,cy)"""
    # centre est une liste de 4 valeurs : les coordonnées du point en haut à gauche du centre,
    # la longeur selon x et selon y
    # cx et cy sont les coordonnées du point a partir du quel on introduit la forme init_tumor
    univers = create_univers(tx, ty)
    env = create_env(univers)
    
    if init_tumor is not None : #on veut rajouter une forme en plus du centre
        (a, b) = np.shape(init_tumor)

        # si rien n'est précisé, on met init_tumor au milieu
        if cx == None:
            cx = (tx - a)//2
        if cy == None:
            cy = (ty - b)//2

        # on implémente la tumeur initiale (ie la tumeur à t=0)
        # print(init_tumor)
        for i in range(a):
            for j in range(b):
                set_cell(i + cx, j + cy, get_cell(i, j, init_tumor), env)

    # on vérifie que le centre est bien composé de cellules tumorales
    regen_centre(env, centre)

    # on ajoute les astrocytes
    return ajout_astrocytes(env, Pocc)


### A l'état initial, on a un centre composé de cellules tumorales, pouvant être complété par une forme particulière init_tumor ###
