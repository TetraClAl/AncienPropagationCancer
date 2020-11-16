from game_of_life import *
from pytest import *
import os  # Pour l'exécution des commandes

# Test de game_of_life_launch()


def test_game_of_life_launch():
    game_of_life_launch((20, 20), [[1, 1, 1], [1, 1, 1]], (10, 10), 'r', 20)
    # Je vois mal quels tests on peut faire à part lancer la fonction et vérifier que python ne décède pas


# Test de la fonction main, fait appel à des commandes
def test_main():
    # On exécute et on vérifie si ça marche TODO : Essayer de faire un système qui s'adapte aux différentes configurations ou qui se coupe en cas de problèmes
    os.system("'D:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\python.exe' game_of_life/game_of_life.py 50 50 r_pentomino 10 10 'r' 200 --interval 500 --save")
    # Pytest ne semble pas être capable de suivre ce test, mais coverage ne semble pas non plus indiquer main() comme couverte, donc c'est bon.
    # Je laisse test_main() là si jamais on trouve un moyen de la faire marcher.
