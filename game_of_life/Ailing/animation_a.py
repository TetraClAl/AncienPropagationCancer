from display_img import *

import matplotlib.animation as anim
import copy as c

# init univers initial
# n itérations


#init = init_universe((30, 30), 'infinite', 10, 10)


def game_life_anime(init, n, interv=300, color='binary', save=False):
    # initier figure
    fig = plt.figure()

    # liste des états
    animation = game_life_simulation(init, n)
    # liste des images
    ims = []

    # attention, il y a un petit soucis de dim dans animation
    for universe in animation:
        image = plt.imshow(universe, cmap=color, animated=True)
        ims.append([image])

    anime = anim.ArtistAnimation(fig, ims, interval=interv, blit=True,
                                 repeat_delay=0)
    # blit = True: only re-draw the pieces of the plot which have changed
    plt.show()


def game_anim_param(size, type_seed, xstart, ystart, cmap='binary', n_generations=30, interval=300):
    init = init_universe(size, type_seed, xstart, ystart)
    animation = game_life_anime(init, n_generations, interval, cmap, save)
    return animation
