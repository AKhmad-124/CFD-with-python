import numpy as np
from matplotlib import pyplot as plt
import elements as ele
sizex = 50
sizey = 50
S1x,S1y = 25,25
V1x,V2y = 25,25

S2x,S2y = 12,35
S3x,S3y = 37,S2y


x  = np.arange(sizex)
y  = np.arange(sizey)
xx,yy = np.meshgrid(x,y)



field1 = ele.Source(-230,S1x,S1y,xx,yy)
field2 = ele.Vortex(150,V1x-5,V2y,xx,yy) 
field3 = ele.uniform(5.5,np.pi/2,sizex,sizey)
field4 = ele.Vortex(-150,V1x+5,V2y,xx,yy) 
field5 = ele.Source(-110,S2x,S2y,xx,yy)
field6 = ele.Source(-110,S3x,S3y,xx,yy)



field = 0 
field += field1 
field += field2
field += field3 
field += field4 
field += field5 
field += field6 
# field1 = uniform(10,0,sizex,sizey)
print("here")

U = field[:, :, 0]
V = field[:, :, 1]

speed = np.sqrt(U**2 + V**2)
speed[speed == 0] = 1e-9  # prevent division by zero
speed[speed >40] = 40



fig, ax = plt.subplots(figsize=(14,14))
ax.quiver(xx, yy, U, V)
ax.scatter(S1x,S1y,color='red',s=80)
fig, ax = plt.subplots(figsize=(10,10))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.streamplot(xx, yy, U, V ,density = 14,color=speed,cmap=plt.cm.viridis)
# ax.scatter(S1x,S1y,color='yellow',s=80)
ax.scatter(S1x+5.5,S1y+.5,color='red',s=80)
ax.scatter(S1x-5.5,S1y+.5,color='red',s=80)

plt.show()










