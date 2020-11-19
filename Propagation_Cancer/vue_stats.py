from stats import *
import matplotlib
import matplotlib.pyplot as plt 


def display_occ(env, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):

    X = np.array([i for i in range(iterations)])
    Y1 = [taux_occ_tumeur(env[0])]
    Y2 = [taux_occ_astro(env[0])]
    for i in range(iterations-1):
        function(env, centre, p, q)
        Y1.append(taux_occ_tumeur(env[0]))
        Y2.append(taux_occ_astro(env[0]))
    Y1 = np.array(Y1)
    Y2 = np.array(Y2)
    plt.bar(X, Y1, color = (0.0, 0.0, 0.0, 0.4), label = "Taux de cellules tumorales" )
    plt.bar(X, -Y2, color = (1.0,0.38823529411764707, 0.2784313725490196, 0.4), label = "Taux d'astrocytes")
    plt.legend()
    plt.title("Occupation de la couche en fonction du nombre d'itérations")

    for x,y in zip(X,Y1):
        plt.text(x, y+0.02, '%.02f' % y, ha='center', va= 'bottom')
    for x, y in zip(X,Y2):
        plt.text(x, -y-0.08, '%.02f' % y, ha='center', va= 'bottom')

    plt.ylim(-1, 1)
    plt.show()


def display_distance(env, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):

    X = np.array([i for i in range(iterations)])
    Y = [plus_grande_distance(env, centre)[0]]
    for i in range(iterations-1):
        function(env, centre, p, q)
        Y.append(plus_grande_distance(env, centre)[0])
    Y = np.array(Y)

    plt.bar(X, Y, color = 'darkblue', label = "Distance au centre" )
    plt.legend()
    plt.title("Cellule tumorale la plus éloignée du centre en fonction du nombre d'itération")

    for x,y in zip(X,Y):
        plt.text(x, y+0.02, '%.02f' % y, ha='center', va= 'bottom')

    plt.ylim(0, 1.5*max(Y))
    plt.show()


def display_moyenne_occ(env, n, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):
    l = moyenne_occ(env, n, iterations, centre, function, p, q)

    X = np.array([i for i in range(iterations)])
    Y1 = []
    Y2 = []
    for k in range(iterations):
        Y1.append(l[k][0])
        Y2.append(l[k][1])
    Y1 = np.array(Y1)
    Y2 = np.array(Y2)

    plt.bar(X, Y1, color = (0.0, 0.0, 0.0, 0.4), label = "Taux de cellules tumorales" )
    plt.bar(X, -Y2, color = (1.0,0.38823529411764707, 0.2784313725490196, 0.4), label = "Taux d'astrocytes")
    plt.legend()
    plt.title("Occupation moyenne de la couche en fonction du nombre d'itérations")

    for x,y in zip(X,Y1):
        plt.text(x, y+0.02, '%.02f' % y, ha='center', va= 'bottom')
    for x, y in zip(X,Y2):
        plt.text(x, -y-0.08, '%.02f' % y, ha='center', va= 'bottom')

    plt.ylim(-1, 1)
    plt.show()


def display_moyenne_distance(env, n, iterations, centre, function = dep_homotype_all, p = 0.5, q = 0.5):

    X = np.array([i for i in range(iterations)])
    Y = moyenne_plus_grande_distance(env, n, iterations, centre, function, p, q)
    Y = np.array(Y)

    plt.bar(X, Y, color = 'darkblue', label = "Distance au centre" )
    plt.legend()
    plt.title("Cellule tumorale la plus éloignée du centre en fonction du nombre d'itération")

    for x,y in zip(X,Y):
        plt.text(x, y+0.02, '%.02f' % y, ha='center', va= 'bottom')

    plt.ylim(0, 1.5*max(Y))
    plt.show() 





if __name__ == '__main__':
    
    env = init_univers(10, 10, (2, 1, 1, 2))  
    centre = (2, 1, 1, 2)
    #display_occ(env, 20, centre, dep_homotype_all, 0.6)
    #display_distance(env, 15, centre, dep_homotype_all, 0.8 )
    #display_moyenne_occ(env, 50, 15, centre, dep_homotype_all, 0.8 )
    display_moyenne_distance(env, 50, 15, centre, dep_homotype_all, 0.8)



