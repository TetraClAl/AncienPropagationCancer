from data_import import *
from data_base import *

# Note to self (TODO) : utiliser des listes de coordonnées triées selon l'ordre alphabétique pourrait permettre d'accélérer les fusions de listes en éléminant les doublons.
# Les propriétés de ces éléments (coordonnées ne se répétant pas) pourraient permettre d'obtenir un algo très rapide.

# ----- Ce code pourrait nécessiter du refactoring

hex_directions = [
    [[+1,  0], [0, -1], [-1, -1],
     [-1,  0], [-1, +1], [0, +1]],
    [[+1,  0], [+1, -1], [0, -1],
     [-1,  0], [0, +1], [+1, +1]],
]


def voisin_dir(hex, direction):
    """ Retourne les coordonnées de l'hex situé dans la direction associée. """
    # Calcul de parité
    if hex[0] % 2 == 1:
        parity = 1
    else:
        parity = 0

    # Récupération de la direction à effectuer
    direction_calc = hex_directions[parity][direction]

    # Calcul des nouvelles coordonnées ajoutant nos coordonnées d'origine comme offset
    # Mauvaise inversion ? TODO : Vérifier que les coordonnées ne sont pas inversées (update : normalement c'est bon, les tests sont corrects)
    return hex[1] + direction_calc[0], hex[0] + direction_calc[1]


def s_get_adj(x, y, univers):
    """ Retourne la liste des coordonnées des cellules adjacentes à (x, y). """
    Lc = []
    for direction in range(6):
        x1, y2 = voisin_dir([x, y], direction)
        Lc += [[x1, y2]]
    return s_check_list(Lc, univers)

# ----- Fin de la section cible refactoring


def s_get_groupe(x, y, env):
    """ Retourne l'index du groupe de la cellule (x, y). """
    for i in range(len(env[1])):
        e = env[1][i]
        in_groupe = False
        for comp in e[0]:
            if comp[0] == x and comp[0] == y:
                return i
        for comp in e[1]:
            if comp[0] == x and comp[0] == y:
                return i
    return None


def s_union_liste(l1, l2):
    """ Fait une union de deux listes de cellules. """
    Lf = []
    Lf.append(l1)

    for e in l2:
        pres = False
        for i in l1:
            if i[0] == e[0] and i[1] == e[1]:
                pres = True
        if pres == False:
            Ls += [e]

    return Lf


def s_prive_liste(l1, l2):
    """ Retourne la liste l1 privée de l2. """
    i = 0
    while i < len(l1):
        value = l1[i]
        delete = False
        for e in range(len(l2)):
            if value[0] == e[0] and value[1] == e[1]:
                delete = True
        if delete:
            l1.erase(i)
        else:
            i += 1


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

    # Suppressions des adjacentes superposées
    s_prive_liste(groupe1[1], groupe1[0])

    # Suppression du groupe 2
    folder.erase(index_groupe2)


def s_creer_groupe(cellules, env):
    # Fetch
    folder = env[1]
    univers = env[0]
    groupe = [[cellules], []]
    adj = groupe[1]

    # Ajout des cellules adjacentes
    for e in groupe[0]:
        adj = s_union_liste(adj, s_get_adj(e[0], e[1], univers))
        s_prive_liste(adj, cellules)

    # Ajout à l'env
    folder.append(groupe)

    # Fusion avec nouveaux groupes adjacents
    for e in cellules:
        i = s_get_groupe(e[0], e[1], env)
        if i != None:
            s_fusion_groupe(len(folder) - 1, i, env)

    # Renvoie l'index du groupe
    return len(folder) - 1
