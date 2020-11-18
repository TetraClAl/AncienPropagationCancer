import random as rd 

from data_main import * 

# regle(env,centre, p = None, q = None)

def coord_centre(centre) : 
    """permet d'obtenir les coordonnées de tous les sites occupant le centre 
    centre est un quadruplant donnant les coordonées du centre du centre, la largeur selon x puis y"""
    centres = []
    x,y,l, L = centre
    for i in range (l) : 
        for j in range (L) : 
            centres.append ((x+i, y+j))
    return centres


def choix_uniforme_site (env, x, y) :  
    """ choix uniforme site voisin au site en paramètre qui va devenir tumorale si il est libre
    x,y : coordonnée du site avec une cellule tumorale """
    voisins = get_adj(x, y , env[0])
    indice = rd.randint (0, len(voisins)- 1)  # on choisit un voisin de manière aléatoire 
    a,b  = voisins[indice] 

    if get_cell(a, b , env[0]) == 0 : 
        set_cell(a, b , 1, env)
        set_cell(x ,y, 0, env)

def choix_uniforme (env, centre, p=None, q=None) : 
    """ applique la fonction choix_uniforme_site a tous les sites avec une cellule tumorale """

    vides, tumorales, astrocytes = tri_cells(env[0]) #trie les sites selon leur type
    centres = coord_centre(centre) #permet d'obtenir tous les sites qui sont dans le centre

    for site in tumorales : # a toutes les cellules tumorales, on applique un choix uniforme 
        i,j = site 
        choix_uniforme_site (env, i ,j)

        if site in centres : # on regènere le centre si besoin 
            set_cell(i,j,1,env)

