# Heat-Transfer-Simulation-2D
Solving the Heat Equation in 2D numerically using the Finite Difference Method. Run the python script to view the output.

https://github.com/BrandonTayKaiheng/Heat-Transfer-Simulation-2D/blob/main/HeatTransferSim.py

## Description
The Fourier Heat Equation (diffusion) is given as follows:

## ∂u / ∂t = α∇ ²u


Where:

u = Temperature at a position

t = time

α = thermal diffusivity of the material

∇ = The Laplace operator


This partial differential equation governs how heat diffuses in a medium (solid) over time.

The Finite Difference algorithm is used to discretize the equation by converting the differential terms into finite difference terms using a Forward Difference method.
Each derivative is approximated by:

![image](https://github.com/BrandonTayKaiheng/Heat-Transfer-Simulation-2D/assets/115394445/f745c04e-9e65-4a55-bae7-ba36636c7274)

In 2D, the discretized heat equation is thus given by:

![image](https://github.com/BrandonTayKaiheng/Heat-Transfer-Simulation-2D/assets/115394445/4921c211-89d1-498a-9479-10ea51180549)

A grid space is first initialized, with 4 walls serving as the system boundaries in which temperature boundary conditions may be set. In this simulation, the top wall was simulated as a heat source at 50 degree Celsius. The other 3 boundaries were set at 0 degree Celsius initially.

Following which, the explicit method was used to calculate the temperature of each grid point for each discrete time step. An animated heatmap was generated to visualize the transient diffusion of heat through the medium via a temperature gradient field. 

Example of output:

![heat_equation_2](https://github.com/BrandonTayKaiheng/Heat-Transfer-Simulation-2D/assets/115394445/703dad2f-f62c-463b-a0dd-dfb81eb2160b)


## Library Dependencies

Numpy

Matplotlib
