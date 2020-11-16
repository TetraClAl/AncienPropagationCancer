import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(1, figsize=(10, 10))  # crée le graphe

# limites
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# quadrillage
plt.grid(which='major', linestyle='-', linewidth=1, color='k')
plt.minorticks_on()
plt.grid(which='minor', linestyle='--')  # tiret

# ajouter un rectangle
ax.add_artist(patches.Rectangle((1, 1), 1, 1, color='green'))


# ax.add_patch(
#     patches.Rectangle(
#         (1, 1),
#         0.5,
#         0.5,
#         edgecolor='red',
#         facecolor='red',
#         fill=True
#     ))
# ax.add_artist(patches.Rectangle(
#     (0.2, 0.2), 0.4, 0.3, color='magenta'))
plt.show()
