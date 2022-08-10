import inspect


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email=f"{fname}.{lname}@gmail.com"

    # def  email(self):
    #     return f"{self.fname}.{self.lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set,please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, strng):
        names = strng.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


a = Employee("Deb", "student")
b = Employee("rutu", "stu")

# print(a.email())
a.fname = "debashish"
# print(a.email())
# print(a.fname)
# after decoretor
# a.email="deb.sahu@gmail.com"
# print(a.email)
# print(a.lname)

# del a.email
# print(a.email)

# object  introspection
skillf = Employee("skill", "f")
# print(skillf.email)
# print(type(skillf))
# print(type("this is deb"))
# print(id("this is deb"))  #show the id of object
o = "this is string"
# print(dir(0))
# print(dir(skillf))  #function that are access
# print(id(o))

print(inspect.getmembers(skillf))
