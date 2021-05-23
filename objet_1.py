class Cercle(object):

    def __init__(self,x):
        self.x = x
    def setr(self,x):
        self.x = x
    def per(self):
        return 2*3.14*self.x
    def diam(self):
        return self.x*2
    def comper(self,y):
        return ("La différence des périmètres vaut : ",abs(2*3.14*self.x - 2*3.14*y))
    def compsurf(self,y):
        return ("La différence des surfaces vaut : ",abs(3.14*(self.x**2) - 3.14*(y**2)))
    def compdiam(self,y):
        return ("La différence des diamètres vaut : ",abs((self.x*2)-(y*2)))
    def compare(self,y):
        if self.x == y:
            return True
        if self.x!= y:
            return False



class Rectangle(object):
    def __init__(self, lo, la):
        self.lo = lo
        self.la = la
    def setlo(self,lo):
        self.lo = lo
    def setla(self,la):
        self.la = la
    def per(self):
        return 2*self.lo + 2*self.la
    def surf(self,lo,la):
        return self.lo*self.la
    def diag(self):
        return (self.lo**2 + self.la**2)*(1/2)
    def comper(self,yla,ylo):
        return ((2*self.lo + 2*self.la)-(2*yla + 2*ylo))
    def compsurf(self,yla,ylo):
        return ((self.lo*self.la)-(yla*ylo))
    def compdiag(self,yla,ylo):
        return (self.lo**2 + self.la**2)*(1/2) -(ylo**2 + yla**2)*(1/2)
    def compare(self,yla,ylo):
        if self.lo == ylo && self.la == yla:
            return True
        else:
            return False
            
rec = Rectangle(3,4)
print(rec.compdiag(3,8))



# cercle1 = Cercle(5)
# print(cercle1.per())
# print(cercle1.diam())
# print(cercle1.comper(8))
# print(cercle1.compsurf(8))
# print(cercle1.compdiam(8))
# print(cercle1.compare(8))
