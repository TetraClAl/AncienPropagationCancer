from pytest import *


from animation_a import *

init = init_universe((6, 6), 'beacon', 1, 1)

animation = game_life_simulation(init, 3)


def test_anim():
    print('L animation correspond à l attente')
    assert False
