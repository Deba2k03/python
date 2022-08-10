n=int(input("enter size of row to draw a pattern:"))
b=bool(input("Enter true or false:"))
if b==1:
    for i in range(0,n+1):
        print("*"*i)   
        print('')   
elif b==0:
    for i in range(n,0,-1):
        print("*"* i)


        
    
