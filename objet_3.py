class Vecteurn(object):
    def __init__(self, n):
        self.list = []
        self.n = n
        for i in range(n):
            self.list.append(0)
    def getn(self):
        return self.n
    def getvec(self):
        return self.list
    def geti(self,i):
        return self.list[i]
    def setn(self):
        self.n = n
    def setvec(self, *composantes):
        self.list = []
        self.n = len(composantes)
        for i in composantes:
            self.list.append(i)
        return self.list,self.n
    def seti(self, i, val):
        self.list[i] = val
        return self.list
    def impl(self):
        self.list = []
        print("Dimension ", self.n)
        for i in range(self.n):
            print("Entrer valeur vecteur pour composante ", i)
            val = input()
            self.list.append(val)
        return self.list
    def opp(self):
        for i in range(self.n):
            self.list[i] = -int(self.list[i])
        vecteur = Vecteurn(self.n)
        vecteur.setvec(self.list)
        return vecteur
    def norm(self):
        temp = self.list.copy()
        sum = 0
        for i in range(len(temp)):
            temp[i] = int(temp[i])**2
        for i in temp:
            sum += i

        return sum**(1/2)
    def vu(self):
        uni = []
        for i in range(self.n):
            uni.append(int(self.list[i])/x.norm())
        return uni
    def som(self):
        somme = 0
        for i in self.list:
            somme += int(i)
        return somme







x = Vecteurn(3)
x.impl()
print(x.som())
