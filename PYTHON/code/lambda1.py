# lambda function or anonymous function
# def minus(x,y):
#     return x-y


minus=lambda x,y:x-y    #lambda function
# print(minus(9,4))
def list_first(list):
    return list[0]
list=[[1,14],[51,6],[7,18]]
list.sort(key=list_first)
print(list)


# in lambda function
list=[[1,14,2],[51,6,23],[7,18,5],[12,45,19],[4,11,13]]
# list.sort(key=lambda x:x[2]) #[[1, 14, 2], [7, 18, 5], [4, 11, 13], [12, 45, 19], [51, 6, 23]]
# list.sort(key=lambda x:x[0])   #[[1, 14, 2], [4, 11, 13], [7, 18, 5], [12, 45, 19], [51, 6, 23]]
# list.sort(key=lambda x:x[1])    #[[51, 6, 23], [4, 11, 13], [1, 14, 2], [7, 18, 5], [12, 45, 19]]
# def x(xk):
#     return xk[0]
xx=lambda a,b:a*b
yy=xx(2,4)
# print(yy)