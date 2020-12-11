import matplotlib.pyplot as plt
import numpy as np

from {{cookiecutter.project_name}} import parameters as P
from {{cookiecutter.project_name}}.utils import SignalGenerator
from {{cookiecutter.project_name}}.hw2.animation import Animation
from {{cookiecutter.project_name}}.hw2.plotter import DataPlotter


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
    # Instantiate all the necessary reference generators (may be more than one).
    reference = SignalGenerator(amplitude=0.5, frequency=0.1)

    # Instantiate the simulation plots and animation
    dataplot = DataPlotter()
    animation = Animation()

    # Simulation time starts at t_start
    t = P.t_start 

    # Main simulation loop
    while t < P.t_end:  
        # Set variables
        r = reference.square(t) # Mocks reference
        u = reference.sin(t)    # Mocks control inputs
        
        # Update animation
        state = None # Replace this with a "mock" state for testing your animation
        animation.update(state)
        dataplot.update(t, r, state, u)

        # Advance time by t_plot
        t = t + P.t_plot
        if live_plot:
            plt.pause(0.0001)

    # Keeps the program from closing when a simulation ends until the user presses 
    # a button.
    print('Press any key to close')
    plt.waitforbuttonpress()
    plt.close()

    return dataplot


if __name__ == "__main__":
    run()
