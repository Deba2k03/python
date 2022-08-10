# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)

# print(ls)

#list comprehension
# ls=[i for i in range(100) if i%3==0]
# print(ls)

#dictionary comprehension
# dict=(0:"item0",1:"item1",2:"item2".......)
#using comprehension
dict1={i:f"item{i}" for i in range(10)}

dict2={value:key for key,value in dict1.items()}
# print(dict1)
# print(dict2)
# print(dict1,"\n",dict2)

#set comprehension
# dresses={dress for dress in {"dress1","dress2","dress1","dress2"}}
a={"dress1","dress2","dress1","dress2"}
dresses={dress for dress in a}

print(dresses)
# print(type(dresses)) #object interspection


#generator comprehension
evens=(i for i in range(10) if i%2==0)
# print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

#or
# for i in evens:
#     print(i)


a=[]
b=int(input("how many element you input:"))
for i in range(b):
    i=input("enter elemnt:")
    a.append(i)

print(a)
x={i for i in a}
print(x)
y=(i for i in a)
print(y.__next__())
print(y.__next__())
c={i:f"item{i}" for i in a}
print(c)

