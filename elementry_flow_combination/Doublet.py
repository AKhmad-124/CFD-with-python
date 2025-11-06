import numpy as np
from matplotlib import pyplot as plt
import elements as ele
sizex = 50
sizey = 50

x  = np.arange(sizex)
y  = np.arange(sizey)
xx,yy = np.meshgrid(x,y)

def doublet(k,locx,locy,xx,yy): #Lambda = Λ
    dx,dy = (xx-locx),(yy-locy)
    rmag = np.sqrt(dx**2+dy**2)
    rmag[rmag == 0] = 0.0001 #to not divide by zero
    const = k/2/np.pi
    u = -const*(dx**2-dy**2)/(rmag**4)
    v = -const*2*dx*dy/(rmag**4)
    field = np.dstack((u, v))
    return field

field1 = doublet(5,25,25,xx,yy)
field2 = ele.uniform(1,0,sizex,sizey)
field = 0
field = field + field1
field = field + field2


U = field[:, :, 0]
V = field[:, :, 1]


fig, ax = plt.subplots(figsize=(12,12))
# ax.quiver(xx, yy, U, V)
ax.streamplot(xx, yy, U, V)
plt.show()










