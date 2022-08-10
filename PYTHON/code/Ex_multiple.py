class electronic_gadged:
    no_of_gadjed=5

class pocket_gadjet(electronic_gadged):
    no_of_pkt=2
    
    def _gedjet(self):
        return self.no_of_pkt
class phone(pocket_gadjet):
    no_of_phn=3
    def _gedjet(self):
        return self.no_of_phn

e=electronic_gadged()
p=pocket_gadjet()
pp=phone()
print(pp._gedjet())
print(p._gedjet())
        
