from data_main import *


uni = create_univers(5, 5)

set_cell(1, 0, 2, uni)
print(uni)

print(get_adj(1, 0, uni))
