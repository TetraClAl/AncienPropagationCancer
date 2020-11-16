from utilitaires_univers import *
from init_univers import *

# https://gitlab-cw5.centralesupelec.fr/victor.lebrun/jeudelavie_groupe5/-/wikis/survival.py


def evaluer_voisines(univers, x, y):
    """ Compte le nombre de cellules vivantes adjacentes à la cellule (x, y). """
    # On initialise le comptage
    s = 0

    # Colonne de gauche
    s += get_univers(univers, x + 1, y + 1)
    s += get_univers(univers, x, y + 1)
    s += get_univers(univers, x - 1, y + 1)

    # Colonne du milieu
    s += get_univers(univers, x + 1, y)
    s += get_univers(univers, x - 1, y)

    # Colonne de droite
    s += get_univers(univers, x + 1, y - 1)
    s += get_univers(univers, x, y - 1)
    s += get_univers(univers, x - 1, y - 1)

    # Retour
    return s


def survival(univers, x, y):
    """ Evalue si une cellule survie. """
    # Evaluation de l'environnement
    s = evaluer_voisines(univers, x, y)
    v = get_univers(univers, x, y)

    # Si la cellule est vivante
    if v == 1:
        if s == 2 or s == 3:
            return 1  # Elle vie
        else:
            return 0  # Elle décède

    # Si la cellule est morte
    else:
        if s == 3:
            return 1  # Elle naît
        else:
            return 0  # Elle reste morte

    # Assert se déclenchant automatiquement si la fonction atteind ce point, ce qui n'est pas censé arriver
    assert False


def generation(univers):
    """ Effectue une itération de l'univers. """
    # Initialisation d'un univers vide retour
    retour = init_univers(len(univers), len(univers[0]))

    # Application de la fonction survival à l'ensemble des cellules, écriture des résultats dans retour
    for i in range(len(univers)):
        for j in range(len(univers[0])):
            set_univers(retour, i, j, survival(univers, i, j))

    # Fin de fonction et envoie de la valeur retour du nouvel état
    return retour


def game_life_simulation(univers, n=20):
    """ Renvoie l'univers après n itérations """

    # Initialisation
    N = 0

    # Boucle principale
    while N < n:
        # Stockage temporaire du nouvel état
        cache = generation(univers)

        # Copie du cache dans l'univers, actualisation de l'état
        for i in range(len(univers)):
            for j in range(len(univers[0])):
                univers[i][j] = cache[i][j]

        # Incrémentation du compteur
        N += 1

    # Retour
    return univers


def game_life_simulation_animated(univers, n=20):
    """ Renvoie la liste des n états de l'univers"""
    anim = [[]]

    # Copie de l'univers dans le premier frame de l'animation
    for i in range(len(univers)):
        # Ajout d'une ligne
        anim[0] += [[]]

        # Remplissage de la ligne
        for j in range(len(univers[0])):
            anim[0][i] += [univers[i][j]]

    # Initialisation
    N = 0

    # Boucle principale
    while N < n:
        # Stockage du nouvel état dans le frame suivant
        anim += [generation(anim[-1])]

        # Incrémentation du compteur
        N += 1

    # Retour
    return anim
