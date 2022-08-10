from tkinter import *
root = Tk()
root.geometry("800x600")
root.title("Debashish")

f1=Frame(root, bg = "grey",borderwidth=2)#,relief=SUNKEN)
f1.pack(side = TOP,fill = X)
f2=Frame(root,bg = "grey",borderwidth=6)
f2.pack(side=LEFT,fill=Y)
l2=Label(f2,text="EXPLORER",font="helvetica 8 bold")
l2.pack(padx=30)
l1 = Label(f1,text="Visual Studio Code",fg="blue")
l1.pack(padx=30)
root.mainloop()