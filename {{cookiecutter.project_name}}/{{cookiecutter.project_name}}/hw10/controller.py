import numpy as np

import {{cookiecutter.project_name}}.parameters as P
import .param10 as P10


class Controller:
    """
    The controller for the system. This is a PD controller.
    """
    def __init__(self):
        # Instantiates the PD parameters
        self.kp = P10.kp
        self.kd = P10.kd
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


class PIDControl:
    """
    A class for computing PID control values.

    Parameters
    ----------
    kp : float
    ki : float
    kd : float
    limit : float
    beta : float
    Ts : float
    """
    def __init__(self, kp, ki, kd, limit, beta, Ts):
        self.kp = kp                 # Proportional control gain
        self.ki = ki                 # Integral control gain
        self.kd = kd                 # Derivative control gain
        self.limit = limit           # The output will saturate at this limit
        self.beta = beta             # gain for dirty derivative
        self.Ts = Ts                 # sample rate

        self.y_dot = 0.0              # estimated derivative of y
        self.y_d1 = 0.0              # Signal y delayed by one sample
        self.error_dot = 0.0          # estimated derivative of error
        self.error_d1 = 0.0          # Error delayed by one sample
        self.integrator = 0.0        # integrator

    def PID(self, y_r, y, flag=True):
        """
        PID control output. `error_dot` and `y_dot` are computed numerically 
        using a dirty derivative. Integral (error) is computed numerically 
        using trapezoidal approximation.

        Parameters
        ----------
        y_r : float
            The reference command.
        y : float
            The current value.
        flag : bool
            If `True`, the derivative gain operates on the derivative of the 
            error. Otherwise, operates on the derivative of the output; i.e.,
            if flag==True, then returns
                u = kp*error + ki*integral(error) + kd*error_dot.
            else returns 
                u = kp*error + ki*integral(error) - kd*y_dot.

        Returns
        -------
        u_sat : float
            The saturated control input to the system.
        """

        # Compute the current error
        error = y_r - y
        # integral needs to go before derivative to update error_d1 correctly
        self.integrate_error(error)
        # differentiate error and y
        self.differentiate_error(error)
        self.differentiate_y(y)

        # PID Control
        if flag is True:
            u_unsat = self.kp*error + self.ki*self.integrator + self.kd*self.error_dot
        else:
            u_unsat = self.kp*error + self.ki*self.integrator - self.kd*self.y_dot
        # return saturated control signal
        u_sat = self.saturate(u_unsat)
        self.integrator_anti_windup(u_sat, u_unsat)
        return u_sat

    def PD(self, y_r, y, flag=True):
        '''
        PD control (no integrator). `error_dot` and `y_dot` are computed 
        numerically using a dirty derivative.

        Parameters
        ----------
        y_r : float
            The reference command.
        y : float
            The current value.
        flag : bool
            If `True`, the derivative gain operates on the derivative of the 
            error. Otherwise, operates on the derivative of the output; i.e.,
            if flag==True, then returns
                u = kp*error + kd*error_dot.
            else returns 
                u = kp*error - kd*y_dot.
            
        Returns
        -------
        u_sat : float
        '''

        # Compute the current error
        error = y_r - y
        # differentiate error and y
        self.differentiate_error(error)
        self.differentiate_y(y)

        # PD Control
        if flag is True:
            u_unsat = self.kp*error + self.kd*self.error_dot
        else:
            u_unsat = self.kp*error - self.kd*self.y_dot
        # return saturated control signal
        u_sat = self.saturate(u_unsat)
        return u_sat

    def differentiate_error(self, error):
        '''
        differentiate the error signal
        '''
        self.error_dot = self.beta*self.error_dot + (1-self.beta)*((error - self.error_d1) / self.Ts)
        self.error_d1 = error

    def differentiate_y(self, y):
        '''
            differentiate y
        '''
        self.y_dot = self.beta*self.y_dot + (1-self.beta)*((y - self.y_d1) / self.Ts)
        self.y_d1 = y

    def integrate_error(self, error):
        '''
            integrate error
        '''
        self.integrator = self.integrator + (self.Ts/2)*(error+self.error_d1)

    def integrator_anti_windup(self, u_sat, u_unsat):
         # integrator anti - windup
         if self.ki != 0.0:
            self.integrator = self.integrator + self.Ts/self.ki*(u_sat-u_unsat);

    def saturate(self,u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u