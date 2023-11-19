# Heat-Transfer-Simulation-2D
Solving the Heat Equation in 2D numerically using the Finite Difference Method 
\
The Fourier Heat Equation (diffusion) is given as follows:

\ ∂u / ∂t = α∇ ²u
\
\ Where:
\ u = Temperature at a position, x
\ t = time
\ α = thermal diffusity of the material
\ ∇ = The LaPlace operator

This partial differential equation governs how heat diffuses in a medium (solid) over time.

The Finite Difference algorithm is used to descretize the equation by converting the differential terms into finite difference terms
Each derivative is approximated by:

\ ![image](https://github.com/BrandonTayKaiheng/Heat-Transfer-Simulation-2D/assets/115394445/f745c04e-9e65-4a55-bae7-ba36636c7274)

In 2D, the discretized heat equation is given by:

\ ![image](https://github.com/BrandonTayKaiheng/Heat-Transfer-Simulation-2D/assets/115394445/4921c211-89d1-498a-9479-10ea51180549)

A grid space is first initialized, with 4 walls serving as the system boundaries in which temeperature boundary conditions may be set. In this simulation, the top wall was simulated as a heat source. 

Following which, the explicit method was used to calculate the temperature of each grid point for each discrete time step. 

Example of output:
![heat_equation_2](https://github.com/BrandonTayKaiheng/Heat-Transfer-Simulation-2D/assets/115394445/703dad2f-f62c-463b-a0dd-dfb81eb2160b)
