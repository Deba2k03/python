from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("coding")
root.geometry("300x300")
def getrs():
    print(f"we have send money to your account {myslider.get()}rs")
    tmsg.showinfo("amount credited",f"we have credited {myslider.get()} rs to your account")
# myslider = Scale(root,from_=0,to=455)
# myslider.pack()
Label(root,text="How many rs do you want:").pack()
# myslider = Scale(root,from_=0,to=100,orient=HORIZONTAL)
myslider = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider.set(50)   #default value
myslider.pack()
Button(root,text="get Rupees",command=getrs).pack()
root.mainloop()