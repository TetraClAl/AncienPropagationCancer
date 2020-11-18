import random as rd 

from data_main import * 
from controleur_choix_uniforme import * 

def get_adj_astrocyte(x, y, env) : 
    """ renvoie la liste des sites adjacents occupés par un astrocyte"""
    astro = []
    univers = env[0]
    voisins = get_adj(x, y, univers)
    for site in voisins : # on parcourt tous les voisins
        x,y = site 
        if get_cell(x, y, univers) == 2 : #si ce sont des astrocytes, on les rajoute à la liste 
            astro.append (site)
    return astro



def get_adj_vide (x, y, env ) : 
    """ renvoie la liste des sites adjacents vides"""
    vide = []
    univers = env[0]
    voisins = get_adj(x, y, univers)
    for site in voisins : # on parcout tous les voisins
        x,y = site 
        if get_cell(x, y, univers) == 0 : #si ils sont vides on les rajoute à la liste
            vide.append (site)
    return vide 


def jonction_heterotype_site (env,x ,y, q): 
    """ q est la probabilité de choisir un site occupé par un astrocyte """
    u = rd.random()

    if u < q : #la cellule va migrer vers un astrocyte si il y en a un 
        astro = get_adj_astrocyte (x, y, env)
        if astro != [] : 
            indice = rd.randint (0, len(astro) - 1)
            a, b = astro[indice]

            set_cell(a, b , 1, env)
            set_cell(x ,y, 0, env)

    else : #elle migre vers un site vide si il y en a un 
        vide = get_adj_vide (x, y, env)
        if vide != [] : 
            indice = rd. randint (0, len(vide) - 1)
            a, b = vide[indice]

            set_cell(a, b , 1, env)
            set_cell(x ,y, 0, env)


def jonction_heterotype (env, centre,p,q ) : 
    """ applique la fonction jonciton_heterotype_site a tous les sites avec une cellule tumorale """

    vides, tumorales, astrocytes = tri_cells(env[0]) #trie les sites selon leur type
    centres = coord_centre(centre) #permet d'obtenir tous les sites qui sont dans le centre

    for site in tumorales : # a toutes les cellules tumorales, on applique une jonction heterotype
        i,j = site 
        jonction_heterotype (env, i ,j, q)

        if site in centres : # on regènere le centre si besoin 
            set_cell(i,j,1,env)
