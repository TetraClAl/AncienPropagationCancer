from vue_patch import *
from vue_univers import *
from controleur_initialisation import *
from controleur_choix_uniforme import *
import copy as c
from matplotlib.animation import FuncAnimation


def omega(env, n, regle=choix_uniforme):
    "Renvoie la liste des états de l'univers pour n itérations. La regle est sous forme d'une fonction s'appliquant à un environnement"

    omega = []
    environ = env

    for i in range(n):
        # copie indépendante
        univ = c.deepcopy(environ[0])
        # qui est ajoutée à omega
        omega += [univ]

        # regle modifie directement environ
        regle(environ)

    return omega


def init_plane_by_state(env):
    "Stocke les patches correspondant à un univers donné par ordre d'état "
    univ = env[0]
    v, t, a = tri_cells(univ)

    plane = []

    # vides
    for (x, y) in v:
        patch = create_patch(x, y, 0)
        ax.add_patch(patch)
        ligne = [patch]
        plane += [ligne]

    # astrocytes
    for (x, y) in a:
        patch = create_patch(x, y, 2)
        ax.add_patch(patch)
        ligne = [patch]
        plane += [ligne]

    # tumorales
    for (x, y) in a:
        patch = create_patch(x, y, 1)
        ax.add_patch(patch)
        ligne = [patch]
        plane += [ligne]

    return plane


def create_plane(n, m, ax):
    plane = []

    for x in range(n):
        line = []
        for y in range(m):
            patch = create_patch(x, y, 0)
            ax.add_patch(patch)
            line += [patch]

        plane += [line]

    return plane


def init_plane(univ, ax):
    "Création de l'image initiale et renvoie le tableau des patches, utilisé par les fonctions d'animation"
    n, m = np.shape(univ)

    plane = []

    for x in range(n):
        line = []
        for y in range(m):
            etat = get_cell(x, y, univ)
            patch = create_patch(x, y, etat)
            ax.add_patch(patch)
            line += [patch]

        plane += [line]

    return plane


def refresh_plane(plane, univers):
    "Ajuste la couleur des patches en fonction des nouveaux états de l'univers"
    n, m = np.shape(univers)

    for x in range(n):
        for y in range(m):
            etat = get_cell(x, y, univers)
            patch = plane[x][y]
            coul = patch.get_facecolor()
            if coul != couleur[etat]:
                patch.set_facecolor(couleur[etat])


def redim(plane):
    """ Transforme un tableau 2D en tableau 1D. """
    # Cette fonction sert à transformer le tableau 2D de cellules à afficher en un tableau 1D pour la fonction d'animation.
    liste = []
    for e in plane:
        liste += e
    return liste


def animation_init(omega, ax):
    plane = init_plane(omega[0], ax)
    return redim(plane)


def animation_update(i, omega, plane):
    refresh_plane(plane, omega[i])
    return redim(plane)


def animation(env, n, regle=choix_uniforme):
    fig, ax = plt.subplots(1)
    plt.axis([-1, 10, -1, 10])

    omeg = omega(env, n, regle)
    n, m = np.shape(omeg[0])
    plane = create_plane(n, m, ax)

    print(omeg)
    # Fonctions d'animation, update:  int -> liste de patches
    def f_update(i): return animation_update(i, omeg, plane)
    def f_init(): return animation_update(0, omeg, plane)

    # Animation
    ani = FuncAnimation(fig, f_update, frames=(
        n + 1), init_func=f_init, blit=True, interval=600, repeat=True)

    plt.show()
