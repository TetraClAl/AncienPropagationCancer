from vue_utilitaires import *


def create_patch(x, y, etat, centre=False):
    """Crée le patch correspondant à la cellule. Si elle appartient au centre, elle est mise en valeur."""
    xp, yp = plane_coord(x, y)
    # arguments: centre, nombre de sommet, distance centre-sommet, couleur du bord, couleur de l'interieur
    hexagone = patches.RegularPolygon(
        (xp, yp), 6, radius=2/sqrt(3), ec='grey', fc=couleur[etat])

    if centre:
        hexagone.set_alpha(1)
        # hexagone.set_hatch('/')

    return hexagone


def display_patch(x, y, etat, ax, centre=False):
    "Affiche le patch correspond sur le subplot ax"
    patch = create_patch(x, y, etat, centre)
    ax.add_patch(patch)
