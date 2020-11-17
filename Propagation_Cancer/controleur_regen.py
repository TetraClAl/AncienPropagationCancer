from data_main import *


def regen_centre(env, dx, dy, tx, ty):
    """ Fait en sorte que le centre ne se vide pas """
    # Pour simplifier, on prend des centres rectangulaires
    for i in range(tx):
        for j in range(ty):
            if get_cell(dx + i, dy + j, env[0]) != 1:
                set_cell(dx + i, dy + j, 1, env)
    
