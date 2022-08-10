class A:
    clsVariable="i m a class variable in class A"
    def __init__(self):
        self.var1="i m inside class A's constructor"
        self.clsVariable="instance variable in class A"
        self.spacial="special"

class B(A):
    clsVariable="i m in class B"
    def __init__(self):
        # super().__init__()
        self.var1="i m inside class B's constructor"
        self.clsVariable="instannce variable in class B"
        # super().__init__()
        print(super().clsVariable)
        # print(self.clsVariable)


a=A()
b=B()
# print(b.clsVariable)
# print(b.spacial)    
# print(b.spacial,b.clsVariable,b.var1)  
                         