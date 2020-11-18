from vue_utilitaires import *


def create_patch(x, y, etat):
    """Crée le patch correspondant à la cellule"""
    xp, yp = plane_coord(x, y)
    # arguments: centre, nombre de sommet, distance centre-sommet, couleur du bord, couleur de l'interieur
    hexagone = patches.RegularPolygon(
        (xp, yp), 6, radius=2/sqrt(3), ec='grey', fc=couleur[etat])

    return hexagone


def display_patch(x, y, etat, ax):
    "Affiche le patch correspond sur le subplot ax"
    patch = create_patch(x, y, etat)
    ax.add_patch(patch)
