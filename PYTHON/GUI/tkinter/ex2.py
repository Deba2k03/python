from tkinter import *
root = Tk()
root.geometry("400x400")
def s():
    root.geometry(f"{x.get()}x{y.get()}") 
Label(root,text="Width").pack()
x=StringVar()
e1=Entry(root,textvariable=x).pack()
y=StringVar()
Label(root,text="Height").pack()
e2=Entry(root,textvariable=y).pack()

a=Button(root,text="Apply",command=s).pack()


# size(c_width,c_height)
root.mainloop()