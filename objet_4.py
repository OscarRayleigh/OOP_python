class Somn(object):
    def __init__(self,n):
        self.n = n
        self.list = []
        for i in range(self.n):
            self.list.append(0)
    def getn(self):
        return self.n
    def get(self):
        return self.list
    def geti(self,i):
        return self.list[i]
    def setn(self,n):
        self.n = n
    def set(self, *elements):
        self.list = []
        for i in elements:
            self.list.append(i)
        return self.list

    def seti(self,i,val):
        val = int(input("Nouvelle valeur pour composante {} : ".format(i)))
        self.list[i] = val
        return self.list
    def impl(self,n):
        for i in range(n):
            new_val = []
            new_val = int(input("Nouvelle valeur : "))
            self.n += 1
            self.list.append(new_val)
    def val(self):
        sum = 0
        for i in range(self.n):
            sum += self.list[i]
            print("sum = ", sum)
        return sum
    def opp(self):
        return -x.val()
    def inv(self):
        return x.val()**(-1)
    def somPuisn(self,n):
        somme = 0
        for i in self.list:
            somme += i**n
        return somme
    def affich(self,n):
        if x.val() > 0:
            print("Signe de la somme : +")
        if x.val() < 0:
            print("Signe de la somme : -")
        if x.val() == 0:
            print("Signe de la somme : =0")
        print("Valeur de la somme : ",x.val())
        print("Opposé de la somme : ",x.opp())
        print("Inverse de la somme : ",x.inv())
        print("Somme des puissances ({}°): ".format(n),x.somPuisn(n))

class Prodn(Somn):
    def val(self):
        prod = 1
        print(self.list)
        for i in self.list:
            prod*=i
        return prod
    def prodPuisn(self,n):
        prod = 1
        for i in self.list:
            prod*=i**(n)
        return prod

    def affich(self,n):
        if x.val() > 0:
            print("Signe du produit : +")
        if x.val() < 0:
            print("Signe du produit  : -")
        if x.val() == 0:
            print("Signe du produit : =0")
        print("Valeur du produit : ",x.val())
        print("Opposé du produit  : ",-x.val())
        print("Inverse du produit  : ",-x.val())
        print("Produit des puissances ({}°): ".format(n),x.prodPuisn(n))

x = Prodn(0)
x.impl(3)
x.affich(2)
