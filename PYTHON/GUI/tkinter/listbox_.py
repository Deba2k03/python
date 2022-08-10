from msilib.schema import ListBox
from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("list Box")
i=0
def add():
    global i
    lbx.insert(ACTIVE,f"{i} ")
    i+=1
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"first item of our listbox")
Button(root,text="add",command=add).pack()
root.mainloop()