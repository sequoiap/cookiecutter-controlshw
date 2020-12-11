import numpy as np

import {{cookiecutter.project_name}}.parameters as P


class Dynamics:
    """
    The dynamics of a system. 

    The parameters for any physical system are never known exactly.  Feedback
    systems need to be designed to be robust to this uncertainty.  In the simulation
    we model uncertainty by changing the physical parameters by a uniform random variable
    that represents alpha*100 % of the parameter, i.e., alpha = 0.2, means that the parameter
    may change by up to 20%.  A different parameter value is chosen every time the simulation
    is run.

    Parameters
    ----------
    alpha : float
        The uncertainty in the parameters.
    """
    def __init__(self, alpha=0.0):
        # Initial state conditions. It should be a column vector, shape (n,1).
        self.state = np.array([[]])

        # Store system parameters within the Python object (using `self`) as
        # necessary.
        self.Ts = P.Ts

    def update(self, u):
        """
        This is the external method that takes the input u at time
        t and returns the output y at time t.

        Parameters
        ----------
        u : np.ndarray
            The column vector of the control inputs, shape (n,1).

        Returns
        -------
        y : np.ndarray
            A column vector of the system's states.
        """
        # Propagate the state by one time sample
        self.rk4_step(u)
        # Return the corresponding output
        y = self.h()
        return y

    def f(self, state, u):
        """
        Calculates the derivatives of your state vector given control inputs,
        the system update equations.

        Parameters
        ----------
        state : np.ndarray
            A column vector representing the current system state, ordered
            in the same way as your initial state vector `self.state`, 
            shape (n,1).
        u : np.ndarray
            A column vector of the control inputs to your system, shape (n,1).

        Returns
        -------
        xdot : np.ndarray
            A column vector of derivatives corresponding to variables in the 
            same order as your state vector, shape (n,1).
        """
        # You can extract the state into its variables using state.item(n).

        
        # You can extract the control input into its variables using u.item(n).
        

        # The equations of motion.


        # Build xdot and return. It should be a column vector, shape (n,1).
        xdot = np.array([[]])
        return xdot

    def h(self):
        """
        Returns the output equations, the part of the state vector that 
        doesn't contain derivatives.

        Returns
        -------
        y : np.ndarray
            The output equations.
        """
        # Extract the variables from the state vector


        # Reconstruct them into a column vector to return
        y = np.array([[]])
        return y

    def rk4_step(self, u):
        """
        Integrates the ODE using the Runge-Kutta RK4 algorithm.

        Parameters
        ----------
        u : np.ndarray
            The column vector representing the control inputs.
        """
        F1 = self.f(self.state, u)
        F2 = self.f(self.state + self.Ts / 2 * F1, u)
        F3 = self.f(self.state + self.Ts / 2 * F2, u)
        F4 = self.f(self.state + self.Ts * F3, u)
        self.state += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)
        