class FunctionToolbox(object):
    """Class that gives a list of function to calculate neighbours"""
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

        Atom_ref = List_Atoms[i]
        for j in range(0,len(List_Tmp)):
            if Compute_Radius(Atom_ref,List_Tmp[j]) <= Rc:
                    List_neighboors.append(List_Tmp[j])
        Atom_ref.Update_Neighbours(List_neighboors) 
