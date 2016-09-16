from Atom import Atom
from Potential import Potential
import math

Potential_LJ = Potential(1.0,0.8,6,12,1)  
u1 = Potential_LJ.PotentialCalculation(1.2)
f1 = Potential_LJ.Force_Calculation(1.2)

List_Atoms = list()
for x in range(0,10):
    List_Atoms.append(Atom(x,[0,0,x]))

