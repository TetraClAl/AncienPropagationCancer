from pytest import *

from gol_simulation import *
from test_survival_a import *


def test_game_life_simulation():
    test = np.array(game_life_simulation_end(universe, 3) == survival2)
    assert test.all()
