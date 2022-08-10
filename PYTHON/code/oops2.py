
class Student:
    id=1
    def __init__(self,name,roll_no,std,age):
        self.name=name
        self.roll_no=roll_no
        self.std=std
        self.age=age
    @classmethod
    def class_(cls,i):
        cls.id=i

    @classmethod
    def class_2(cls,strg):
        rahul=strg.split(",")
        return cls(rahul[0],rahul[1],rahul[2],rahul[3])

    def print_details(self):
        print(f"\nyour name {self.name}\n your roll_no is {self.roll_no}\n your std is {self.std}\n your age is {self.age}")
    
    @staticmethod
    def name_(stn):
        print("my self  "+stn)

# rahul=Student("rahul",32,12,23)
# rahul.class_(3)
# print(rahul.id)
rahul=Student.class_2("rahul,21,12,33")
# rahul.print_details()
rahul.name_("deb")

class inharit(Student):
    pass