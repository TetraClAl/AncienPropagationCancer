from vue_patch import *
from vue_univers import *
from controleur_initialisation import *
from controleur_choix_uniforme import *
import copy as c
from matplotlib.animation import FuncAnimation


def omega(env, n, regle=choix_uniforme):
    """Renvoie la liste des états de l'univers pour n itérations. La regle est sous forme d'une fonction s'appliquant à un environnement"""

    omega = []
    environ = env

    for i in range(n):
        # copie indépendante!
        univ = c.deepcopy(environ[0])
        # qui est ajoutée à omega
        omega += [univ]

        # regle modifie directement environ. Comment ne pas modifier env lorsque l'on modifie environ?
        regle(environ)

    return omega


def create_plane(n, m, ax):
    """crée un pavage de sites vides sur ax, de taille n*m et renvoie le tableau des patches correspondants"""
    plane = []

    for x in range(n):
        line = []
        for y in range(m):
            # site vide
            patch = create_patch(x, y, 0)
            # ajouté à la figure
            ax.add_patch(patch)
            # ajouté au tableau
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


def animation_update(i, omega, plane):
    """ renvoie la liste des patch pour l'état i """
    refresh_plane(plane, omega[i])
    return redim(plane)


def animation(env, n, regle=choix_uniforme, show=True, fig=None, interv=300):
    """Animation de n générations en partant initialement de env. regle est une fonction qui modifie un env. Par défaut, l'affichage est activé avec show."""

    omeg = omega(env, n, regle)
    a, b = np.shape(omeg[0])

    # création de la figure avec des axes adaptés à la taille de l'univers
    if fig == None:
        fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    plt.axis([-1, 2*(a+1), -1, sqrt(3)*b + 0.5])

    # création du plan vide
    plane = create_plane(a, b, ax)

    # Fonctions d'animation, update:  int -> liste de patches
    def f_update(i): return animation_update(i, omeg, plane)
    def f_init(): return animation_update(0, omeg, plane)

    # Animation. blit: ne change que les elements modifiés d'une frame à l'autre
    ani = FuncAnimation(fig, f_update, frames=(
        n), init_func=f_init, blit=True, interval=interv, repeat=True)

    if show:
        plt.show()
