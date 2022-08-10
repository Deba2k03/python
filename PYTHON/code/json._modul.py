# java script object notation
import json
data='{"var1":"deb","var2":56}'
parsed=json.loads(data)
#json.load working in google
# print(data)
print(parsed['var1'])
print(type(parsed)) #dictionary

data2={
    "channel":"deb codong",
    "cars":["rolls royes","bmw"],
    "fridge":("roti",540),
    "isbad":False
}

jscomp=json.dumps(data2)
print(jscomp)

#what is sort_keys parametr in dumps