print("\n***welcome***\n")
while True:
    print("\nEnter your name:\n")
    print("\n1.Debashish\n")
    print("\n2.Ruturaj\n")
    print("\n3.Rahul\n")
    n=int(input())
    if n==1:
        print("\npress \n1.retrive\n2.log\n")
        a=int(input())
        if a==2:
            print("\n1.food\n2.exercise\n")
            b=int(input())
            if b==1:
                f=open("rohanf.txt","a")
                c=input("\nwhat you eat today:\n")
                f.write(c)
                print("\nwritten successful\n")
                f.close()
            elif b==2:
                f=open("rohane.txt","a")
                c=input("\nwhich exercise you do:\n")
                f.write(c)
                print("\nwritten successful\n")
                f.close()
        elif a==1:
            print("1.food\n2.exercise\n")
            b=int(input())
            if b==1:
                f=open("rohanf.txt")
                q=f.read()
                print("\n",q)
                f.close()
            elif b==2:
                f=open("rohane.txt","a")
                print("\n",f.read())
                f.close()
    elif n==2:
        print("\npress \n1.retrive\n2.log\n")
        a=int(input())
        if a==2:
            print("\n1.food\n2.exercise\n")
            b=int(input())
            if b==1:
                f=open("rajeshf.txt","a")
                c=input("\nwhat you eat today:\n")
                f.write(c)
                print("\nwritten successful\n")
                f.close()
            elif b==2:
                f=open("rajeshe.txt","a")
                c=input("\nwhich exercise you do:\n")
                f.write(c)
                print("\nwritten successful\n")
                f.close()
        elif a==1:
            print("1.food\n2.exercise\n")
            b=int(input())
            if b==1:
                f=open("rajeshf.txt")
                q=f.read()
                print("\n",q)
                f.close()
            elif b==2:
                f=open("rajeshe.txt","a")
                print("n",f.read())
                f.close()
    elif n==3:
        print("\npress \n1.retrive\n2.log\n")
        a=int(input())
        if a==2:
            print("\n1.food\n2.exercise\n")
            b=int(input())
            if b==1:
                f=open("ramaf.txt","a")
                c=input("\nwhat you eat today:\n")
                f.write(c)
                print("\nwritten successful\n")
                f.close()
            elif b==2:
                f=open("ramae.txt","a")
                c=input("\nwhich exercise you do:\n")
                f.write(c)
                print("\nwritten successful\n")
                f.close()
        elif a==1:
            print("1.food\n2.exercise\n")
            b=int(input())
            if b==1:
                f=open("ramaf.txt")
                q=f.read()
                print("\n",q)
                f.close()
            elif b==2:
                f=open("ramae.txt","a")
                print("\n",f.read())
                f.close()
    

