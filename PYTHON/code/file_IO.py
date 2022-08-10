# file IO basic


# "r"-open file for reading---default
# "w"-open file writting
# "x"-(Exclusive creation) creates file if not exist
# "a"-(append) add more content to a file
# "t"-(text mode) text file---default
# "b"-binary mode
# "+"-read and write

x=open("file_x.txt","rt+")
x.write("debashish")
a=x.read()
print(a)
x.close()

# y=open("file_x.txt")
# print(y.read())
# y.close()
