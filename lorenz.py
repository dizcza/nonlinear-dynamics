import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0


def lorenz_dynamics(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives


state0 = [10.0, 15.0, 100.0]
t = np.arange(0.0, 4000.0, 0.01)

states = odeint(lorenz_dynamics, state0, t)

fig = plt.figure()
ax = fig.gca(projection="3d")
ax.plot(states[:, 0], states[:, 1], states[:, 2], lw=0.5)
plt.draw()
plt.show()
