import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pandas as pd
import xlrd
import openpyxl

"""
Zad1

fig = plt.figure()
ax = fig.gca(projection='3d')
z = np.linspace(0, 2 * np.pi, 100)
x = np.sin(z)
y = 2 * np.cos(z)

ax.plot(x, y, z, label="Wykres")
ax.legend()
plt.show()
"""

"""
Zad2

np.random.seed(19680801)

def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', -20, 0),
                          ('b', '^', -40, -20),
                          ('g', 'D', -60, -40),
                          ('y', 's', -80, -60),
                          ('k', '*', -100, -80)]:

    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label")
plt.show()
"""

"""
Zad3

fig = plt.figure()
ax = fig.gca(projection='3d')

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x,y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)

#surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#surf = ax.plot_surface(x, y, z, cmap=cm.twilight, linewidth=0, antialiased=False)
#surf = ax.plot_surface(x, y, z, cmap=cm.BuPu, linewidth=0, antialiased=False)
#surf = ax.plot_surface(x, y, z, cmap=cm.viridis, linewidth=0, antialiased=False)
surf = ax.plot_surface(x, y, z, cmap=cm.turbo, linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
"""

"""
Zad4

fig = plt.figure(figsize=(8,3))
ax1 = fig.add_subplot(321, projection='3d')
ax2 = fig.add_subplot(322, projection='3d')
ax3 = fig.add_subplot(323, projection='3d')
ax4 = fig.add_subplot(324, projection='3d')
ax5 = fig.add_subplot(325, projection='3d')

_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title("Wykres zacieniony")
ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
ax2.set_title("Wykres niezacieniony")
ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color='yellow')
ax3.set_title("Wykres zacieniony")
ax4.bar3d(x, y, bottom, width, depth, top, shade=False, color='black')
ax4.set_title("Wykres niezacieniony")
ax5.bar3d(x, y, bottom, width, depth, top, shade=True, color='green')
ax5.set_title("Wykres zacieniony")
plt.show()
"""

"""
Zad5

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x,y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)

xx = np.arange(-5, 5, 0.1)
yy = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(xx,yy)
rr = np.sqrt(xx**2 + yy**2)
zz = np.sin(rr)

surf1 = ax1.plot_surface(x, y, z, cmap=cm.turbo, linewidth=0, antialiased=False)
surf2 = ax2.plot_surface(xx, yy, zz, cmap=cm.turbo, linewidth=0, antialiased=True)


ax1.set_zlim(-1.01, 1.01)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf1, shrink=0.5, aspect=5)

ax2.set_zlim(-1.01, 1.01)
ax2.zaxis.set_major_locator(LinearLocator(10))
ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf2, shrink=0.5, aspect=5)
plt.show()
"""
