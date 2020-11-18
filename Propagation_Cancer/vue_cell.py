from vue_utilitaires import *

# fig = plt.figure(figsize=(6, 6))
# # # necessite l'appel à une sous figure
# ax = plt.subplot(1, 1, 1)
# plt.axis([-1, 10, -1, 10])


def create_cell(x, y, univers):
    """Crée le patch correspondant à la cellule, si le site occupé. Si le site est libre, elle retourne None"""
    value = get_cell(x, y, univers)
    xp, yp = plane_coord(x, y)
    if value == 0:
        return None
    elif value == 1:
        # rouge pour les tumorales
        hexagone = patches.RegularPolygon(
            (xp, yp), 6, radius=2/sqrt(3), ec='white', fc='red', alpha=0.5)
    else:
        hexagone = patches.RegularPolygon(
            (xp, yp), 6, radius=2/sqrt(3), ec='white', fc='gray', alpha=0.5)
    return hexagone


def display_cell(x, y, univers, ax):
    "Affiche le patch correspond à la cellule sur le subplot ax. Une cellule vide n'est pas représentée"
    cell = create_cell(x, y, univers)
    if cell != None:
        ax.add_patch(cell)
