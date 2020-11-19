from vue_animation import *


# Figures pour les démos:
# pour une règle donnée, 4 figures pour 4 itérations successives
# et une animation (seconde fenetre)

# Modifier les paramètres suivants
p = None
q = None
pocc = 0.5


# Séparation en 4 sous-figures
fig = plt.figure()
#plt.suptitle("dep_homotype_groupe_all \n p=1: attractif")

ax1 = fig.add_subplot(2, 2, 1)
plt.axis([-1, 10, -1, 10])

ax2 = fig.add_subplot(2, 2, 2)
plt.axis([-1, 10, -1, 10])

ax3 = fig.add_subplot(2, 2, 3)
plt.axis([-1, 10, -1, 10])

ax4 = fig.add_subplot(2, 2, 4)
plt.axis([-1, 10, -1, 10])


# création du centre et de l'environnement sans astrocytes
centre = [2, 2, 3, 1]
env = init_univers(15, 15, centre, Pocc=pocc)

# création des planes sur chaque figure
plane0 = create_plane(env, ax1)
plane1 = create_plane(env, ax2)
plane2 = create_plane(env, ax3)
plane3 = create_plane(env, ax4)


def regle(env, centre, p, q):
    return jonction_duo(env, centre, p, q)


def display_regle_4(regle):
    omeg = omega(env, centre, 4, regle=regle, p=p, q=q)

    # Univers initial
    refresh_plane(plane0, omeg[0], centre)

    # Premier tour
    refresh_plane(plane1, omeg[1], centre)

    # Deuxième tour
    refresh_plane(plane2, omeg[2], centre)

    # Troisième tour
    refresh_plane(plane3, omeg[3], centre)


display_regle_4(regle)


def anim_regle(regle):
    animation(env, centre, 20, regle, p, q)


anim_regle(regle)
plt.show()
