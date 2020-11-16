from generate_universe_a import *
from pytest import *


def test_generate_universe():
    assert generate_universe((4, 4)) == [[0, 0, 0, 0], [
        0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


test_generate_universe()
print('la grille est correctement générée')
