from pytest import *
from performances import *


# Fonction de test de test_measure, si ton ordi n'arrive pas à faire quelques carrés en moins de 10s F
# Ce test permet surtout de s'assurer qu'il n'y a pas d'erreur de syntaxe/boucle infinie
def test_measure():
    t = measure(lambda x: x**2, [1, 2, 3], 100)
    assert t[0] < 10
    assert t[1] < 10
    assert t[2] < 10
