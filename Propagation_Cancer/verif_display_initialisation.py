from vue_univers import *
from controleur_initialisation import *

x = 3
y = 0
centre = [x, y, 2, 2]

univers = init_univers(6, 6, centre)

display_univers(univers)
display_center(x, y)
plt.show()
