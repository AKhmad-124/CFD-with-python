import numpy as np
from matplotlib import pyplot as plt
sizex = 50
sizey = 50
def uniform(V,angle,sizex,sizey):
    Vx = V*np.cos(angle)
    Vy = V*np.sin(angle)
    
    field = np.full((sizex,sizey,2),[Vx,Vy])
    return field

field1 = uniform(10,0,sizex,sizey)

x  = np.arange(sizex)
y  = np.arange(sizey)
xx,yy = np.meshgrid(x,y)


U = field1[:, :, 0]
V = field1[:, :, 1]


fig, ax = plt.subplots(figsize=(12,12))
ax.quiver(xx, yy, U, V)
ax.streamplot(xx, yy, U, V)

plt.show()










