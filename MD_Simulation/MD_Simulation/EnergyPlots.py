import matplotlib.pyplot as plt
import numpy as np

# Please note:
#     - filename input should not include .txt, e.g. for a file called energies.txt, filename = 'energies'
#     - delim input should contain the delimiter between columns in the .txt, e.g. ','
#     - del_t should be the actual time step for the simulation
#     - Columns of the txt file should be:
#              Column 1: time step number, e.g. 1, 2, 3, etc., not the actual time values
#              Column 2: total system kinetic energy at each time step
#              Column 3: total system potential energy at each time step

## Plot total system kinetic energy vs. time
def PlotKinetic(filename,delim,del_t):
    data = np.loadtxt(filename,delimiter=delim) # read in data
    t_step = data[:,0] # extract t_step numbers from 1st column
    E_kinetic = data[:,1] # extract kinetic energy from 2nd column
    t_vec = del_t*t_step # generate vector of times
    plt.plot(t_vec,E_kinetic) # plot kinetic energy vs. time
    plt.xlabel('Time')
    plt.ylabel('Total System Kinetic Energy')
    plt.show() # display plot
    return 0

## Plot total system kinetic energy vs. time
def PlotPotential(filename,delim,del_t):
    data = np.loadtxt(filename, delimiter=delim) # read in data
    t_step = data[:, 0] # extract t_step numbers from 1st column
    E_potential = data[:, 2] # extract potential energy from 3rd column
    t_vec = del_t * t_step # generate vector of times
    plt.plot(t_vec, E_potential) # plot potential energy vs. time
    plt.xlabel('Time')
    plt.ylabel('Total System Potential Energy')
    plt.show() # display plot
    return 0

def PlotError(filename,delim,del_t):
    data = np.loadtxt(filename, delimiter=delim) # read in data
    t_step = data[:, 0] # extract t_step numbers from 1st column
    E_kinetic = data[:,1] # extract kinetic energies from 3rd column
    E_potential = data[:, 2] # extract potential energies from 3rd column
    E_total = E_kinetic + E_potential
    E_total_init = E_total[0] # total system energy at t = 0
    E_ratio = E_total/E_total_init # ratio of total energy to initial total energy
    E_err = 1.0 - E_ratio # energy error
    t_vec = del_t * t_step # generate vector of times
    plt.plot(t_vec, E_err)
    plt.xlabel('Time')
    plt.ylabel('Total System Energy Error')
    plt.show() # display plot
    return 0
