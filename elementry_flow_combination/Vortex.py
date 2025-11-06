import numpy as np
from matplotlib import pyplot as plt
sizex = 50
sizey = 50

x  = np.arange(sizex)
y  = np.arange(sizey)
xx,yy = np.meshgrid(x,y)

print(xx,yy)
def Vortex(Gamma,locx,locy,xx,yy):
    rmag = np.sqrt((xx-locx)**2+(yy-locy)**2)
    const = -Gamma/2/np.pi/rmag
    u_rx = (xx-locx)/rmag
    u_ry = (yy-locy)/rmag
    u = const*u_ry
    v = -const*u_rx
    field = np.dstack((u, v))
    return field

# field1 = Vortex(-5,3*sizex/4,3*sizey/4,xx,yy)
field2 = Vortex(5,sizex/4,sizey/4,xx,yy) 
field = field2 
# field1 = uniform(10,0,sizex,sizey)


U = field[:, :, 0]
V = field[:, :, 1]


fig, ax = plt.subplots(figsize=(12,12))
# ax.quiver(xx, yy, U, V)
ax.streamplot(xx, yy, U, V ,density = 3)

# ax.streamplot(xx, yy, U, V)
plt.show()










