from generate_universe_a import *
from survival_a import *
from seeds_a import *
from gol_simulation import *
from display_img import *
from animation_a import *

import argparse


def game_of_life_launch(size, type_seed, seed_position, cmap, n_generations=30, interval=300, save=False):
    """
:param  tuple (int, int) universe_size: dimensions of the universe
:param type_seed: (str) initial type of seed 
:param seed_position: (tuple (int, int)) coordinates where the top-left corner of the seed array should be pinned
:param cmap: (str) the matplotlib cmap that should be used
:param n_generations: (int) number of universe iterations, defaults to 30
:param interval: (int )time interval between updates (milliseconds), defaults to 300ms
:param save: (bool) whether the animation should be saved, defaults to False
"""
    # initialisation de l'univers
    x, y = seed_position
    init = init_universe(size, type_seed, x, y)

    # animation
    game_life_anime(init, n_generations, interv=interval,
                    color=cmap, save=save)


def main():
    # gestion des arguments
    parser = argparse.ArgumentParser()

    # Ajout des arguments
    parser.add_argument(
        "x", help="taille de l'univers en x", type=int)
    parser.add_argument(
        "y", help="taille de l'univers en y", type=int)

    parser.add_argument("type_seed", help="type de graine initial", type=str)

    parser.add_argument(
        "sx", help="position de la graine initialement en x", type=int)
    parser.add_argument(
        "sy", help="position de la graine initialement en y", type=int)

    parser.add_argument("cmap", type=str)

    parser.add_argument(
        "n_generations", help="nombre de générations", type=int)

    parser.add_argument("--interval", help="intervale en ms", type=int)

    # On parse les arguments
    args = parser.parse_args()

    # execution
    game_of_life_launch((args.x, args.y), args.type_seed, (args.sx, args.sy),
                        args.cmap, args.n_generations, args.interval)


if __name__ == "__main__":
    main()
