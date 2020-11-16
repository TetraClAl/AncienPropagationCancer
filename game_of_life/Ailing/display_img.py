import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from gol_simulation import *

# """ test = np.zeros((6, 6), dtype=np.uint8)
# img = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
# print(test)
# plt.imshow(img, cmap='gray')
# plt.show() """


def display_img(universe):  # universe :tableau np ou liste de liste. 2D
    # figure de base
    img = plt.figure()

    # config des axes : graduations de 1 en 1, correspondent aux cellules
    ax = img.gca()
    ax.set_xticks(np.arange(-0.5, len(universe), 1))
    ax.set_yticks(np.arange(-0.5, len(universe[0]), 1))

    # cacher les graduations
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

    # afficher une grille (a partir des graduations données)
    plt.grid()

    # afficher le tableau en tant qu'image
    plt.imshow(universe, cmap='binary')
    plt.show()


# universe = generate_universe_np((4, 4))
# seed = create_seed('r_pentomino')
# universe = add_seed_to_universe(seed, universe)


# univ = generate_universe_np((20, 20))
# graine = create_seed("block_switch_engine")


# ajouter_pattern(univ, graine, 3, 7)
# display_img(univ)
