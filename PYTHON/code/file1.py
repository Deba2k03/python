# import file2
# print(file2.a)

'''
from file2 import a
print(a)
# it is a bad practice'''

# import file2
# file2.printjoke("this is me ")



def printcd(strng):
    return f"my self {strng}"
def adding(s,p):
    return s+p

print("the name is",__name__)
if __name__=='__main__':   #main(): another file not call the code entire the main()
    print(printcd("deba"))
    k=adding(5,6)
    print(k)