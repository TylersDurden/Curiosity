import matplotlib.pyplot as plt
import numpy as np
import sys
import os


def snap_image(file_name):
    os.system('raspistill -o '+file_name)
    imat = np.array(plt.imread(file_name))
    os.system('rm '+file_name)
    return imat


if '-snap' in sys.argv:
    image = snap_image(sys.argv[2])
    plt.imshow(image)
    plt.show()
