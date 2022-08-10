# classes-template
# object-instace of the class

'''class student:
    pass
deba=student()
shish=student()

deba.name="Debashish"
deba.std=12
deba.roll_no=21
shish.std=6
shish.subject=("python","c++","c")
# print(deba.std)
print(deba,shish)'''

class Employee:
    no_leaves=8
    pass
    
rutu=Employee()
deb=Employee()
rutu.name="ruturaj"
rutu.salary=45000
rutu.role="student"
deb.name="debashish"
deb.salary=340000
deb.role="student"
deb.no_leaves=9  #it do not change the class variable it creates a instance variable
print(deb.__dict__)
# print(Employee.__dict__)
# print(rutu.no_leaves)
Employee.no_leaves=9  #it change the class variable
# print(Employee.no_leaves)
# oops2
class Employee:
    no_leaves=8
    def print_details(self):
        return f"The name is {self.name},salary is {self.salary} and role is {self.role}"
    
rutu=Employee()
deb=Employee()
rutu.name="ruturaj"
rutu.salary=45000
rutu.role="student"
deb.name="debashish"
deb.salary=340000
deb.role="student"

# print(deb.print_details())
print(rutu.print_details())

# constructor
class Employee:
    no_leaves=8

    def __init__(self,aname,asalary,arole):
          self.name=aname
          self.salary=asalary
          self.role=arole
    def print_details(self):
        return f"The name is {self.name},salary is {self.salary} and role is {self.role}"
     
#class method
    @classmethod        #by use of classmethod we change the class variable  #decorator
    def change_leaves(cls,new_leaves):  #cls=Employee
        cls.no_leaves=new_leaves

#class method as alternative constructor
    @classmethod
    def from_dash(cls,string):
        # shiba=string.split("-") #shiba is list #split function make a list
        # print(shiba)
        # return cls(shiba[0],shiba[1],shiba[2])

        #or
        return cls(*string.split("-"))
     
#static method
    @staticmethod
    def print_gd(string):
        print("this is good "+string)
        # return 111


#inharitance
class programmer(Employee):
    no_holiday=67
    def print_program(self):
        return f"programmers name is {self.name},salary is {self.salary} and role is {self.role},the languages are {self.language}"

    def __init__(self, aname, asalary, arole,alanguage):
        # super().__init__(aname, asalary, arole)
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=alanguage
rutu=Employee("ruturaj",4500,"student")
deb=Employee("Debashish",45360,"student")
sonali=Employee.from_dash("sonali-43000-student")

rahul=programmer("Rahul",54000,"student","python")
siddhant=programmer("siddhant",23000,"student",["java","c","python"])
# print(rutu.print_details())
# print(rutu.name)

# rutu.change_leaves(34)
# print(rutu.no_leaves)

# print(sonali.name)

# print(deb.print_gd("debashish"))

# print(rahul.print_program())
# print(rahul.no_holiday)
# print(rahul.print_gd("agrawal"))

