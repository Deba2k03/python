class Dad:
    m=1
    
class Son(Dad):
    # m=3
    dance=1
    def isdance(self):
        return f"yes i dance {self.dance}no. of times"
class GrandSon(Son):
    dance=6
    def isdance(self):     #method overloading
        return f"yes i dance very well {self.dance}no. of times"
da=Dad()
so=Son()
grs=GrandSon()

# print(grs.isdance())
print(grs.m)  #first check in GrandSon class than check in Son class and than check iin Dad class oposite to the multiple inharitance