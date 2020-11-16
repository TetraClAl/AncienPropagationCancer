from math import *
from matplotlib import *
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from data_main import *
from vue_cell import *


def display_univers(univers):
    n, m = np.shape(univers)
    for x in range(n):
        for y in range(m):
            display_cell(x, y, univers)


# univers = np.array([[1, 1, 2, 1, 1], [1, 0, 1, 0, 1], [2, 1, 2, 1, 2]])
# display_univers(univers)
# plt.show()
