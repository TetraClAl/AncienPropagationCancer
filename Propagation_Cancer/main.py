from data_main import *
from vue_univers import *


univers = create_univers(5, 5)

env = [univers, []]

x1 = 1
y1 = 2
x2 = 2
y2 = 2
x3 = 2
y3 = 3

set_cell(x1, y1, 1, env)
set_cell(x2, y2, 1, env)
set_cell(x3, y3, 1, env)

set_cell(x2, y2, 0, env)

index = s_get_groupe(x1, y1, env)
adj = env[1][index][1]
for e in adj:
    univers[e[0], e[1]] = 2

index = s_get_groupe(x3, y3, env)
adj = env[1][index][1]
for e in adj:
    univers[e[0], e[1]] = 2

display_univers(univers)
plt.show()
