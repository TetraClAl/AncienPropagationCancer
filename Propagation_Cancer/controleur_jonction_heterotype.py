import random as rd 

from data_main import * 

def get_adj_tri(x, y, env) : 
    """ renvoie la liste des sites adjacents occupés par un astrocyte"""
    return asto



def get_adj_vide (x, y, env) : 
    """ renvoie la liste des sites adjacents vides"""
    return vide 


def jonction_heterotype_site (env,x ,y, q): 
    """ q est la probabilité de choisir un site occupé par un astrocyte """
    u = rd.random()

    if u < q : #la cellule va migrer vers un astrocyte   
        astro = get_adj_astrocyte (x, y, env)
        indice = rd.randint (0, len(astro))
        a, b = astro[indice]

        set_cell(a, b , 1, env)
        set_cell(x ,y, 0, env)

    else : #elle migre vers un site vide 
        vide = get_adj_vide (x, y, env)
        indice = rd. randint (0, len(vide))
        a, b = vide[indice]

        set_cell(a, b , 1, env)
        set_cell(x ,y, 0, env)


def jonction_heterotype (env) : 
    """ applique la fonction jonciton_heterotype_site a tous les sites avec une cellule tumorale """
    for i in range (len(env[0])) : 
        for j in range (len(env[0][0])) : #on parcourt tout l'univers
            
            if get_cell (i,j, env[0]) == 1 : #si site est occupé par cellule tumorale elle peut migrer
                jonction_heterotype_site (env, i ,j)