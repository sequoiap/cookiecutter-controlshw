[Home](README.md)

Previous Topic: [Python Packages: Imports explained](python_imports.md)

# System Simulation: The structure of a simulation

You're going to become very familiar with a file included in almost every
"hw\[n\]" folder: `sim.py`. In just about it's most complex iteration, it has
the following form:

```
import matplotlib.pyplot as plt
import numpy as np

from project_name import parameters as P
from project_name.utils import SignalGenerator
from project_name.hw2.animation import Animation
from project_name.hw2.plotter import DataPlotter
from project_name.hw3.dynamics import Dynamics
from project_name.hw18.controller import Controller


def run(live_plot=True):
    """
    Runs a simulation of the system. Simulation parameters are defined in 
    ``{{cookiecutter.project_name}}.parameters``. 

    Parameters
    ----------
    live_plot : bool
        If True, creates a live-updating animation. If False, only shows the
        dataplot results at the end of the full simulation.
    """
    # Instantiate system, controller, and reference classes
    system = Dynamics(alpha=0.0)
    controller = Controller()
    reference = SignalGenerator(amplitude=0.5, frequency=0.1, offset=0.0)
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


if __name__ == "__main__":
    run()
```

The code is already well commented, but just so you have a detailed explanation
of what's happening in every step, well--let's go over it section by section 
here as well. You'll want to know how to do this on your own, after all--you'll
likely have to create your own working simulation on a midterm or final!

## Import third party libraries

We use several useful functions from other libraries. So we import them first.

```
import matplotlib.pyplot as plt
import numpy as np
```

## Import project resources

The file that runs the simulation simply pulls together resources we've already
implemented in other places throughout the project, like the system dynamics,
the data plotters, and the controllers. The simulation file mainly acts to link
them all together, making sure the right information gets passed between them.

```
from project_name import parameters as P
from project_name.utils import SignalGenerator
from project_name.hw2.animation import Animation
from project_name.hw2.plotter import DataPlotter
from project_name.hw3.dynamics import Dynamics
from project_name.hw18.controller import Controller
```

## The `run()` function

The file implements a single function, `run()`, that contains all the code to
run a simulation. Why implement it as a function, instead of a script? In the
future, we may want to implement a system that can autograde or give feedback
on how well tuned simulations are. In order for it to access your
implementation, it needs to be able to *call* your simulation. So, it's a
function.

Functions in Python ought to be documented. Documentation is usually emphasized
in computer science classes. In this project, we adhere to the 
[numpydoc](https://numpydoc.readthedocs.io/en/latest/) standard.

```
def run(live_plot=True):
    """
    Runs a simulation of the system. Simulation parameters are defined in 
    ``{{cookiecutter.project_name}}.parameters``. 

    Parameters
    ----------
    live_plot : bool
        If True, creates a live-updating animation. If False, only shows the
        dataplot results at the end of the full simulation.
    """
```

## Instantiated objects

We create instances of all our classes to actually have an object to work with.

* **Dynamics** is a model of how our system behaves given certain inputs.
* **Controller** calculates what inputs should be given to our system, given
  its current configuration
* **SignalGenerator** creates sine waves, square waves, random noise, etc.
  depending on how its used. We also use them as references to tell our system
  how we want it to behave.

The other objects should be pretty self-explanatory.

```
    # Instantiate system, controller, and reference classes
    system = Dynamics(alpha=0.0)
    controller = Controller()
    reference = SignalGenerator(amplitude=0.5, frequency=0.1, offset=0.0)
    disturbance = SignalGenerator(amplitude=0.0, frequency=0.0)
    noise = SignalGenerator(amplitude=0.0)

    # Instantiate the simulation plots and animation
    dataplot = DataPlotter()
    animation = Animation()
```

## The simulation

We set the simulation start time and iterate through updating the system's
dynamics, the controller's reference inputs, etc. each time we advance by some
time step.

Since updating plots is processor-intensive (i.e., SLOW), we update them at a
slower rate but still fast enough for us to not really notice with our eyes.

```
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
```

## Keeping the program alive

Typically, when a program runs to completion, it automatically exits. In our
case, we'd like to look at our graphs of system performance once the simulation
has ended, so we want the program to stay open. Matplotlib contains a function
to keep its graph windows open that we use to make the program wait before
exiting.

```
    # Keeps the program from closing when a simulation ends until the user presses 
    # a button.
    print('Press any key to close')
    plt.waitforbuttonpress()
    plt.close()
```

## Running our function if the file is run as a script

Since our program is written as a function, we add this statement to the bottom
of the file that says "if this file is run as a script, call the `run()`
function." In most formal Python programs, this is considered the "Pythonic"
way of doing things (as opposed to not having a function and having everything
written as a script).

```
if __name__ == "__main__":
    run()
```

---

Next Topic: [Testing: The test runner](testing.md)