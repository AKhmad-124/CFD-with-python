import numpy as np
from matplotlib import pyplot as plt
import elements as ele
sizex = 50
sizey = 50
S1x,S1y = 18,25
V1x,V1y = 32,25


x  = np.arange(sizex)
y  = np.arange(sizey)
xx,yy = np.meshgrid(x,y)



field1 = ele.Source(50,S1x,S1y,xx,yy)
field2 = ele.Source(-50,V1x,V1y,xx,yy) 
field3 = ele.uniform(0.5,0,sizex,sizey)
# np.pi/4
field = 0 
field += field1 
field += field2
# field += field3 
# field1 = uniform(10,0,sizex,sizey)


U = field[:, :, 0]
V = field[:, :, 1]

speed = np.sqrt(U**2 + V**2)
speed[speed == 0] = 1e-9  # prevent division by zero
speed = np.log(speed) *2

fig, ax = plt.subplots(figsize=(12,12))
ax.quiver(xx, yy, U, V)
ax.scatter(S1x,S1y,color='red',s=80)
fig, ax = plt.subplots(figsize=(12,12))
ax.streamplot(xx, yy, U, V ,density = 3)
ax.scatter(S1x,S1y,color='green',s=80)
ax.scatter(V1x,V1y,color='red',s=80)

plt.show()

# cmap='viridis'     # smooth green-blue
# cmap='inferno'     # yellow-orange-red
# cmap='plasma'      # purple-pink-yellow
# cmap='cool'        # cyan-magenta
# cmap='turbo'       # vivid rainbow










