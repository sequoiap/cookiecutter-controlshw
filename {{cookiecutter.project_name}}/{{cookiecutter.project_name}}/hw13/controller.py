import numpy as np

import {{cookiecutter.project_name}}.parameters as P
import .param13 as P13

class Controller:
    """
    The controller for the system. This is a state feedback controller win an
    integrator and integrator anti-windup.
    """
    def __init__(self):
        # Save desired parameters here
        self.x_hat = np.array([[]]) # Initial estimate for x_hat
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
        x_hat : np.ndarray
            The observer state estimate.
        """
        return

    def update_observer(self, y):
        # update the observer using RK4 integration
        F1 = self.observer_f(self.x_hat, y)
        F2 = self.observer_f(self.x_hat + self.Ts / 2 * F1, y)
        F3 = self.observer_f(self.x_hat + self.Ts / 2 * F2, y)
        F4 = self.observer_f(self.x_hat + self.Ts * F3, y)
        self.x_hat += self.Ts / 6 * (F1 + 2 * F2 + 2 * F3 + F4)
        return self.x_hat

    def observer_f(self, x_hat, y):
        """
        Derivatives of the observer state.

        Returns
        -------
        xhat_dot : np.ndarray
            The derivatives of x_hat as a state column vector.
        """
        return xhat_dot

    def integrateError(self, error):
        """
        Integrates the error and saves it as a data member (no return value).
        """
        pass

    def integratorAntiWindup(self, F, F_unsat):
        """
        Performs integrator anti-windup (no return value).
        """
        pass

    def saturate(self,u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u
