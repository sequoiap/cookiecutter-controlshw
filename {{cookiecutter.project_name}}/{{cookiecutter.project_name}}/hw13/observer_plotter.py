import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D
import numpy as np

# Enable interactive drawing
plt.ion()

class ObserverDataPlotter:
    """
    Creates a dynamic data plot window that can be updated.

    The number of rows and columns can be specified in the init function, but
    are not taken as parameters as this value shouldn't need to change between
    homework assignments.

    You should create different lists and plots to contain the various data 
    histories of interest. You should not have to edit the CustomSubplot class,
    however.
    """
    def __init__(self):
        # Number of subplots = num_of_rows*num_of_cols
        self.num_rows = 3    # Number of subplot rows
        self.num_cols = 1    # Number of subplot columns

        # Crete figure and axes handles
        self.fig, self.ax = plt.subplots(self.num_rows, self.num_cols, sharex=True)

        # Instantiate lists to hold the time and data histories.  Create more 
        # data histories as necessary to store and display all the desired
        # information. Use sensible names! Those listed here are just template
        # values that can be replaced or renamed as you see fit.
        self.time_history = []  # time
        self.z_history = []  # position z
        self.z_hat_history = []  # estimate of z
        self.d_history = []  # estimate of disturbance
        self.z_dot_history = []
        self.z_hat_dot_history = []
        self.d_hat_history = []

        # Create a handle for every subplot. If you want to add more subplots
        # or rows, make sure to add more handles with increasing index values
        # for self.ax[n]! You can see the arguments for CustomSubplot below.
        self.handle = []
        self.handle.append(CustomSubplot(self.ax[0], ylabel='z (m)', title='Data'))
        self.handle.append(CustomSubplot(self.ax[1], ylabel='z_dot (m/s)'))
        self.handle.append(CustomSubplot(self.ax[2], xlabel='t(s)', ylabel='d'))

    def update(self, t, x, x_hat, d, d_hat):
        '''
        Add to the time and data histories and update the plots.

        This function does not return anything.

        Parameters
        ----------
        t : int or float
            The current simulation time.
        x : np.ndarray
            The state vector representing the current system state, of 
            shape (n,1).
        x_hat : np.ndarray
            The estimated state vector, shape (n,1).
        d : float
            The current disturbance value.
        d_hat : float
            The estimated disturbance value.
        '''
        # Update the time history of all plot variables. Note indices may need
        # to change to match your state vectors.
        self.time_history.append(t)  # time
        self.z_history.append(x.item(0))
        self.z_dot_history.append(x.item(1))
        self.z_hat_history.append(x_hat.item(0))
        self.z_hat_dot_history.append(x_hat.item(1))
        self.d_history.append(d)
        self.d_hat_history.append(d_hat)

        # Update the plots with associated histories
        self.handle[0].update(self.time_history, [self.z_history, self.z_hat_history])
        self.handle[1].update(self.time_history, [self.z_dot_history, self.z_hat_dot_history])
        self.handle[2].update(self.time_history, [self.d_history, self.d_hat_history])


class CustomSubplot:
    ''' 
    Creates and manages each individual subplot. This class shouldn't need to 
    be changed for any of the different problems.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        This is a handle to the axes of the figure.
    xlabel : str
        Label of the x-axis.
    ylabel : str
        Label of the y-axis.
    title : str
        Plot title.
    legend : tuple of str
        A tuple of strings that identify the data. 
        Example: ("data1", "data2", ..., "dataN")
    '''
    def __init__(self, ax, xlabel='', ylabel='', title='', legend=None):
        self.legend = legend
        self.ax = ax                  # Axes handle

        # A list of colors. The first color in the list corresponds
        # to the first line object, etc.
        # 'b' - blue, 'g' - green, 'r' - red, 'c' - cyan, 'm' - magenta
        # 'y' - yellow, 'k' - black
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b']
        
        # A list of line styles.  The first line style in the list
        # corresponds to the first line object.
        # '-' solid, '--' dashed, '-.' dash_dot, ':' dotted
        self.line_styles = ['-', '-', '--', '-.', ':']

        self.line = []

        # Configure the axes
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlabel(xlabel)
        self.ax.set_title(title)
        self.ax.grid(True)

        # Keeps track of initialization
        self.init = True   

    def update(self, time, data):
        ''' 
        Adds data to the plot.  

        Parameters
        ----------
        time : list of int or floath
            The time values for the x-axis.
        data : list of lists
            A list of lists; a list corresponds to a line on the plot, and 
            the list of lists contains each separate list, or line.
        '''
        # Initialize the plot the first time routine is called
        if self.init == True:
            for i in range(len(data)):
                # Instantiate line object and add it to the axes
                self.line.append(Line2D(time,
                                        data[i],
                                        color=self.colors[np.mod(i, len(self.colors) - 1)],
                                        ls=self.line_styles[np.mod(i, len(self.line_styles) - 1)],
                                        label=self.legend if self.legend != None else None))
                self.ax.add_line(self.line[i])
            self.init = False
            # Add legend if one is specified
            if self.legend != None:
                plt.legend(handles=self.line)
        else: # Add new data to the plot
            # Updates the x and y data of each line.
            for i in range(len(self.line)):
                self.line[i].set_xdata(time)
                self.line[i].set_ydata(data[i])

        # Adjusts the axis to fit all of the data
        self.ax.relim()
        self.ax.autoscale()
           

