from Atom import Atom
from numpy import *
import math
import structure_v2 as StructureV2


lattice = array([0,1,0,1,0,1])
structure = "sc"
a = 5

List_Atoms = list()
List_Atoms = StructureV2.StructureInitialize(lattice,structure,a)

# Output atom positions as to verify correctness:
for i in range(0,len(List_Atoms)):
    print(List_Atoms[i].Position)