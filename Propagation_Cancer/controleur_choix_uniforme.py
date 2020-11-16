import random as rd 

from data_main import * 

def choix_uniforme_site (univers, site) :  
    """ choix uniforme site voisin au site en paramètre qui va devenir tumorale si il est libre
    site: site avec une cellule tumorale """

    indice = rd.randint (0, 5)  # on choisit un voisin de manière aléatoire 
    site_tumorale = voisins(site)[indice] # seulement si la fonction disponible renvoie bien une liste

        if get_cellC(site_tumorale , univers ) == 0 : 
            set_cellC(site_tumorale, 1, univers)
            set_cellC(site, 0, univers)

def choix_uniforme (univers) : 
""" applique la fonction choix_uniforme_site a tous les sites avec une cellule tumorale """
    for i in range (len(univers)) : 
            for j in range (len(univers[0])) : #on parcourt tout l'univers
                if get_cellC ((i,j), univers) == 1 : #si site est occupé par cellule tumorale elle peut migrer
                    choix_uniforme_site (univers, site)