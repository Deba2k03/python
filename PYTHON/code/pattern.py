n=int(input("Enter n:"))
k=1
for i in range(1,n):
        for j in range(2*n):
                if i is j or i+j==2*n:
                        print(k,end='')
                else:
                        print(" ",end='')
        print()
        k+=1
for i in range(n,0,-1):
        for j in range(2*n,0,-1):
                if i is j or i+j==2*n:
                        print(k,end='')
                else:
                        print(" ",end='')
        k-=1
        print()