from turtle import pos


s=set()
'''
# print(type(s))
csc=set([1,2,3,4])
print(csc)
print(type(csc))
# or
l=[2,3,4,5,6]
cd=set(l)
print(cd)'''
s.add(1)
s.add(2)
# s.union({1,2,3})
s1=s.union({1,2,3})
s3=s.union({4})
s4=s.intersection({1,2,3})

# print(s,s1,s3,s4)
# print(len(s))
# print(max(s1))
# print(min(s1))
s5={7,8}
# print(s.isdisjoint(s5))
s5.remove(7)
# print(s5)
s6={3,4,8,5}
# s6.clear()
# print(s6)
# s7=s6.copy()
# print(s7)
s8={1,2,3,4,5,6}
# s9=s8.copy()
# print(s9)
# print(s6.difference(s8))
s9={3,4,5}
# result=s9.difference_update(s8)
# print(result)
# s9.discard(3)
# print(s9 )

# print(s8.pop()) 
