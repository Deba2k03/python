from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title('Note pad')
root.geometry('600x400')

def myfunc():
    print("i m good")

def help():
    print("i will help you")
    # a = tmsg.Message("This")
    b = tmsg.showinfo("help","deb will help you with this website")
    print(b)
def rate():
    value=tmsg.askquestion("Experience"," was your experience Good!")
    print(value)
    if value == "yes":
        msg = "Rate me on app store plz"
    else:
        msg = "tell us what went wrong,we will call you!"
    tmsg.showinfo("Experience",msg)
def frnd():
    ans = tmsg.askokcancel("mera frnd ban jao","sry ea intrested nehi he")
    if ans:
        print("retry karne par bhi kuch nehi hoga")
    else:
        print("thnks for cancelling")
#use this to create a non-dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="file",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="save",command=myfunc)
m1.add_command(label="new project",command=myfunc)
m1.add_separator()
m1.add_command(label="save as",command=myfunc)
m1.add_command(label="print",command=myfunc)
root.config(menu = mainmenu)
mainmenu.add_cascade(label="file",menu=m1)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="cupy",command=myfunc)
m2.add_command(label="paste",command=myfunc)
m2.add_separator()
m2.add_command(label="find",command=myfunc)
root.config(menu = mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label="help",command=help)
m3.add_separator()
m3.add_command(label="rate us",command=rate)
m3.add_command(label="Befriend",command=frnd)
mainmenu.add_cascade(label="Help",menu=m3)
root.config(menu=mainmenu)

root.mainloop()