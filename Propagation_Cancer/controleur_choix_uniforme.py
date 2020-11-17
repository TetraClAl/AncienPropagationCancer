import random as rd 

from data_main import * 

def choix_uniforme_site (univers, x, y) :  
    """ choix uniforme site voisin au site en paramètre qui va devenir tumorale si il est libre
    x,y : coordonnée du site avec une cellule tumorale """
    voisins = get_adj(x, y ,univers)
    indice = rd.randint (0, len(voisins) - 1)  # on choisit un voisin de manière aléatoire 
    a,b  = voisins[indice] 

    if get_cell(a, b , univers ) == 0 : 
        set_cell(a, b , 1, univers)
        set_cell(x ,y, 0, univers)

def choix_uniforme (univers) : 
    """ applique la fonction choix_uniforme_site a tous les sites avec une cellule tumorale """
    for i in range (len(univers)) : 
        for j in range (len(univers[0])) : #on parcourt tout l'univers
            if get_cell (i,j, univers) == 1 : #si site est occupé par cellule tumorale elle peut migrer
                choix_uniforme_site (univers, i ,j)

