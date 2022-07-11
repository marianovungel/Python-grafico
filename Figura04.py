#Mariano António Vunge

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def E(c, r0, x, y):
	distance = np.hypot(x - r0[0], y - r0[1])
	return c * (x - r0[0]) / (distance**3), c * (y - r0[1]) / (distance**3)

nx = 147
ny = 147
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)

X, Y = np.meshgrid(x,y)

charges = []

charges.append((2, (-2, 0.0)))
charges.append((-2, (2, 0.0)))
charges.append((2, (-2, 0.10)))
charges.append((-2, (2, 0.10)))
charges.append((2, (-2, 0.20)))
charges.append((-2, (2, 0.20)))
charges.append((2, (-2, 0.30)))
charges.append((-2, (2, 0.30)))
charges.append((2, (-2, 0.40)))
charges.append((-2, (2, 0.40)))
charges.append((2, (-2, 0.50)))
charges.append((-2, (2, 0.50)))
charges.append((2, (-2, 0.60)))
charges.append((-2, (2, 0.60)))
charges.append((2, (-2, 0.70)))
charges.append((-2, (2, 0.70)))
charges.append((2, (-2, 0.80)))
charges.append((-2, (2, 0.80)))
charges.append((2, (-2, 0.90)))
charges.append((-2, (2, 0.90)))
charges.append((-2, (2, 0.100)))
charges.append((2, (-2, 0.100)))
charges.append((-2, (2, 0.110)))
charges.append((2, (-2, 0.110)))
charges.append((-2, (2, 0.120)))
charges.append((-2, (2, 0.120)))
charges.append((2, (-2, -0.10)))
charges.append((-2, (2, -0.10)))
charges.append((2, (-2, -0.20)))
charges.append((-2, (2, -0.20)))
charges.append((2, (-2, -0.30)))
charges.append((-2, (2, -0.30)))
charges.append((2, (-2, -0.40)))
charges.append((-2, (2, -0.40)))
charges.append((2, (-2, -0.50)))
charges.append((-2, (2, -0.50)))
charges.append((2, (-2, -0.60)))
charges.append((-2, (2, -0.60)))
charges.append((2, (-2, -0.70)))
charges.append((-2, (2, -0.70)))
charges.append((2, (-2, -0.80)))
charges.append((-2, (2, -0.80)))
charges.append((2, (-2, -0.90)))
charges.append((-2, (2, -0.90)))
charges.append((-2, (2, -0.100)))
charges.append((2, (-2, -0.100)))
charges.append((-2, (2, -0.110)))
charges.append((2, (-2, -0.110)))
charges.append((-2, (2, -0.120)))
charges.append((-2, (2, -0.120)))
charges.append((-2, (2, -0.130)))
charges.append((2, (-2, -0.130)))
charges.append((-2, (2, -0.140)))
charges.append((2, (-2, -0.140)))
charges.append((-2, (2, -0.150)))
charges.append((-2, (2, -0.150)))
charges.append((-2, (2, -0.160)))
charges.append((2, (-2, -0.160)))
charges.append((-2, (2, -0.170)))
charges.append((-2, (2, -0.170)))
charges.append((-2, (2, -0.180)))
charges.append((2, (-2, -0.180)))
charges.append((-2, (2, -0.190)))
charges.append((2, (-2, -0.190)))
charges.append((-2, (2, -0.200)))
charges.append((-2, (2, -0.200)))

Mx = np.zeros((ny, nx))
My = np.zeros((ny, nx))

for charge in charges:
	mx, my = E(*charge, x=X, y=Y)
	Mx += mx
	My += my

fig = plt.figure()
splot = fig.add_subplot(111)

color = np.log(np.hypot(Mx, My))

splot.streamplot(x,y,Mx, My, color=color, linewidth=1.5, cmap=plt.cm.inferno, density = 1, arrowstyle='->', arrowsize=1)

qColors = {
	True : '#FF0000',
	False : '#0000FF'
}
for q, pos in charges:
	splot.add_artist(Circle(pos, 0.1, color=qColors[q>0]))

splot.set_xlim(-2,2)
splot.set_ylim(-2,2)
splot.set_aspect('equal')

plt.show()