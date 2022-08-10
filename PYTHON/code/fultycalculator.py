a = int(input("Enter your 1st number:"))
c = input("Enter your operation(+,-,*,/):")
b = int(input("Enter your 2nd number:"))
if a == 56 and b == 9 and c == '+':
    print("result:", 77)
elif a == 56 and b == 4 and c == '/':
    print("result:", 4)
elif c == '+':
    print("result:", a+b)
elif c == '-':
    print("result:", a-b)
elif c == '*':
    print("result:", a*b)
elif c == '/':
    print("result:", a/b)
else:
    print("invalid input")
