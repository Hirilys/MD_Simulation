class FunctionToolbox(object):
    """Class that gives a list of function to calculate neighbours and forces"""
import math
from Atom import *


def __init__(self):
    pass

def Compute_Radius(Atom1, Atom2):
    Radius = math.sqrt((Atom1.Position[0]-Atom2.Position[0])**2+(Atom1.Position[1]-Atom2.Position[1])**2+(Atom1.Position[1]-Atom2.Position[1])**2)
    return Radius

def Compute_Neighbours(List_Atoms, Rc):
     for i in range(0,len(List_Atoms)):
        List_Tmp = List_Atoms[:]
        List_Tmp.remove(List_Atoms[i])
        List_neighbours = list()
        List_RadiusNeighbours = list()
        Atom_ref = List_Atoms[i]
        for j in range(0,len(List_Tmp)):
            Radius = Compute_Radius(Atom_ref,List_Tmp[j])
            if Radius <= Rc:
                    List_neighbours.append(List_Tmp[j])
                    List_RadiusNeighbours.append(Radius)
        Atom_ref.Update_Neighbours(List_neighbours) 
        Atom_ref.Update_RadiusNeighbours(List_RadiusNeighbours)


#################################################################################
## Function to compute total/net forces on a all atoms due to all neighboors ##
#################################################################################
def Force_Projection(Atom1, Atom2 , Force):
    #Vector to project force on the (x,y,z) base
    Vector = [Atom1.Position[0]-Atom2.Position[0], Atom1.Position[1]-Atom2.Position[1], Atom1.Position[2]-Atom2.Position[2]]
    Norm_Vector = math.sqrt(Vector[0]**2+Vector[1]**2+Vector[2]**2)

    return [Force*Vector[0]/Norm_Vector, Force*Vector[1]/Norm_Vector,Force*Vector[2]/Norm_Vector]


def Calc_Forces(List_Atoms,Potential_LJ):
# Input 1 : List of all atoms
# Input 2: LJ potential object

    #########################################################
    # Loop over all atoms:
    for i in range(0,len(List_Atoms)):
        Force = [0,0,0]        
        #Loop over evevry radius
        for j in range(0,len(List_Atoms[i].Radius_Neighbour)):
            Force3D = Force_Projection(List_Atoms[i],List_Atoms[i].neighbour[j],Force_Calculation(List_Atoms[i].Radius_Neighbour[j]))
            #Force= [Force_x, Force_y, Force_z]
            Force[0]+=Force3D[0]
            Force[1]+=Force3D[1]
            Force[2]+=Force3D[2]
        
        #End neighbour loop
        ########################################################
        List_Atoms[i].Update_Force(Force)
    # End atom list loop
    ############################################################   