#Mariano António Vunge

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def C(q, r0, x, y):
	distance = np.hypot(x - r0[0], y - r0[1])
	return q * (x - r0[0]) / (distance**3), q * (y - r0[1]) / (distance**3)

nx = 135
ny = 135
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)

X, Y = np.meshgrid(x,y)

charges = []

charges.append((1, (-0.6, 0.6)))
charges.append((-1, (0.6, 0.6)))
charges.append((1, (0.6, -0.6)))
charges.append((-1, (-0.6, -0.6)))

Ex = np.zeros((ny, nx))
Ey = np.zeros((ny, nx))

for charge in charges:
	ex, ey = C(*charge, x=X, y=Y)
	Ex += ex
	Ey += ey

fig = plt.figure()
splot = fig.add_subplot(111)

color = np.log(np.hypot(Ex, Ey))

splot.streamplot(x,y,Ex, Ey, color=color, linewidth=0.5, cmap=plt.cm.inferno, density = 2, arrowstyle='->', arrowsize=1)

qColors = {
	True : '#FF0000',
	False : '#0000FF'
}
for q, pos in charges:
	splot.add_artist(Circle(pos, 0.05, color=qColors[q>0]))

splot.set_xlim(-2,2)
splot.set_ylim(-2,2)
splot.set_aspect('equal')

plt.show()
