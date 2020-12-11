import numpy as np

class SignalGenerator:
    """
    Yields the result of some type of signal given the current time value.

    Parameters
    ----------
    amplitude : float, optional
        The signal amplitude, default 1.0.
    frequency : float
        The signal frequency in Hz, default 0.001.
    y_offset : float
        The offset of the signal from zero, default 0.

    Examples
    --------
    >>> sg = SignalGenerator(1.0, 1.0, 0.0)
    >>> t = np.linspace(0, 10)
    >>> y = sg.sawtooth(t)
    >>> plt.plot(t, y)
    >>> plt.show()
    """
    def __init__(self, amplitude=1.0, frequency=0.001, offset=0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.y_offset = offset

    def square(self, t):
        """
        Returns the value of a square signal at time t.

        Parameters
        ----------
        t : float
            The current simulation time.
        
        Returns
        -------
        out : float
            The offset +/- the amplitude, depending on time.
        """
        if t % (1.0/self.frequency) <= 0.5/self.frequency:
            out = self.amplitude + self.y_offset
        else:
            out = - self.amplitude + self.y_offset
        return out

    def sawtooth(self, t):
        """
        Returns the value of a sawtooth wave at some given time. Values range
        between ``y_offset`` +/- ``amplitude``. The sawtooth rises smoothly
        only in the upward direction and then resets to its initial value 
        before rising again. Pictorially, this is:

         /| /| /| /|
        / |/ |/ |/ |

        Parameters
        ----------
        t : float
            The current simulation time.

        Returns
        -------
        out : float
            The value of the sawtooth at the time t.
        """
        tmp = t % (0.5/self.frequency)
        out = 4 * self.amplitude * self.frequency*tmp \
              - self.amplitude + self.y_offset
        return out

    def step(self, t):
        """
        Returns the value of a step signal, stepping up at time 0.

        Parameters
        ----------
        t : float
            The current simulation time.
        
        Returns
        -------
        out : float
            The offset if time < 0, else offset plus amplitude.
        """
        if t >= 0.0:
            out = self.amplitude + self.y_offset
        else:
            out = self.y_offset
        return out

    def random(self, t):
        """
        Returns a random value from a normal distribution with mean 
        ``y_offset`` and standard deviation ``amplitude``.

        Parameters
        ----------
        t : float
            The current simulation time.
        
        Returns
        -------
        out : float
            A random value from a normal distribution.
        """
        out = np.random.normal(self.y_offset, self.amplitude)
        return out

    def sin(self, t):
        """
        Returns a value from a sine wave given current time.

        Parameters
        ----------
        t : float
            The current simulation time.
        
        Returns
        -------
        out : float
            The value of a sine wave with the given parameters at time t.
        """
        out = self.amplitude * np.sin(2*np.pi*self.frequency*t) \
              + self.y_offset
        return out
        