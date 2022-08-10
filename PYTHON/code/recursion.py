'''def print2(str1):
    print("this is"+str1)
print2("deb")
'''

'''def factorial_iterative(n):
    #   n!=n*n-1*n-2.....1
    fact=1
    for i in range(n):
        fact=fact*(i+1)
    return fact
number=int(input("Enter a no:"))
print("factorial using iterative method:",factorial_iterative(number))'''
'''
def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
# 5*factorial_recursive(4)
# 5*4*factorial_recursive(3)
# 5*4*3*factorial_recursive(2)
# 5*4*3*2*1
number=int(input("Enter a number:"))
print("factorial  recursive",factorial_recursive(number))'''

# 0 1 1 2 3 5 8 13


def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-1)+fibonaci(n-2)


n = int(input("Enter the number:"))
print("factorial:", fibonaci(n))
