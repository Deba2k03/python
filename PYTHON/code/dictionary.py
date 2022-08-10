#dictionary is nothing but key value pairs



d1=()
#print(type(d1))
d2={"deb":"cs","netra":"math","pratap":"botany","ruturaj":{"m":"mth","p":"phy","c":"cs"}}
# print(d2["deb"])
d2["ankit"]="zoology"
d2["harry"]="it"
# print(d2["ruturaj"]["p"])
# print(d2)
del d2["harry"]
# print(d2)

# print(d2.copy())
# d3=d2.copy()
# print(d3)
'''if we use d3=d2 and we change in d3 than d2 also change'''
# print(d2.get("deb"))
# print(d2.update({"tikeswer":"botany"}))
# print(d2)
# print(d2.keys())
# print(d2.values())
# print(d2.items())
d3={"ruturaj","Debashish","pratap"}
# x="*".join(d3)
x="-".join(d3)
# print(x)


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

# print(x)
# print("-".join(d3))       #ruturaj-Debashish-pratap
myDict = {"name": "John", "country": "Norway","deb":" "}
mySeparator = "TEST"

x = mySeparator.join(myDict)   # x=mySeparator.join(myDict.keys())
# x=mySeparator.join(myDict.values())


# print(x)
y="*student*"
# print(y.join(d3))     #ruturaj*student*Debashish*student*pratap

txt = "welcome to the jungle"

x = txt.split()

# print(x)

# print(txt.format("to","for"))
# print(txt)

# print(myDict.setdefault("deb","gamer"))
# print(myDict) 
# print(myDict.__dict__)

# tx="hey-i-m-back"
# print(tx.split("-"))
myTuple.__dict__