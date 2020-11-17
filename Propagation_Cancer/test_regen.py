from controleur_regen import *

def test_regen_centre():
    univers = create_univers(5,5)
    regen_centre(univers, 2, 2, 2, 3)
    print(univers)
    A = np. array([[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1],
                   [0, 0, 1, 1, 1],
                   [0, 0, 0, 0, 0]])

    assert np.array_equal(univers, A)

test_regen_centre()
print("test regen ok")