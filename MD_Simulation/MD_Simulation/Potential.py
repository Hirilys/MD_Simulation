class Potential(object):
    """description of class"""
    """Create a Lennard-Jones potential with the specified parameters"""

    def __init__(self,eps, Sig, m , n , InterAtomic):
        self.eps = 1
        self.k = n/(n-m)*(n/m)**(m/(n-m))
        self.m = 6
        self.n = 12
        self.Sig = Sig
        self.Rc = 2.5*InterAtomic

    def PotentialCalculation(self, Radius):
        if abs(Radius) <= abs(self.Rc):
            return self.k*self.eps*(((self.Sig/Radius)**self.n)-((self.Sig/Radius)**self.m))
        else:
            return 0


    def Force_Calculation(self,Radius):

        if abs(Radius) < abs(self.Rc):
            return  self.k*self.eps*(self.m*(self.Sig/Radius)**self.m - self.n*(self.Sig/Radius)**self.n)/Radius + self.Force_Calculation(self.Rc)
        if abs(Radius-self.Rc)/abs(self.Rc)<=0.001:
            return self.k*self.eps*(self.m*(self.Sig/Radius)**self.m - self.n*(self.Sig/Radius)**self.n)/Radius
        else:
            return 0
        



