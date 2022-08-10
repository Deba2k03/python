'''l=10 #global variable
def func(n):
    # l=5  #local variable
    m=8
    global l   #global keyword use to change global variable
    l=l+3
    print(l,m)
    print(n)
func("i m in func")
print(l)'''
 
def deb():
    x=10
    def sahu():
        global x    #if  global variable is not place than creat a global variable
        x=45        
    print("before calling sahu",x)
    sahu()
    print("after calling deb",x)
deb()
print(x)
