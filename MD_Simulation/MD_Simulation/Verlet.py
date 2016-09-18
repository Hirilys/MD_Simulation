#### VERLET INTEGRATOR #####

### VERSION 2.0
# Updates: All functions treat all atoms as opposed to one atom at a time

import Atom as Atom
import Potential as Potential
import math


#################################################################################
## Function to compute total/net forces on a all atoms due to all neighboors ##
#################################################################################
def Calc_Forces(List_Atoms,Potential_LJ):
# Input 1 : List of all atoms
# Input 2: LJ potential object

    #########################################################
    # Loop over all atoms:
    for j in range(0,len(List_Atoms)):
        # Get atom position
        x0 = List_Atoms[j].Position[0]
        y0 = List_Atoms[j].Position[1]
        z0 = List_Atoms[j].Position[2]

        # Get neighbour list
        neighbours = List_Atoms[j].neighboor

        # Initialize forces
        Fx = 0.0
        Fy = 0.0
        Fz = 0.0

        #####################################################
        # Loop over neighborlist to sum forces
        for i in range(0,len(neighbours)):

            # Get position of i-th neighbour
            x1 = neighbours[i].Position[0]
            y1 = neighbours[i].Position[1]
            z1 = neighbours[i].Position[2]

            # Calculate spacing between atom and neighbor
            del_x = x1 - x0
            del_y = y1 - y0
            del_z = z1 - z0

            # Sum forces for all neighbours
            Fx = Fx + Potential_LJ.Force_Calculation(del_x)
            Fy = Fy + Potential_LJ.Force_Calculation(del_y)
            Fz = Fz + Potential_LJ.Force_Calculation(del_z)
        #End neighbour loop
        ########################################################

        F_new = [Fx, Fy, Fz] # Make list of new forces on atom
        List_Atoms[j].Update_Force(F_new) # Update atom with new forces
    # End atom list loop
    ############################################################
    return 0 # End function



#####################################################################
## Function to advance position and velocity using velocity Verlet ##
#####################################################################
def Verlet_Stepper(del_t,List_Atoms,mass,Potential_LJ):
# Input 1: time step
# Input 2: List containing all atoms in system
# Input 3: atom mass
# Input 4: LJ potential object

    ###########################################################
    # Advance position of all atoms:
    for i in range(0,len(List_Atoms)):
        # Current atom position
        x_old = List_Atoms[i].Position[0]
        y_old = List_Atoms[i].Position[1]
        z_old = List_Atoms[i].Position[2]

        # Current atome velocities (V = P/m)
        Vx_old = List_Atoms[i].Momentum[0]/mass
        Vy_old = List_Atoms[i].Momentum[1]/mass
        Vz_old = List_Atoms[i].Momentum[2]/mass

        # Current atom accelerations (a = F/m)
        Ax_old = List_Atoms[i].Force[0]/mass
        Ay_old = List_Atoms[i].Force[1]/mass
        Az_old = List_Atoms[i].Force[2]/mass

        # New atom position using Verlet
        x_new = x_old + del_t*Vx_old + del_t*del_t*Ax_old/2.0
        y_new = y_old + del_t*Vy_old + del_t*del_t*Ay_old/2.0
        z_new = z_old + del_t*Vz_old + del_t*del_t*Az_old/2.0

        # Update atom position
        R_new = [x_new, y_new, z_new]
        List_Atoms[i].Update_Position(R_new)
    # End loop over all atoms
    ############################################################

    # Recompute forces on all atoms
    Calc_Forces(List_Atoms,Potential_LJ)

    ############################################################
    # Advance velocities/momenta of all atoms:
    for j in range(0,len(List_Atoms)):
        # New acceleration computed from updated force
        Ax_new = List_Atoms[j].Force[0]/mass
        Ay_new = List_Atoms[j].Force[1]/mass
        Az_new = List_Atoms[j].Force[2]/mass

        # New atom velocities using Verlet
        Vx_new = Vx_old + (Ax_old + Ax_new)*del_t/2.0
        Vy_new = Vy_old + (Ay_old + Ay_new)*del_t/2.0
        Vz_new = Vz_old + (Az_old + Az_new)*del_t/2.0

        # New atom momentum (P = mV)
        Px_new = Vx_new*mass
        Py_new = Vy_new*mass
        Pz_new = Vz_new*mass

        P_new = [Px_new, Py_new, Pz_new] # List of new momentum
        List_Atoms[j].Update_Momentum(P_new) # Update atom momentum
    # End loop over all atoms
    ###############################################################

    return 0 # End function





