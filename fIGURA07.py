#Mariano António Vunge

import numpy as np
import matplotlib.pyplot as plt

def E(m, r0, x, y):
    v=((y-r0[1])**2+(x-r0[0])**2)**1.5
    return m * (y - r0[1])/v, m * (x - r0[0])/v

k = 10**(-10)
x,y = np.meshgrid(np.arange(-5,5,.2), np.arange(-5,5,.2))
c=[]

for i in range (-20,20,1):
    c.append((20,(-0.50,i/10)))
    c.append((20,(-0.50,i/10)))
    c.append((20,(-0.50,i/10)))
    c.append((-20,(0.50,i/10)))
    c.append((-20,(0.50,i/10)))
    c.append((-20,(0.50,i/10)))

My =(J*y/(x**2+y**2))
Mx =(-J*x/(x**2+y**2))

for c in c:
    mx,my = E(*c, x=x, y=y)
    Mx += (-J*mx/(x**2+y**2))
    My += (J*my/(x**2+y**2))

fig = plt.figure()
ax = fig.add_subplot()
ax.streamplot(x,y,Mx,My,arrowsize=0.8,linewidth=2,arrowstyle='->')

ax.set_xlim(-4,4)
ax.set_ylim(-4,4)

plt.show()