import matplotlib.animation as anim
import matplotlib.pyplot as plt
import numpy as np


def animation_save():
    ims = []
    fig = plt.figure()
    for i in range(7):
        tab = np.array([[i/10 for j in range(5)] for k in range(5)])
        image = plt.imshow(tab)
        ims.append([image])

    anime = anim.ArtistAnimation(
        fig, ims, blit=True, interval=500, repeat=True)
    return anime


anime = animation_save()

plt.show()
