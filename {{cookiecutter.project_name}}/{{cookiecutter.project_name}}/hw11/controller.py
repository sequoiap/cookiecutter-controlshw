import numpy as np

import {{cookiecutter.project_name}}.parameters as P
import .param11 as P11


class Controller:
    """
    The controller for the system. This is a state feedback controller.
    """
    def __init__(self):
        # Store parameters as desired
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
        # Extract the system states


        # Construct the state linearized around the equilibrium
        

        # Compute equilibrium forces, if any
        

        # Compute the state feedback controller
        

        # Saturate
        
        return

    def saturate(self,u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u