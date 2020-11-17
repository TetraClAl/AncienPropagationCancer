from controleur_initialisation import *

def test_ajout_astrocytes():
    univers = create_univers(5,5)
    env = create_env(univers)
    res = 0
    env = ajout_astrocytes(env, 0.2)

    for i in range(5):
        for j in range(5):
            if univers[i,j] == 2:
                res+=1
    assert res == 5

def test_init_univers():
    env = init_univers(4, 4, (1,1,2,2))
    univers = env[0]

    assert np.shape(univers) == (4,4)
    res = 0
    for i in range(4):
        for j in range(4):
            if get_cell(i, j, env[0]) == 1:
                res+=1
    assert res == 4

