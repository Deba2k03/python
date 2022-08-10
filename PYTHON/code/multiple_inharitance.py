class Student:
    id=1
    vari=10
    def __init__(self,name,roll_no,std,age):
        self.name=name
        self.roll_no=roll_no
        self.std=std
        self.age=age
        
    def print_details(self):
        print(f"\nyour name {self.name}\n your roll_no is {self.roll_no}\n your std is {self.std}\n your age is {self.age}")

class Player:
    vari=9
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def print_detail(self):
        print(f"name is {self.name} game is {self.game}")

subham=Player("subham",["cricket"])

class  Cool_Programmer(Student,Player):
    # vari=8 
    language="c++"
    def print_language(self):
        print(self.language)

karan=Cool_Programmer("Deb",32,12,43) #when an object is created than first search the constructor in Student class than olayer class and than Cool_programmer class
# karan.print_language()
print(karan.vari)