# list =("a","b","c","d")
# for item in list:
#     print(item)
from re import I
from traceback import print_tb


list1 = [["a", 1], ["b", 2], ["c", 3]]

list2 = {"s": "a", "d": "v"}
# for item,value in list2.items():
#     print(item,value)
#     print(item,"value is",value)

# for item,value in list1:
#     print(item,value)
#     print(item,"value is",value)

dict1 = dict(list1)
# print(dict1)#dict=dictionary function
# for item,value in dict1.items():
#     print(item,"value is",value)

# for item in list2.items():
#     print(item)

# for item in dict1.keys():   #print the key
#     print(f"key is {item}")

# for item in dict1.values():   #print the values
#     print(f"value is {item}")
'''stu=("ruturaj","debashish",8,65,3,2,7)
for item in stu:
    if str(item).isnumeric() and item>6:
        print(item)'''
# std={"s","a"}
# for item in std:
#  if item.isnumeric():
#     print(item)


# s={2,4,6,}
# for item in s:
#     if str(item).isnumeric():
#         print(item)

# for i in range(6):
#     print(i)

# for i  in range(1,5,+1):  #i=1;i<5;i+=1
#     print(i)

# for j in range(5,0,-1):    #i=5;i>0;i-=1
#     print(j)

# for i in range(3):
#     for j in range(3):
#         print("*",end='  ')
#     print(' ')

for i in range(3):
    for j in range(3):
        if j <= i:
            print("*", end='  ')
        else:
            print("0", end='  ')
    print(' ')
