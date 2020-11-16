from controleur_initialisation import *

def test_ajout_astrocytes():
    univers = create_univers(5,5)
    res = 0
    univers = ajout_astrocytes(univers, 0.2)
    print(univers)
    for i in range(5):
        for j in range(5):
            if univers[i,j] == 2:
                res+=1
    assert res == 5


def test_init_univers():
    univers = init_univers(1,1)
    assert univers == np.array([[1]])





