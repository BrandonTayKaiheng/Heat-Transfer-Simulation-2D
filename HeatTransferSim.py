# Heat Transfer Equation (Transient temperature distribution)
# This script solves the Fourier heat equation in 2D over a grid
# The Finite Difference Algorithm is implemented to provide a numerical solution
# Boundary and intitial conditions can be set
# Returns a heat map and an animated gif

# Author: Brandon Tay Kaiheng

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

# Solver Parameters
base_length = 50
max_iter_time = 750

alpha = 18.46 # Thermal Diffusivity of air in mm^2/s
dx = 1 # Position step size
dt = (dx**2)/(4*alpha)
gamma = (dt*alpha)/(dx**2)

# Initialize Grid (zero array of specified shape)
u = np.empty((max_iter_time, base_length, base_length))
# print(u)

# Initial Conditions
u_initial = 0
u.fill(u_initial) # Populate array with initial condition

# Boundary Conditions (fixed wall temperatures)
u_top = 50 # Assume heat source is at top
u_left = 0 
u_right = 0
u_bottom = 0

u[:, (base_length-1):, :] = u_top
u[:, :, :1] = u_left
u[:, :, (base_length-1):] = u_right
u[:, :1, 1:] = u_bottom

# Finite Difference Method (iterate i,j,k, different start due to 2nd derivative vs 1st derivative)
def heat_calc(u):
    for k in range(0, max_iter_time - 1, 1):
        for i in range(1, base_length - 1, dx):
            for j in range(1, base_length -1, dx):
                u[k+1, i, j] = gamma*(u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]
    
    return u

u = heat_calc(u)

# Data Visualisation
def heat_map(u_k, k):
    plt.clf   # Clear Current Plot
    plt.title(f"Temperature at t = {k*dt:.3f} unit time")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.pcolormesh(u_k, cmap = plt.cm.jet, vmin = -10, vmax = 50)
    plt.colorbar()

    return plt

def animate(k):
    heat_map(u[k], k)

anim = animation.FuncAnimation(plt.figure(), animate, interval = 1, frames = max_iter_time, repeat = False)
anim.save('heat_equation_2.gif')

plt.show()