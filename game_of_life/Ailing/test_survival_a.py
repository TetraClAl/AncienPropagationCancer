from pytest import *

from survival_a import *
from generate_universe_a import *


universe = generate_universe_np((5, 5))
seed = seeds['r_pentomino']
universe = add_seed_to_universe(seed, universe, xstart=1, ystart=1)


survival = generation(universe)
survival2 = generation(survival)
survival3 = generation(survival2)

print(universe)
print(survival)


def test_voisines():
    assert voisines(universe, 1, 1) == 3
    assert voisines(universe, 0, 1) == 1


def test_generation():
    assert get_univers(survival, 1, 1) == 1
    assert get_univers(survival, 3, 3) == 0
