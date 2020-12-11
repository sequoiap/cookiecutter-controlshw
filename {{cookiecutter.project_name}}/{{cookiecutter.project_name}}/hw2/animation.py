import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np 

import {{cookiecutter.project_name}}.parameters as P


class Animation:
    '''
    A matplotlib window containing an animation for the system. There are
    no parameters for initialization, as the Animation object can directly
    access the parameters in {{cookiecutter.project_name}}.parameters.
    '''
    def __init__(self):
        pass

    def update(self, u):
        """
        Updates the animation, given a system state. This function does not
        return any value.

        Parameters
        ----------
        u : np.ndarray
            A vector of shape (n,1) containing the state vector of the system.
        """
        pass
