from data_main import *


uni = create_univers(5, 5)

set_cellC(1, 2, 2, uni)
print(get_cell((0, 2), uni))
print(s_cubic_to_cart((0, 2)))
print(uni)


def affiche(s, q, univers, ax):
    if get_cell((s, q)) == 1:
        # Code vivant
        print("Vivant ", s, q)
        ax.add_patche()


appliquer_fonction(fonction, univers)
