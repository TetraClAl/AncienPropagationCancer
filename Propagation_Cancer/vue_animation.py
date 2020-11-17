from vue_patch import * 
from vue_univers import * 
from controleur_initialisation import *
from controleur_choix_uniforme import * 

def omega(env, n, regle= choix_uniforme):
    "Renvoie la liste des états de l'univers pour n itérations. La regle est sous forme d'une fonction s'appliquant à un environnement 
    omega =[]
    environ= env 
    for i in range(n):
        omega+=[environ[0]]
        environ= regle(environ)
