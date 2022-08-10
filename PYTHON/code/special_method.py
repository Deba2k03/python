


class Student:
    id=1
    def __init__(self,name,roll_no,std,age): #dunder method #dunder init #constructor
        self.name=name
        self.roll_no=roll_no
        self.std=std
        self.age=age
    
    def print_details(self):
        print(f"\nyour name {self.name}\n your roll_no is {self.roll_no}\n your std is {self.std}\n your age is {self.age}")
    
    def __add__(self,other): #dunder method
        return self.age+other.age

    def __truediv__(self,other):
        return self.age/other.age

    def __repr__(self):
        # return self.print_details()
        print("in repr")
        return f"Student('{self.name}',{self.roll_no},{self.std},{self.age})"

    # def __str__(self):
    #     print("in str")
    #     return f"Student('{self.name}',{self.roll_no},{self.std},{self.age})"

stu1=Student("Deb",12,8,12)
# stu2=Student("Sahu",15,9,14)
# print(stu1+stu2)
# print(stu1/stu2)
# print(stu1) #if str not present than call repr if str present than call str
#or
print(str(stu1))

#if str present and u call to repr than 
# print(repr(stu1))


#mapping operator to function
#https://docs.python.org/3/library/operator.html#:~:text=Mapping%20Operators%20to%20Functions%20%C2%B6%20%20%20,truediv%20%28a%2C%20b%29%20%2031%20more%20rows%20