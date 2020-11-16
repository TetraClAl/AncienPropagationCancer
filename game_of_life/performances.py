from timeit import timeit
from survival import *



def measure(func, values, number=100):
    """ Fonction de mesure des performances """ 
    m = []
    for i in values:
        m.append(timeit(lambda: func(i), number=number))
    return m


# Petit test de temps d'exécution
if __name__ == "__main__":
    univers = init_univers(100, 100, seeds["r_pentomino"], 50, 50)
    print(measure(game_life_simulation, [univers], 20))
