from data_import import *
from data_base import *
from data_fusion import *

# Note to self (TODO) : utiliser des listes de coordonnées triées selon l'ordre alphabétique pourrait permettre d'accélérer les fusions de listes en éléminant les doublons.
# Les propriétés de ces éléments (coordonnées ne se répétant pas) pourraient permettre d'obtenir un algo très rapide.

use_fusion = True


def set_fusion(data):
    global use_fusion
    use_fusion = data


def get_fusion():
    global use_fusion
    return use_fusion


# ----- Ce code pourrait nécessiter du refactoring


hex_directions = [
    [[+1,  0], [0, -1], [-1, -1],
     [-1,  0], [-1, +1], [0, +1]],
    [[+1,  0], [+1, -1], [0, -1],
     [-1,  0], [0, +1], [+1, +1]], ]


def voisin_dir(hex, direction):
    """ Retourne les coordonnées de l'hex situé dans la direction associée. """
    # Calcul de parité
    if hex[1] % 2 == 1:
        parity = 1
    else:
        parity = 0

    # Récupération de la direction à effectuer
    direction_calc = hex_directions[parity][direction]

    # Calcul des nouvelles coordonnées ajoutant nos coordonnées d'origine comme offset
    # Mauvaise inversion ? TODO : Vérifier que les coordonnées ne sont pas inversées (update : normalement c'est bon, les tests sont corrects)
    return hex[0] + direction_calc[0], hex[1] + direction_calc[1]


def s_get_adj(x, y, univers):
    """ Retourne la liste des coordonnées des cellules adjacentes à (x, y). """
    Lc = []
    for direction in range(6):
        x1, y2 = voisin_dir([x, y], direction)
        Lc += [[x1, y2]]

    # Cas fusion
    if use_fusion:
        return tri_liste(s_check_list(Lc, univers))

    # Retour par défaut
    return s_check_list(Lc, univers)

# ----- Fin de la section cible refactoring


def s_get_groupe_adj(x, y, env):
    """ Retourne l'index du groupe de la cellule (x, y). """
    for i in range(len(env[1])):
        e = env[1][i]
        for comp in e[0]:
            if comp[0] == x and comp[1] == y:
                return i
        for comp in e[1]:
            if comp[0] == x and comp[1] == y:
                return i
    return None


def s_get_groupe(x, y, env):
    """ Retourne l'index du groupe de la cellule (x, y). """
    folder = env[1]
    for i in range(len(env[1])):
        e = folder[i]
        for comp in e[0]:
            if comp[0] == x and comp[1] == y:
                return i
    return None


def s_union_liste(l1, l2):
    """ Fait une union de deux listes de cellules. """
    # Cas fusion
    if use_fusion:
        print("fusion")
        return union_tri(l1, l2)
    else:
        print("legacy")

    # Initialisation
    Lf = []
    Lf += l1

    # Ajout de tous les éléments de l2 qui ne sont déjà pas dans l1
    for e in l2:
        # Initialisation variable locale
        pres = False

        # On parcoure l1 pour savoir si l'élément est dedans
        for i in l1:
            if i[0] == e[0] and i[1] == e[1]:
                pres = True

        # Si la réponse est non, on ajoute l'élément à Lf
        if pres == False:
            Lf += [e]

    # Retour
    return Lf


def s_prive_liste(l1, l2):
    """ Retourne la liste l1 privée de l2. Tri aussi l1 """
    # Cas fusion
    if use_fusion:
        l1 = prive_tri(l1, l2)
        # print(l1)
        return l1

    # Initialisation boucle while
    i = 0

    # Boucle
    while i < len(l1):
        # Fetch
        value = l1[i]
        delete = False

        # Vérification présence
        for e in l2:
            if value[0] == e[0] and value[1] == e[1]:
                delete = True

        # Suppression si besoin
        if delete:
            del l1[i]
        else:
            i += 1  # En cas de suppression, pas besoin d'incrémenter

    # Retour
    return l1


def s_fusion_groupe(index_groupe1, index_groupe2, env):
    """ Fait fusionner deux groupes. """
    # Récupération de variables intermédiaires
    #univers = env[0]
    folder = env[1]

    # Récupération des groupes
    groupe1 = folder[index_groupe1]
    groupe2 = folder[index_groupe2]

    # Fusions des composants/adjacents
    groupe1[0] = s_union_liste(groupe1[0], groupe2[0])
    groupe1[1] = s_union_liste(groupe1[1], groupe2[1])

    # print("----")
    #print("Composants : ", groupe1[0])
    #print("Adjacents : ", groupe1[1])

    # Suppressions des adjacentes superposées
    groupe1[1] = s_prive_liste(groupe1[1], groupe1[0])
    #print("Maj Adjacents : ", groupe1[1])

    # Suppression du groupe 2
    del folder[index_groupe2]


def s_creer_groupe(cellules, env):
    # Fetch
    folder = env[1]
    univers = env[0]
    if use_fusion:
        cellules = tri_liste(cellules)
    groupe = [cellules, []]
    adj = groupe[1]

    # Ajout des cellules adjacentes
    for e in groupe[0]:
        adj = s_union_liste(adj, s_get_adj(e[0], e[1], univers))
        s_prive_liste(adj, cellules)

    # Màj adj
    groupe[1] = adj

    # Ajout à l'env
    folder.append(groupe)

    # Fusion avec nouveaux groupes adjacents
    for e in cellules:
        i = s_get_groupe_adj(e[0], e[1], env)  # Ok _adj
        if i != None and i != len(folder) - 1:
            #print("Fusion avec ", i)
            s_fusion_groupe(len(folder) - 1, i, env)

    # Renvoie l'index du groupe
    return len(folder) - 1


def s_check_cell_groupe(x, y, env):
    i = s_get_groupe(x, y, env)  # Non _adj
    if i == None:
        return s_creer_groupe([[x, y]], env)
    return i


def s_cell_delete(x, y, env):
    """ Met à jour le groupe après la suppression d'une cellule. """
    # Fetch
    folder = env[1]
    index_groupe = s_get_groupe(x, y, env)  # Non _adj

    # print(env)

    # Cas sans groupe
    if index_groupe == None:
        return

    # Récupération cellules
    cells = folder[index_groupe][0]
    cells = s_prive_liste(cells, [[x, y]])

    # Suppression groupe
    del folder[index_groupe]

    # On recrée les groupes
    for e in cells:
        s_check_cell_groupe(e[0], e[1], env)
