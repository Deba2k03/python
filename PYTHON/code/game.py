# snake water gun
import random
while True:
    i=0
    j=0
    list=["snake","water","gun"]
    a=random.choice(list)
    print("\n1.snake\n")
    print("2.water\n")
    print("3.gun\n")
    print("\nEnter your choice:")
    b=int(input())
    if a=="snake" and b==2:
        print("\npc  win")
        i+=1
    elif a=="water" and b==1:
        print("\nyou win")
        j+=1
    elif a=="gun" and b==1:
        print("\npc win")
        i+=1
    elif a=="snake" and b==3:
        print("you win")
        j+=1
    elif (a=="snake" and b==1) or (a=="water" and b==2) or (a=="gun" and b==3):
        print("\ntie choices")
    elif a=="water" and b==3 :
        print("\npc win")
        i+=1
    elif a=="gun" and b==2:
        print("\nyou win")
        j+=1
    print("\n***want to play again***\n")
    print("1.yes\n")
    print("2.no\n")
    x=int(input("(1/0):"))
    if x==1:
        continue
    else:
        print("\nyou win",j,"times\n")
        print("pc wins",i,"times\n")
        if i<=j:
            print("\nyou win\n")
            print("***thank you***")
        else:
            print("you lose\n")
            print("***thank you***")
        break
