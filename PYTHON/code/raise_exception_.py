
# a=input("What is your name:")
# # if a.isnumeric():
# #     raise Exception("numbers are not allowed")

# # print(f"hello {a}")

# b=input("how much do you earn:")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")

#write abput two build in exception
c=input("Enter your name:")

try:
    print(x)
except Exception as e:
    if c=="deb":
        raise ValueError("deb is blocked he is not allowed")
    print("Exception handle",e)



