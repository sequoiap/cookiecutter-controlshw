import matplotlib.pyplot as plt
import numpy as np

from {{cookiecutter.project_name}} import parameters as P
from {{cookiecutter.project_name}}.utils import SignalGenerator
from {{cookiecutter.project_name}}.hw2.animation import Animation
from {{cookiecutter.project_name}}.hw2.plotter import DataPlotter
from {{cookiecutter.project_name}}.hw3.dynamics import Dynamics
from {{cookiecutter.project_name}}.hw18.controller import Controller

# Instantiate system, controller, and reference classes
system = Dynamics(alpha=0.0)
controller = Controller()
reference = SignalGenerator(amplitude=0.5, frequency=0.1, y_offset=0.0)
disturbance = SignalGenerator(amplitude=0.0, frequency=0.0)
noise = SignalGenerator(amplitude=0.0)

# Instantiate the simulation plots and animation
dataplot = DataPlotter()
animation = Animation()

# Simulation time starts at t_start
t = P.t_start 
y = system.h() # Output of system at start of simulation

# Main simulation loop
while t < P.t_end:  
    # Propagate dynamics in between plot samples
    t_next_plot = t + P.t_plot

    # Update control and dynamics at faster simulation rate
    while t < t_next_plot:
        r = reference.square(t) # Reference input
        d = disturbance.step(t)  # Input disturbance
        n = np.array([[noise.random(t)]])  # Simulate sensor noise
        u = controller.update(r, y + n)
        y = system.update(u + d)  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts
    # update animation and data plots
    animation.update(system.state)
    dataplot.update(t, r, system.state, u)
    plt.pause(0.0001)  # the pause causes the figure to be displayed during the simulation

# Keeps the program from closing when a simulation ends until the user presses 
# a button.
print('Press any key to close')
plt.waitforbuttonpress()
plt.close()
