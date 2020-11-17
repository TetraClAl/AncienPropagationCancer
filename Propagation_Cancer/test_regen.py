from controleur_regen import *

def test_regen_centre():
    univers = create_univers(5,5)
    env = create_env(univers)
    regen_centre(env, 2, 2, 2, 3)
    
    A = np. array([[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1],
                   [0, 0, 1, 1, 1],
                   [0, 0, 0, 0, 0]])

    assert np.array_equal(univers, A)

if __name__ == "__main__":
    test_regen_centre()
    print("test regen ok")