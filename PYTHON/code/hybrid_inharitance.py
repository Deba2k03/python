class A:
    def met(self):
        print("this is a method from cls A")
class B(A):
    def met(self):
        print("this is a method from cls B") 
class C(A):
    def met(self):
        print("this is a method from cls C")
class D(B,C):              #if method is not present in D class than object first check to B class than check to C class
    # def met(self):
    #     print("this is a method from cls D")
    pass
    


a=A()
b=B()
c=C()
d=D()

d.met()