# --------------------map-------------------------
from cmath import sqrt

from numpy import less


numbers=["12","34","65","89"]

# numbers[2]=numbers[2]+1   #error for string and int can not cancartinate

# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])

#or without for we change the type
numbers=list(map(int,numbers))

numbers[2]=numbers[2]+5
# print(numbers[2])

def sqr(a):
    return a*a
num=[1,2,3,4,5,6]
square=list(map(sqr,num))
# print(square)

ad_2=list(map(lambda x:x+2,num))
# print(ad_2)

# or
'''num=[1,2,3,4,5,6]
square=list(map(lambda x:x*x,num))  #lambda function
print(square)'''

def square(a):
    return a*a
def cube(a):
    return a*a*a

func=(square,cube)
num=[1,2,3,4,5,6]
# for i in range(len(num)):
#     val=list(map(lambda x:x(i),func))
    # print(val)


# ----------------filter------------------
list_1=[1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_thn_5=list(filter(is_greater_5,list_1))
# print(gr_thn_5)

def less_thn_5(n):
    return n<5
l5=list(filter(less_thn_5,list_1))
# print(l5)
# ------------------------reduce--------------------------
from functools import reduce

list2=[1,2,3,4]
# num=0
# for i in list2:
#     num=num+i
# print(num)

num=reduce(lambda x,y:x+y,list2)
print(num)

