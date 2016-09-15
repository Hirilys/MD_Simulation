class Potential(object):
    """description of class"""
    """Create a Lennard-Jones potential with the specified parameters"""

    def __init__(self,eps, k , Sig, m , n):
        self.eps = 1
        self.k = 4
        self.m = 8
        self.n = 12
        self.Sig = Sig

    def PotentialCalculation(self, Radius):
        if abs((Radius-2.5*self.Sig)/self.Sig) <= 0.001:
            return 4*self.eps*(((self.Sig/Radius)^self.n)-((self.Sig/Radius)^self.m))
        else:
            return 0


    def Force_Calculation(self, radius):



