from controleur_jonction_heterotype import * 
from pytest import * 

import numpy as np 

def test_jonction_heterotype_site () :

    #cas où un seul astrocyte avec proba d'aller dans un astrocyte de 1
    univers = np.array ([[0, 1, 2], [1, 1, 1], [0, 1, 0]])
    env = create_env(univers)
    jonction_heterotype_site(env, 1, 2, 1)
    A = np.array([[0, 1, 1], [1, 1, 0], [0, 1, 0]])
    assert np.array_equal(env[0], A)
    print ('premier test avec astrocyte ok ')

    #cas où un seul site vide avec proba d'aller dans un site vide de 1 (donc q = 0)
    univers = np.array ([[1, 1, 1], [1, 1, 1], [1, 1, 0]])
    env = create_env(univers)
    jonction_heterotype_site(env, 1, 1, 0)
    A = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    assert np.array_equal(env[0], A)
    print ('premier test avec site vide ok')

def test_jonction_heterotype () : 
    # cas ou il vont uniquement dans les astrocytes 

    # cas ou il vont uniquement dans les sites vides 