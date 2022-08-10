# from abc import ABCMeta,abstractmethod

# class Shape(metaclass=ABCMeta): #abstract class
#     @abstractmethod
#     def printarea(self):   #after  this method is necessary for all the derived
#         return 0

# class Rectangle(Shape):
#     type="Rectangle"
#     sides=4
#     def __init__(self):
#         self.length=6
#         self.breath=4
#     # def printarea(self):
#     #     pass

# rect=Rectangle()

# or

from abc import ABC,abstractmethod

class Shape(ABC):#abstract class
    @abstractmethod
    def printarea(self):    #after  this method is mendatory for all the derived  class
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breath=4
    def printarea(self):
        return self.length*self.breath

rect=Rectangle()
print(rect.printarea())

#do not create abstract class method
# b=Shape()

