from controleur_choix_uniforme import *
from pytest import *


univers = np.array([[0, 1, 2], [1, 1, 1], [0, 1, 0]])
env = create_env(univers)


def count_cell(univers):
    """ renvoie le nombre de site occupé par des cellules tumorales dans l'univers """
    compteur = 0
    for i in range(len(univers)):
        for j in range(len(univers[0])):
            if get_cell(i, j, univers) == 1:
                compteur += 1
    return compteur


def count_cell_voisinage(univers, x, y):
    """renvoie le nombre de sité occupé occupé des cellules tumorales dans le site (x,y) et ses voisins"""
    compteur = 0
    voisins = get_adj(x, y, univers)
    for k in range(len(voisins)):
        a, b = voisins[k]
        if get_cell(a, b, univers) == 1:
            compteur += 1
    if get_cell(x, y, univers) == 1:
        compteur += 1
    return compteur


centre = (0, 0, 0, 0)
a, b = 2, 1
avant_site = count_cell(env[0])
choix_uniforme_site(env, a, b)
apres_site = count_cell(env[0])

assert avant_site == apres_site

avant = count_cell(env[0])
choix_uniforme(env, centre)
apres = count_cell(env[0])

assert avant == apres
