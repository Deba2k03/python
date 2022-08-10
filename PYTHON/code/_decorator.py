# def function1():
#     print("hello")
# func2=function1
# del function1 #delete function1
# func2()

# def func(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=func(0)
# print(a)

# def exicution(func):
#     func("this")
# exicution(print)

'''def dec1(func1):
    def execute1():
        print("executing now")
        func1()
        print("function executed")
    return execute1
@dec1  #hello=dec1(hello)  #decorator function
def hello():
    print("hello sir")

# hello=dec1(hello)
hello()
'''
def division(func):
    def divi(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return divi
@division
def div(a,b):
    print(a/b)

div(4,4)
        


'''def sum(fuc):
    def dd(x):
        x += 40
        return fuc(x)
    return dd


@sum
def ss(a):
    print(a)


ss(3)
'''