from data_main import *
from controleur_utilitaires import *


def regen_centre(env, centre):
    """ Fait en sorte que le centre ne se vide pas """
    dx = centre[0]  # coordonnée en x du coin en haut à gauche du centre
    dy = centre[1]  # coordonnée en y du coin en haut à gauche du centre
    tx = centre[2]  # longueur selon x du centre
    ty = centre[3]  # longueur selon y du centre

    # Pour simplifier, on prend des centres rectangulaires
    for i in range(tx):
        for j in range(ty):
            if get_cell(dx + i, dy + j, env[0]) != 1:
                set_cell(dx + i, dy + j, 1, env)


def liste_centre_(centre):
    "Liste des coordonnées des cellules du centre"
    dx = centre[0]  # coordonnée en x du coin en haut à gauche du centre
    dy = centre[1]  # coordonnée en y du coin en haut à gauche du centre
    tx = centre[2]  # longueur selon x du centre
    ty = centre[3]  # longueur selon y du centre

    res = []
    for i in range(tx):
        for j in range(ty):
            res.append([dx + i, dy + j])

    return res
