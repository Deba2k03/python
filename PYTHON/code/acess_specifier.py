#public
#protected 
#private
class X:
    v=1 #public
    _s=23 #protected  use in base class
    __p=45 #private  save in _X__p

a=X()
# print(a._s)
# print(a._X__p)   #_calss__private variable

class Employee:
    var1=45
    _var2=23
    __var3=67

a=Employee()
print(a._Employee__var3)