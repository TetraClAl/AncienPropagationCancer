from vue_utilitaires import *
from vue_univers import *


from matplotlib.animation import FuncAnimation


def omega(env, centre, n, regle=choix_uniforme, p=None, q=None):
    """Renvoie la liste des états de l'univers pour n itérations. La regle est sous forme d'une fonction s'appliquant à un environnement"""

    omega = []
    environ = env

    for i in range(n):
        # copie indépendante!
        univ = c.deepcopy(environ[0])
        # qui est ajoutée à omega
        omega += [univ]

        # regle modifie directement environ.
        regle(environ, centre, p, q)

    return omega


def create_plane(env, ax):
    """crée un pavage de sites vides sur ax, avec le centre mis en valeur, et renvoie le tableau des patches correspondants"""

    n, m = np.shape(env[0])
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


def refresh_plane(plane, univers, centre):
    "Ajuste la couleur des patches en fonction des nouveaux états de l'univers"
    n, m = np.shape(univers)

    for x in range(n):
        for y in range(m):
            etat = get_color(x, y, univers, centre)
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


def animation_update(i, omega, plane, centre):
    """ renvoie la liste des patch pour l'état i """
    refresh_plane(plane, omega[i], centre)
    return redim(plane)


def animation(env, centre, n, regle=choix_uniforme, p=None, q=None, show=True, fig=None, interv=1000):
    """Animation de n générations en partant initialement de env. regle est une fonction qui modifie un env. Par défaut, l'affichage est activé avec show."""

    omeg = omega(env, centre, n, regle, p, q)
    a, b = np.shape(omeg[0])

    # création de la figure avec des axes adaptés à la taille de l'univers
    if fig == None:
        fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    plt.axis([-1, 2*a+0.5, -1, sqrt(3)*b + 0.5])

    # création du plan vide
    plane = create_plane(env, ax)

    # Fonctions d'animation, update:  int -> liste de patches
    def f_update(i): return animation_update(i, omeg, plane, centre)
    def f_init(): return animation_update(0, omeg, plane, centre)

    # Animation. blit: ne change que les elements modifiés d'une frame à l'autre
    ani = FuncAnimation(fig, f_update, n, init_func=f_init,
                        blit=False, interval=interv, repeat=False)

    if show:
        plt.show()

    return ani
