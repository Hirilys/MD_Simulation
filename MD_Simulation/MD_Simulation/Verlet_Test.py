from Atom import Atom
from Potential import Potential
import Verlet as Verlet

#### VERLET TEST CODE

Potential_LJ = Potential(1.0,0.8,6.0,12.0,1.0) #Specify Potential
Atom0 = Atom(0,[0.0,1.2,3.4]) # Create 1st atom
Atom1 = Atom(1,[1.6,1.8,3.0]) # Create 2nd atom

## Test force function:
Atom0.neighboor.append(Atom1) # Make 2nd atom a neighbor of 1st atom
Verlet.Calc_Forces(Atom0,Potential_LJ) # Calculate forces on 1st atom
print(Atom0.Force) # Output new force on 1st atom

## Compute forces on atom manually to validate force function:
del_x = Atom1.Position[0] - Atom0.Position[0]
del_y = Atom1.Position[1] - Atom0.Position[1]
del_z = Atom1.Position[2] - Atom0.Position[2]

Fx = Potential_LJ.Force_Calculation(del_x)
Fy = Potential_LJ.Force_Calculation(del_y)
Fz = Potential_LJ.Force_Calculation(del_z)

print([Fx,Fy,Fz]) # Output manually calculated force for comparison w/ above

## Test Verlet algorithm:
Verlet.Verlet_Stepper(0.001,Atom0,1.0,Potential_LJ) # Advance 1st atom position & velocity
print(Atom0.Force) # Ouput new force
print(Atom0.Position) # Output new position