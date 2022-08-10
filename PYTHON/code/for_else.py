# student=["deb","rutu","rahul","sonali"]
# for item in student:
#     print(item)
# else:
#     print("this loop ended properly")


student=["deb","rutu","rahul","sonali"]
for item in student:
    print(item)
    # break
else:
    print("this loop ended properly")

for item in student:
    if item=="deb":
        break
    
else:
    print("your student is not found")