class Initialization(object):
    """description of class"""
import math
from Atom import Atom

def __init__(self, Type_Lattice, InterAtomic, Boxsize): #Box size is a vector containing [ax,ay,az] which corresponds to the number of atoms along each axis
    Vinit= [0,0,0]  
    List_Atoms = list()
    if Type_Lattice=='BCC':
        
        for x in range(0,Boxsize[0]-1):
            for y in range(1, Boxsize[1]-1):
                for z in range(1,Boxsize[2]-1):
                    i=0
                    if x<Boxsize[0]-1:
                        List_Atoms.append(Atom(x,[0,0,x]))
                    


    if Type_Lattice=='FCC':
        a=1
    if Type_Lattice=='CC':
        a=1

