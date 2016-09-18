class Atom(object):
    """description of class"""
    """ Class atom that stocks position, velocity and neighboors of the atom """

    def __init__(self,ID,Position): #Constructor of the class
        self.ID = ID
        self.Position = Position
        self.Momentum = [0,0,0]
        self.neighbour = list()
        self.Radius_Neighbour = list()
        self.Old_Position = Position
        self.Old_Momentum = [0,0,0] #Allows to keep track of momentum in the previous step
        self.Force = list()

    def Update_Neighbours(self,Liste_Neighbours): #Erase old list and save new one in the variable
        self.neighbour = Liste_Neighbours

    def Update_RadiusNeighbours(self,Liste_RadiusNeighbours): #Erase old list and save new one in the variable
        self.Radius_Neighbour = Liste_RadiusNeighbours


    def Update_Force(self, Force):#Erase olf orce to save the new one in the variable
        self.Force = Force

    def Update_Position(self, Position): 
        self.Old_Position = self.Position
        self.Position = Position

    def Update_Momentum(self, Momentum):
        self.Old_Momentum = self.Momentum
        self.Momentum = Momentum

        





