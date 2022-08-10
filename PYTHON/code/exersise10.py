import requests
import pickle
# data=requests.get("url").text
data='''hello
bro how,
are you'''
l1=data.split("\n")
print(l1)
l2=[item.split(",") for item in l1 if len(item)!=0]
print(l2)

with open("myiris.pkl","wb") as f:
    pickle.dump(l2,f)


# # to read this pikle file you can  use this code
# import pickle
# with open("myiris.pkl","rb") as f:
#     print(pickle.load(f))