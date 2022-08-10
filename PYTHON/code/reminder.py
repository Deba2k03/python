import time
from tkinter import *
from win32com.client import Dispatch

r =True
def speak(str):
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
def set_a():
    global r
    a=int(t.get())
    b=tm.get()
    while r:
        # time.sleep(a*60*60)
        time.sleep(a)
        speak(f"{b}")
def dele():
    global r
    r=FALSE
if __name__=='__main__':
    root = Tk()
    root.title("Reminder")
    root.geometry("400x300")
    Label(root,text=">>Reminder<<",font="senc 20").pack()
    Label(root,text="Enter timelimit",font="lucida 15").pack(pady=15)
    t = StringVar()
    Entry(root,textvariable=t).pack()
    Button(root,text="ON",command=set_a,font="lucida 10 bold",bg="grey",fg="white").pack(pady=10)
    Button(root,text="OFF",command=dele,font="lucida 10 bold",bg="grey",fg="white").pack(pady=10)
    root.mainloop()