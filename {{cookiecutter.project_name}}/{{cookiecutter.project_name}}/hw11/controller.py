import numpy as np

import {{cookiecutter.project_name}}.parameters as P
import .param11 as P11


class Controller:
    def __init__(self):
        self.K = P11.K  # state feedback gain
        self.kr = P11.kr  # Input gain
        self.limit = P.Fmax  # Maximum force
        self.Ts = P.Ts  # sample rate of controller

    def update(self, z_r, x):
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