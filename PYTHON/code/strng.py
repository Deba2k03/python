#print a maximum line
# print('''hello
# world''')
ab="Debashish sahu"
# print(len(ab))  #length of the string
# print(ab[0:15])
# print(ab[0:7:2])
# print(ab[-4:-2])
# print(ab[10:12])
# print(ab[: :-1])

b="helloworld"
# print(ab.isalnum()) #false

 # print(b.isalnum()) #true with out space

# print(ab.endswith("sahu"))#true
# print(ab.endswith("sa"))#false

# print(ab.count("a"))#count number of a

# print(b.capitalize())#capital the first letter
# n=input("Enter your name:")
# k=n.capitalize()
# print(k)

# print(ab.casefold())#convert in to lower case

c="Deb"
# print(c.casefold())


# print(n.upper())
# print(n.lower())

a="he is a good boy in the class 11th"
# print(a.find("is"))

# print(ab.lower())  #convert in to lower
# print(a.upper())    #convert into upper case

#replace
# print(a.replace("is", "are"))  #he are a good boy in the class 11th

x="hey bro how are you i think you are fine"

# print(len(ab))
# print(ab.center(10,"o"))
txt = "banana"

# x = txt.center(20)

# print(x)
# txt = "banana"

# x = txt.center(20, "O")

# print(x)
# print(ab.center(20,"*"))           #***Debashish sahu***
# print(ab.center(25,"^"))        #^^^^^^Debashish sahu^^^^^
# print(ab.join("shiba"))
'''txt = "welcome to the jungle"

x = txt.split()'''

# print(x)
# print("This week I'm workigm on {1},{2} and {4}".format('Mon','Tue','Wed','Thu','Fri'))

#string formating
# me="deb"
# a="this is %s"%me
# print(a)

# another method
m="debashish"
p=1
b="this is {} {}"
c=b.format(m,p)
# print(c)
# print(f"this is {m} {p}")

# another method
m="debashish"
p=1
q=76
r="sahu"
b="this is {0} {3}"
c=b.format(m,p,q,r)
print(c)

import math
# fstring
a=f"this is {m} {p} {3*2} {math.cos(60)}"
# print(a)
