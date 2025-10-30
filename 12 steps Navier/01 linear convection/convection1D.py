import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
nx = 81

dx = 2 / (nx - 1)
nt = 25
dt = 0.025
c = 1

# Initial condition
u = np.ones(nx)
u[int(0.5 / dx):int(1 / dx + 1)] = 2

x = np.linspace(0, 2, nx)

fig, ax = plt.subplots()
line, = ax.plot(x, u, lw=2)
ax.set_ylim(0.5, 2.5)
ax.set_xlim(0, 2)
ax.set_xlabel('x')
ax.set_ylabel('u')
ax.set_title('1D Linear Convection')

def update(frame):
    global u
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])
    line.set_ydata(u)
    return line,

ani = FuncAnimation(fig, update, frames=nt, interval=200, blit=True, repeat=False)
ani.save('linear_convection_bad.gif', fps=10)


plt.show()