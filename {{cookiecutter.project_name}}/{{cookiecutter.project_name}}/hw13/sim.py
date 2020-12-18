import matplotlib.pyplot as plt
import numpy as np

from {{cookiecutter.project_name}} import parameters as P
from {{cookiecutter.project_name}}.utils import SignalGenerator
from {{cookiecutter.project_name}}.hw2.animation import Animation
from {{cookiecutter.project_name}}.hw2.plotter import DataPlotter
from {{cookiecutter.project_name}}.hw3.dynamics import Dynamics
from {{cookiecutter.project_name}}.hw13.controller import Controller
from {{cookiecutter.project_name}}.hw13.observer_plotter import ObserverDataPlotter


def run(live_plot=True, monitor=None):
    """
    Runs a simulation of the system. Simulation parameters are defined in 
    ``{{cookiecutter.project_name}}.parameters``. 

    Parameters
    ----------
    live_plot : bool
        If True, creates a live-updating animation. If False, only shows the
        dataplot results at the end of the full simulation.
    monitor : {{cookiecutter.project_name}}.Monitor
        A monitor object for future test implementation.
    """
    # Instantiate system, controller, and reference classes
    system = Dynamics(alpha=0.0)
    controller = Controller()
    reference = SignalGenerator(amplitude=0.5, frequency=0.1, offset=0.0)
    disturbance = SignalGenerator(amplitude=0.0, frequency=0.0)

    # Instantiate the simulation plots and animation
    dataplot = DataPlotter()
    observer = ObserverDataPlotter()
    animation = Animation()

    # Simulation time starts at t_start
    t = P.t_start 
    y = system.h()  # Output of system at start of simulation

    # Main simulation loop
    while t < P.t_end:  
        # Propagate dynamics in between plot samples
        t_next_plot = t + P.t_plot

        # Update control and dynamics at faster simulation rate
        while t < t_next_plot:
            r = reference.square(t) # Reference input
            d = disturbance.step(t)  # Input disturbance
            x = system.state
            u, x_hat = controller.update(r, y)
            y = system.update(u + d)  # Propagate the dynamics
            t = t + P.Ts  # advance time by Ts
            if monitor:
                monitor.submit_state(y)
        # update animation and data plots
        animation.update(system.state)
        dataplot.update(t, r, system.state, u)
        observer.update(t, system.state, x_hat, d, 0.0)
        plt.pause(0.0001)  # the pause causes the figure to be displayed during the simulation

    # Keeps the program from closing when a simulation ends until the user presses 
    # a button.
    print('Press any key to close')
    plt.waitforbuttonpress()
    plt.close()


if __name__ == "__main__":
    run()
