import numpy as np
from matplotlib import pyplot as plt
import elements as ele
sizex = 200
sizey = 200
D1x,D1y = 25,25


x  = np.linspace(0,50,sizex)
y  = np.linspace(0,50,sizey)
xx,yy = np.meshgrid(x,y)


field1 = ele.doublet(250,D1x,D1y,xx,yy) 
field2 = ele.uniform(1,0,sizex,sizey)

field = 0 
field += field1 
field += field2

U = field[:, :, 0]
V = field[:, :, 1]

speed = np.sqrt(U**2 + V**2)
speed[speed == 0] = 1e-9  # prevent division by zero
speed[speed >40] = 40

cp = 1-(speed/1)**2

fig, ax = plt.subplots(figsize=(12,12))
ax.quiver(xx, yy, U, V)

fig, ax = plt.subplots(figsize=(12,12))
# ax.contour(xx,yy,cp)
ax.streamplot(xx, yy, U, V ,density =6)
ax.scatter(D1x,D1y,color='green',s=80)



plt.show()










