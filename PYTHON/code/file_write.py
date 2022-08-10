f=open("file_write.txt","w")
f.write("my self debashish sahu")
f.close()
#append method
x=open("file_write.txt","a")
a=x.write("\ni am a student")
x.write("\ngood")
print(a) #no of character write
x.close()

# handle read and write both
y=open("file_write.txt","r+")
print(y.read())
y.write("\nthank you")
