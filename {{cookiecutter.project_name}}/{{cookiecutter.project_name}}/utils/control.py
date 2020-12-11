import control as ctrl
import numpy as np

def bode(*args, **kwargs):
    """
    Wraps the control library's ``bode`` function and passes all the parameters
    straight through. I got tired of converting magnitude to dB and phase to
    degrees after every function call, so now I just call my custom bode 
    function that does it for me! Returns the same thing as ``control.bode``, 
    except that now it's:

    Returns
    -------
    mag : float
        Magnitude in dB
    phase : float
        Phase in degrees
    omega : np.array
        x-axis values over the range of ``mag`` and ``phase``.
    """
    mag, phase, omega = ctrl.bode(*args, **kwargs)
    mag = ctrl.mag2db(mag)
    phase = np.rad2deg(phase)
    return mag, phase, omega
