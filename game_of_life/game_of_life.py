from survival import *
from seeds import *
from display import *
from init_univers import *
from animation import *

import argparse


def game_of_life_launch(universe_size, seed, seed_position, cmap, n_generations, interval=300, save=False):
    """
    :param tuple (int, int) universe_size: dimensions of the universe
    :param seed: (list of lists, np.ndarray) initial starting array
    :param seed_position: (tuple (int, int)) coordinates where the top-left corner of the seed array should be pinned
    :param cmap: (str) the matplotlib cmap that should be used
    :param n_generations: (int) number of universe iterations, defaults to 30
    :param interval: (int )time interval between updates (milliseconds), defaults to 300ms
    :param save: (bool) whether the animation should be saved, defaults to False
    """

    # Création de l'univers
    x, y = universe_size
    sx, sy = seed_position
    univers = init_univers(x, y, seed, sx, sy)

    # Simulation
    display_animated_universe(univers, n_generations, interval, cmap, save)


def main():
    """ Fonction main """
    # Gestion des arguments
    parser = argparse.ArgumentParser()

    # Ajout des arguments
    parser.add_argument(
        "taillex", help="taille de l'univers selon x", type=int)
    parser.add_argument(
        "tailley", help="taille de l'univers selon y", type=int)

    parser.add_argument("seed", help="nom de la seed")

    parser.add_argument("seedx", help="position de la seed selon x", type=int)
    parser.add_argument("seedy", help="position de la seed selon y", type=int)

    parser.add_argument("cmap", help="cmap pour matplotlib")

    parser.add_argument("ngen", help="nombre de générations", type=int)

    parser.add_argument("--save", help="sauvegarder sous forme de gif",
                        action="store_true")

    parser.add_argument("--interval", help="intervale en ms")

    # On parse les arguments
    args = parser.parse_args()

    # On exécute
    game_of_life_launch((args.taillex, args.tailley), seeds[args.seed],
                        (args.seedx, args.seedy), args.cmap, args.ngen, int(args.interval), args.save)


# Exécution fonction main()
if __name__ == "__main__":
    main()
