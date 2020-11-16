from generate_universe import * 
from seed import * 
import numpy as np

def test_create_seed():
    seed=create_seed(type_seed = "r_pentomino")
    assert seed==[[0, 1, 1], [1, 1, 0], [0, 1, 0]]

def test_add_seed_to_universe():
    seed = create_seed(type_seed = "r_pentomino")
    universe = generate_universe(size=(6,6))
    universe = add_seed_to_universe(seed, universe, 1, 1)
    test_equality=np.array(universe ==np.array([[0,0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 1, 1, 0, 0, 0],
 [0 ,0, 1, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality.all()


test_create_seed()
print("premier test est un succés")
test_add_seed_to_universe()
print("second test est un succés")
