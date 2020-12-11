import numpy as np

import {{cookiecutter.project_name}}.parameters as P
import .loopshape as L

class Controller:
    """
    Controller based on loopshaping design techniques.
    """
    def __init__(self):
        # Grab matrices from ``loopshape.py`` as required and save them here.
        pass

    def update(self, r, y):
        """
        Updates what the control input to the system should be given the 
        reference and current state of the system.

        Parameters
        ----------
        r : np.ndarray
            The column vector of reference values.
        y : np.ndarray
            The column vector of the observable system state.

        Returns
        -------
        u : np.ndarray
            The control input to the system.
        """
        return

    # Add functions below as required

    def saturate(self,u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
