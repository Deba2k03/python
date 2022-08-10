from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("400x400")
root.title("Radio Button")

def order():
        tmsg.showinfo("Order recoived",f"we have received your order for {var2 .get()}.Thanks for orderring")

# var = IntVar()
# var.set(1)
var2 = StringVar()
var2.set("coke")
Label(root,text="What would you like to have sir",font="lucida 14 bold",
        justify=LEFT,padx=10).pack()
# radio  = Radiobutton(root,text="Dosha",padx=10,variable=var,value=1).pack(anchor="w")
# radio  = Radiobutton(root,text="Etli",padx=10,variable=var,value=2).pack(anchor="w")
# radio  = Radiobutton(root,text="bara",padx=10,variable=var,value=3).pack(anchor="w")
# radio  = Radiobutton(root,text="singhdda",padx=10,variable=var,value=4).pack(anchor="w")

list=["dosa","etli","bara","singhda"]
for item in list:
    r = Radiobutton(root,text=f"{item}",variable=var2,value=f"{item}").pack(anchor="w")

Button(root,text="order now",command=order).pack()

root.mainloop()