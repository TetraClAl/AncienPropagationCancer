from vue_animation import *


# Figures pour les démos:
# pour une règle donnée, 4 figures pour 4 itérations successives
# et une animation (seconde fenetre)

# Modifier les paramètres suivants
p = 1
q = 1
pocc = 0.5
taille = 25

# Séparation en 4 sous-figures
fig = plt.figure()
plt.suptitle(
    "Couplage des jonctions \n p=1, q=1: les cellules restent en groupent et mangent les astrocytes")

ax1 = fig.add_subplot(2, 2, 1)
plt.axis([-1, 2*taille + 0.5, -1, sqrt(3) * taille])

ax2 = fig.add_subplot(2, 2, 2)
plt.axis([-1, 2*taille + 0.5, -1, sqrt(3) * taille])

ax3 = fig.add_subplot(2, 2, 3)
plt.axis([-1, 2*taille + 0.5, -1, sqrt(3) * taille])

ax4 = fig.add_subplot(2, 2, 4)
plt.axis([-1, 2*taille + 0.5, -1, sqrt(3) * taille])


# création du centre et de l'environnement sans astrocytes
centre = [2, 2, 3, 4]
env = init_univers(taille, taille, centre, Pocc=pocc)

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
    animation(env, centre, 35, regle, p, q, interv=500)


anim_regle(regle)
plt.show()
