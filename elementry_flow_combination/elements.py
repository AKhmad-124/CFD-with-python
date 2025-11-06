import numpy as np

def uniform(V,angle,sizex,sizey):
    Vx = V*np.cos(angle)
    Vy = V*np.sin(angle)
    
    field = np.full((sizex,sizey,2),[Vx,Vy])
    return field

def Source(Λ,locx,locy,xx,yy): #Lambda = Λ
    rmag = np.sqrt((xx-locx)**2+(yy-locy)**2)
    rmag[rmag == 0] = 1
    const = Λ/2/np.pi/rmag
    u_rx = (xx-locx)/rmag
    u_ry = (yy-locy)/rmag
    u = const*u_rx
    v = const*u_ry
    field = np.dstack((u, v))
    return field


def Vortex(Gamma,locx,locy,xx,yy):
    rmag = np.sqrt((xx-locx)**2+(yy-locy)**2)
    rmag[rmag == 0] = 1
    const = -Gamma/2/np.pi/rmag
    u_rx = (xx-locx)/rmag
    u_ry = (yy-locy)/rmag
    u = const*u_ry
    v = -const*u_rx
    field = np.dstack((u, v))
    return field

def doublet(k,locx,locy,xx,yy): #Lambda = Λ
    dx,dy = (xx-locx),(yy-locy)
    rmag = np.sqrt(dx**2+dy**2)
    rmag[rmag == 0] = 0.0001 #to not divide by zero
    const = k/2/np.pi
    u = -const*(dx**2-dy**2)/(rmag**4)
    v = -const*2*dx*dy/(rmag**4)
    field = np.dstack((u, v))
    return field









