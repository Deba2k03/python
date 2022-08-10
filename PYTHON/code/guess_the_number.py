while True:
    n=17
    i=1 
    while True:
        a=int(input("\nguess the number between 1 to 20:"))    
        if n==a:
            print("\n*****you win*****\n")
            print("\nyou take ",i,"chance for win\n")
            break
        elif i==5:
                print("\n***game over***\n")
                break
        elif n>a:
            print("\ntoo low\n")
            print("guesses left:",5-i)
        elif n<a:
            print("\ntoo big\n")
            print("guesses left:",5-i)
        i=i+1
    print("\n ***want to play again***\n")
    print("1.yes")
    print("2.NO")
    s=int(input())
    if s==1:
        continue
    else:
        break  
print("\n******thanks for playing*****\n")
