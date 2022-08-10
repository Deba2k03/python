# import time

# def searcher():
#     #some 4 sec. time consuming task
#     book="this is a book of deb"
#     time.sleep(4)

#     while True:
#         text=(yield)
#         if text in book:
#             print("your text is in the book")
#         else:
#             print("your text is not in the book")

# search=searcher()
# print("search started")
# next(search)
# print("next method run")
# search.send("deb")
# input("press any key:")
# search.send("of")
# input("press any key:")
# search.send("joker")

# search.close()
# search.send("hii")  #error

import time


def s():
    f = open("file_write.txt")
    time.sleep(4)
    r = f.read()
    while True:
        name = (yield)
        if name in r:
            print("your name in the file")
        else:
            print("your name is not inn the file")


ss = s()
next(ss)
g = input("Enter your name:")
ss.send(g)
g2 = input("Enter your name:")
ss.send(g2)
