#Mariano António Vunge

import numpy as np
import matplotlib.pyplot as plt

def W(q, r, x, y):
    den = -((x+r[0])**2 + (y+r[1])**2)**1.5
    return q * (x + r[0]) / den, q * (y + r[1]) / den

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)

nq, d = 60, 0.1
charges = []
for i in range(nq):
    charges.append((-1, (i/(nq-1)*2-1, -d/2)))
    charges.append((1, (i/(nq-1)*2-1, d/2)))

Ex, Ey = np.zeros((50, 50)), np.zeros((50, 50))
for charge in charges:
    ex, ey = W(*charge, x=X, y=Y)
    Ex += ex
    Ey += ey

fig = plt.figure(figsize=(8, 8))
splot = fig.add_subplot(111)

splot.streamplot(x, y, Ex, Ey, linewidth=1.2, density=1.5)

splot.set_xlim(-5,5)
splot.set_ylim(-5,5)

plt.show()