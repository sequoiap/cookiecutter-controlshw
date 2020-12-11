import numpy as np

import {{cookiecutter.project_name}}.parameters as P
import .param7 as P7


class Controller:
    """
    The controller for the system. This is a PD controller.
    """
    def __init__(self):
        # Instantiates the PD parameters
        self.kp = P7.kp
        self.kd = P7.kd
        self.limit = None

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
        # Extract the states from the state vector
        

        # Calculate equlibrium values, if any
        

        # Compute the linearized control inputs using PD control
        

        # Compute total control


        # Always saturate to protect hardware
        

        return

    def saturate(self, u):
        """
        Limits the control input to some value defined by `self.limit`.
        If the magnitude of the value is greater than the limit, is rails
        at the limit value, with the same sign. 
        
        Note
        ----
        Some controllers may want to implement this differently, depending on 
        the type of control input. For example, some control inputs may not
        be able to go negative, in which case you may saturate to also be 
        greater than 0.
        """
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
