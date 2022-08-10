from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Debashish")
f1=Frame(root)
f1.pack(pady=100)
l1= Label(f1,text="Introduction",fg="black")
l1.pack()

def name():
    print("Debashish")

def age():
    print("18")

def clg():
    print("panchayat college bargarh")
b1=Button(f1,text="print name",command=name)
b1.pack()
b2=Button(f1,text="print age",command=age)
b2.pack()
b3=Button(f1,text="print college",command=clg)
b3.pack()
root.mainloop()