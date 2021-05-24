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
        return (sum_inf*2)**2
    def amax(self):
        la_rec = self.b/self.n
        sum_sup = 0
        for i in range(0,self.n):
            # -1 car la fonction est décroissante
            sum_sup += func(la_rec * (i-1))*(la_rec)
        return (sum_sup*2)**2
    def amil(self):
        return (x.amin()+x.amax())/2

    def affich(self):
        print("Aire inférieur : ", x.amin())
        print("Erreur relative (%): ", (abs(x.amin()/math.pi)*100)-100)
        print("Aire supérieur : ", x.amax())
        print("Erreur relative (%): ", (abs(x.amax()/math.pi)*100)-100)
        print("Aire moyen : ", x.amil())
        print("Erreur relative (%): ", (abs(x.amil()/math.pi)*100)-100)

    def affichmin(self):
        print("Aire inférieur : ", x.amin())
        print("Erreur relative (%): ", (abs(x.amin()/math.pi)*100)-100)
    def affichmax(self):
        print("Aire supérieur : ", x.amax())
        print("Erreur relative (%): ", (abs(x.amax()/math.pi)*100)-100)
    def affichmil(self):
        print("// Méthode des rectangles // ")
        print("Aire moyen : ", x.amil())
        print("Erreur relative (%): ", (abs(x.amil()/math.pi)*100)-100)
    def atrapz(self):
        la_rec = self.b/self.n
        sum_trap = 0
        for i in range(0,self.n):
            sum_trap += ((((-func(la_rec*(i+1))+func(la_rec*i))*(la_rec)))/2)+ func(la_rec * (i+1))*(la_rec)
        return (sum_trap*2)**2
    def etrapz(self):
        return (1 - x.atrapz()/math.pi) * 100
    def affichtrapz(self):
        print("// Méthode des trapèzes // ")
        print("Estimation de l'aire : ", x.atrapz())
        print("Estimation de l'erreur (%): ", x.etrapz())
x = Pi(2,2)
x.affichmil()
x.affichtrapz()
