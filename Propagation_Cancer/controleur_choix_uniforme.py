from controleur_utilitaires import *

from data_main import *

# regle(env,centre, p = None, q = None)


def choix_uniforme_site(env, x, y):
    """ choix uniforme site voisin au site en paramètre qui va devenir tumorale si il est libre
    x,y : coordonnée du site avec une cellule tumorale """
    voisins = get_adj(x, y, env[0])
    # on choisit un voisin de manière aléatoire
    indice = rd.randint(0, len(voisins) - 1)
    a, b = voisins[indice]

    if get_cell(a, b, env[0]) == 0:
        set_cell(a, b, 1, env)
        set_cell(x, y, 0, env)


def choix_uniforme(env, centre, p=None, q=None):
    """ applique la fonction choix_uniforme_site a tous les sites avec une cellule tumorale """

    vides, tumorales, astrocytes = tri_cells(
        env[0])  # trie les sites selon leur type
    # permet d'obtenir tous les sites qui sont dans le centre
    centres = liste_centre(centre)

    for site in tumorales:  # a toutes les cellules tumorales, on applique un choix uniforme
        i, j = site
        choix_uniforme_site(env, i, j)

        if site in centres:  # on regènere le centre si besoin
            set_cell(i, j, 1, env)
