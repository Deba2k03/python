'''a=9
b=8
c=sum((a, b))  #build in function
print(c)'''
# user define function
'''def function1():
    print("you are in function")
# print(function1())
function1()
'''
'''def function(a,b):
    print("addition:",a+b)
function(2,4)
'''

def func2(a,b):
    """this is the function which calculate addition""" #doc string  
#     addition=a+b
#     # print(addition)
#     return addition
# v=func2(2,4)
# print(v)
print(func2.__doc__)

def details():
    '''it print a details'''
    pass
print(details.__doc__)