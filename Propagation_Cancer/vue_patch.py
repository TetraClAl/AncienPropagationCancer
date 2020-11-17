from vue_utilitaires import *


def create_patch(x, y, etat):
    """Crée le patch correspondant à la cellule"""
    xp, yp = plane_coord(x, y)
    # site vide
    if etat == 0:
        hexagone = patches.RegularPolygon(
            (xp, yp), 6, radius=2/sqrt(3), ec='grey', fc='white')

    # cellule tumorale
    elif etat == 1:
        hexagone = patches.RegularPolygon(
            (xp, yp), 6, radius=2/sqrt(3), ec='white', fc='red', alpha=0.5)

    # astrocyte sain
    else:
        hexagone = patches.RegularPolygon(
            (xp, yp), 6, radius=2/sqrt(3), ec='white', fc='gray', alpha=0.5)
    return hexagone


def display_patch(x, y, etat, ax):
    "Affiche le patch correspond sur le subplot ax"
    patch = create_patch(x, y, etat)
    ax.add_patch(patch)
