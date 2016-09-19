from Atom import Atom
from numpy import *
import math

def StructureInitialize(lattice, structure, a):
    ### inputs
    # Declare supercell size/shape - [xmin, xmax, ymin, ymax, zmin, zmax]. Units are in lattice parameter value.
    # lattice = array([xmin, xmax, ymin, ymax, zmin, zmax])
    # Declare structure (fcc, bcc, or sc)
    # structure = "sc"
    # Declare lattice parameter
    # a = 5 # lattice constant (Angstroms)


    ### Create positions

    # Define lattice vectors
    if structure == "fcc":
      a1 = array([0.0, 0.5, 0.5])
      a2 = array([0.5, 0.0, 0.5])
      a3 = array([0.5, 0.5, 0.0])
    if structure == "bcc":
      a1 = array([0.5, 0.5, -0.5])
      a2 = array([0.5, 0.5, 0.5])
      a3 = array([0.5, -0.5, 0.5])
    if structure == "sc":
      a1 = array([1, 0, 0])
      a2 = array([0, 1, 0])
      a3 = array([0, 0, 1])
    a1 = a*a1;
    a2 = a*a2;
    a3 = a*a3;

    xstart = lattice[0]
    ystart = lattice[2]
    zstart = lattice[4]
    xlength = lattice[1]
    ylength = lattice[3]
    zlength = lattice[5]

    np = 8*xlength*ylength*zlength

    print "Number of atoms: " , np

    r_vec = zeros((np,3))
    #print r_vec
    count = 0
    range1 = xlength+xlength
    range2 = ylength+ylength
    range3 = zlength+zlength
    for n1 in range(0,range1):
      for n2 in range (0,range2):
        for n3 in range (0,range3):
          #print n1, n2, n3
          r = n1*a1 + n2*a2 + n3*a3
          x = r[0]
          y = r[1]
          z = r[2]
          #print r
          r_vec[count][:] = r
          count = count + 1

    r0 = r_vec

    List_Atoms = list() # Initialize list of atoms
    for i in range(0,np): # Loop over all atoms
        List_Atoms.append(Atom(i,list(r0[i,:]))) # Generate list of atoms

    return List_Atoms

    #print(List_Atoms[7].Position)
    #savetxt('positions', r0, delimiter=' ')
