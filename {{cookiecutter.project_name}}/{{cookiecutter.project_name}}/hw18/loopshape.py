import control as ctrl
import matplotlib.pyplot as plt
import numpy as np 

from {{cookiecutter.project_name}} import parameters as P
import {{cookiecutter.project_name}}.hw10.param10 as P
from {{cookiecutter.project_name}}.utils import bode

from control import TransferFunction as tf


Plant = None

# PLOT = True
PLOT = False

# Plot plant initially without any compensation.
if PLOT:
    pass

#########################################
#   Define Design Specifications
#########################################

#----------- general tracking specification --------
omega_r = 0  # track signals below this frequency
gamma_r = 0  # tracking error below this value
w = np.logspace(np.log10(omega_r)-2, np.log10(omega_r))
if PLOT:
    plt.subplot(211)
    trackPlot, = plt.plot(w, (20*np.log10(1.0/gamma_r))*np.ones(len(w)), color='g', label='tracking spec')

#----------- noise specification --------
omega_n = 0    # attenuate noise above this frequency
gamma_n = 0    # attenuate noise by this amount
w = np.logspace(np.log10(omega_n), np.log10(omega_n)+2)
if PLOT:
    plt.subplot(211)
    noisePlot, = plt.plot(w, (20*np.log10(gamma_n))*np.ones(len(w)), color='g', label='noise spec')


#########################################
#   Control Design
#########################################

C = tf([1], [1])

# Add compensation here


# ###########################################
#  Create Plots
# ###########################################


##############################################
#  Convert Controller to State Space Equations
##############################################
C_ss = ctrl.tf2ss(C)  # convert to state space

########################################################################
#  Convert Controller to discrete transfer functions for implementation
########################################################################
C_in_d = tf.sample(C, P.Ts, method='bilinear') #bilinear: Tustin's approximation ("generalized bilinear transformation" with alpha=0.5)
