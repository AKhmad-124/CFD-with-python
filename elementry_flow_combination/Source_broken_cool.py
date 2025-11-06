import numpy as np
from matplotlib import pyplot as plt
sizex = 50
sizey = 50

x  = np.arange(sizex)
y  = np.arange(sizey)
xx,yy = np.meshgrid(x,y)

def Source(Λ,locx,locy,xx,yy): #Lambda = Λ
    const = Λ/2/np.pi
    rmag = np.sqrt((xx-locx)**2+(yy-locy)**2)
    u_u = (xx-locx)/rmag
    u_v = (yy-locy)/rmag
    r = np.dstack((u_u, u_v))
    field = const/r
    return field

field2=Source(5,sizex/2,sizey/2,xx,yy) 

# field1 = uniform(10,0,sizex,sizey)

U = field2[:, :, 0]
V = field2[:, :, 1]


fig, ax = plt.subplots(figsize=(12,12))
ax.quiver(xx, yy, U, V)
ax.streamplot(xx, yy, U, V)
plt.show()










