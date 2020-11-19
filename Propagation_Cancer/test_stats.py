from stats import *

def test_taux_occupation_tumeur():
    env = init_univers(5, 5, (1, 1, 3, 3))
    t = taux_occupation_tumeur(env[0])
    res = 9/25
    assert t == res

def test_taux_occupation_astrocytes():
    env = init_univers(4, 4, (0, 0, 0, 0))
    t = taux_occupation_astrocytes(env[0])
    assert t == 0.5

def test_distance():
    x1 = (0, 0)
    x2 = (0, 1)
    x3 = (1,1)
    assert distance(x1, x1) == 0
    assert distance(x1, x2) == 1
    assert distance(x1, x3) == np.sqrt(2)

def test_plus_grande_distance():
    env = init_univers(5, 5, (2, 2, 1, 1), 0, np.array([[1, 1]]), 0, 0)
    (dist, point) = plus_grande_distance(env, (2, 2, 1, 1))
    assert point == (0, 0)
    assert dist == np.sqrt(8)

    env2 = init_univers(5, 5, (2, 2, 1, 1))
    (dist2, point2) = plus_grande_distance(env2, (2, 2, 1, 1))
    assert point2 == (2, 2)
    assert dist2 == 0



if __name__ == "__main__":
    test_taux_occupation_tumeur()
    print("test taux tumeur ok")
    test_taux_occupation_astrocytes()
    print("test taux astro ok")
    test_distance()
    print("test distance ok")
    test_plus_grande_distance()
    print("test plus grande distance ok")
    print("all ok")

    