from controleur_initialisation import *

def test_ajout_astrocytes():
    univers = create_univers(5,5)
    res = 0
    univers = ajout_astrocytes(univers, 0.2)
    for i in range(5):
        for j in range(5):
            if univers[i,j] == 2:
                res+=1
    assert res == 5

def test_init_univers():
    univers = init_univers(4, 4, (1,1,2,2))
    assert np.shape(univers) == (4,4)
    res = 0
    for i in range(4):
        for j in range(4):
            if get_cell(i, j, univers) == 1:
                res+=1
    assert res == 4


test_ajout_astrocytes()
print("test 1 ok")
test_init_univers()
print("test 2 ok")