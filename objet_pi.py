import math

def euler():
    global e
    for i in range(1,99999):
        e = (1+ 1/i)**i
    return e

e = euler()

def func(x):
    return e**(-(x**2))

class Pi(object):
    # Avec n intervalles allant jusqu'à b (a=0)
    def __init__(self,b,n):
        self.b = b
        self.n = n
    def getb(self):
        return self.b
    def getn(self):
        return self.n
    def setb(self):
        self.b = b
    def setn(self):
        self.n = n
    def amin(self):
        la_rec = self.b/self.n
        sum_inf = 0
        for i in range(1,self.n):
            sum_inf += func(la_rec * i)*(la_rec)
        return sum_inf
    def amax(self):
        la_rec = self.b/self.n
        sum_sup = 0
        for i in range(1,self.n):
            # -1 car la fonction est décroissante
            sum_sup += func(la_rec * (i-1))*(la_rec)
        return sum_sup
    def amil(self):
        return (x.amin()+x.amax())/2

x = Pi(100,1000)
print(x.amil())
