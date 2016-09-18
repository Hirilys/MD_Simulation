from Atom import Atom
from Potential import Potential
import FunctionToolbox
import math

Atom1 = Atom(0,[0,0,0])
Atom2 = Atom(1,[2,0,0])
radius1 = FunctionToolbox.Compute_Radius(Atom1,Atom2)

Liste_Atom=[Atom1,Atom2]
FunctionToolbox.Compute_Neighbours(Liste_Atom, 2.5)



Potential_LJ = Potential(1.0,0.8,6,12,1)  
u1 = Potential_LJ.PotentialCalculation(1.2)
f1 = Potential_LJ.Force_Calculation(1.2)

List_Atoms = list()
for x in range(0,10):
    List_Atoms.append(Atom(x,[0,0,x]))



