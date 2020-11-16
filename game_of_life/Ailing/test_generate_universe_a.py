from generate_universe_a import *
from pytest import *

universe = generate_universe_np((4, 4))
seed = create_seed('r_pentomino')


def test_generate_universe():
    test = np.array(universe == [[0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    assert test.all()


def test_create_seed():
    test = np.array(seed == np.array(
        [[0, 1, 1], [1, 1, 0], [0, 1, 0]]))
    assert test.all()


def test_add_seed_to_universe():
    test1 = np.array(add_seed_to_universe(seed, universe) == np.array(
        [[0, 1, 1, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]))
    assert test1.all()
