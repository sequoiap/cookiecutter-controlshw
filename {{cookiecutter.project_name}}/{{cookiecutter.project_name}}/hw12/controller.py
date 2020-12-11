import numpy as np

import {{cookiecutter.project_name}}.parameters as P
import .param12 as P12

class Controller:
    """
    The controller for the system. This is a state feedback controller win an
    integrator and integrator anti-windup.
    """
    def __init__(self):
        # Save desired parameters here
        pass

    def update(self, r, x):
        """
        Updates what the control input to the system should be given the 
        reference and current state of the system.

        Parameters
        ----------
        r : np.ndarray
            The column vector of reference values.
        x : np.ndarray
            The column vector of the system state.

        Returns
        -------
        u : np.ndarray
            The control input to the system.
        """
        return

    # Define other functions as needed here


    def saturate(self,u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u

