#Mariano António Vunge

import numpy as np
import matplotlib.pyplot as plt

def ECampoCargaPontual(q, r0, x, y):
	distance = np.hypot(x - r0[0], y - r0[1])
	return q * (x - r0[0]) / (distance**3), q * (y - r0[1]) / (distance**3)

nx = 135
ny = 135
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)

X, Y = np.meshgrid(x,y)

charges = []

charges.append((1, (0, 0.0)))

Bx = np.zeros((ny, nx))
By = np.zeros((ny, nx))

for charge in charges:
	bx, by = ECampoCargaPontual(*charge, x=X, y=Y)
	Bx += bx
	By += by

fig = plt.figure()
splot = fig.add_subplot(111)

color = np.log(np.hypot(Bx, By))

splot.streamplot(x,y,Bx,By, color=color, linewidth=1, cmap=plt.cm.inferno, density = 1, arrowstyle='->', arrowsize=1)

qColors = {
	True : '#666',
	False : '#9999'
}

splot.set_xlim(-2,2)
splot.set_ylim(-2,2)
splot.set_aspect('equal')

plt.show()
