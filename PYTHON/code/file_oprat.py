'''f=open("file_write.txt")
print(f.tell())  #print the location of pointer(f)
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())'''

# reset the location of pointer
'''print(f.readline())
f.seek(10)   #go to 10 position of pointer or handler  #reset the location
print(f.readline())
f.close()'''

file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.read())
print()
file1.close()
