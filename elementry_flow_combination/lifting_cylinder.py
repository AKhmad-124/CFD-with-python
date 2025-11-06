import numpy as np
from matplotlib import pyplot as plt
import elements as ele
sizex = 200
sizey = 200
D1x,D1y = 25,25
V1x,V1y = 25,25

Dstr = 250
Vstr = -25
Vinf = 1

x  = np.linspace(0,50,sizex)
y  = np.linspace(0,50,sizey)
xx,yy = np.meshgrid(x,y)


field1 = ele.doublet(Dstr,D1x,D1y,xx,yy) 
field2 = ele.uniform(Vinf,0,sizex,sizey)
field3 = ele.Vortex(Vstr,V1x,V1y,xx,yy)

field = 0 
field += field1 
field += field2
field += field3

U = field[:, :, 0]
V = field[:, :, 1]

speed = np.sqrt(U**2 + V**2)
speed[speed == 0] = 1e-9  # prevent division by zero
speed[speed >40] = 40

cp = 1-(speed/Vinf)**2

fig, ax = plt.subplots(figsize=(12,12))
ax.quiver(xx, yy, U, V)

fig, ax = plt.subplots(figsize=(12,12))
ax.streamplot(xx, yy, U, V ,density =6)
ax.scatter(D1x,D1y,color='green',s=80)

fig, ax = plt.subplots(figsize=(12,12))
ax.contour(xx,yy,cp)
contf = plt.contourf(xx, yy, cp,levels=np.linspace(-4, 1.0, 100), extend='both',cmap=plt.cm.inferno )
cbar = plt.colorbar(contf)
ax.scatter(D1x,D1y,color='green',s=80)


plt.show()










