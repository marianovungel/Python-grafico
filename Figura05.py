#Mariano António Vunge

import numpy as np
import matplotlib.pyplot as plt

m = np.arange(-5, 6, 1.61)
c = np.arange(-5, 6, 1.61)

M,C = np.meshgrid(m,c)

Fm = (np.sin(np.sin(C-C))-(C))
Fc = M

plt.figure(figsize=(7,7))

plt.streamplot(M,C,Fm,Fc, density=0.94)

plt.show()