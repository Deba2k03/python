from tkinter import *
from time import strftime
import time
import pygame
pygame.mixer.init()
pygame.mixer.music.load('n1.mp3')
def at():
    xy = dn.get()
    time.sleep(xy)
    pygame.mixer.music.play()
def after_time():
    rt = Tk()
    rt.title("set alarm")
    rt.geometry("300x300")
    Label(rt,text="Enter hour time",font="lucida 15").pack(padx=30,pady=20)
    dn = StringVar()
    Entry(rt,textvariable=dn).pack(padx=10)
    Label(rt,text="Enter minute time",font="lucida 15").pack(padx=30,pady=20)
    mn = StringVar()
    Entry(rt,textvariable=mn).pack(padx=10)
    Button(rt,text="set",command=at,font="lucida 20",bg="grey",fg="white",width=7).pack(padx=10,pady=20)
    rt.mainloop()
def sets():
    pass
def set_alarm():
    r = Tk()
    r.title("set alarm")
    r.geometry("300x300")
    Label(r,text="Enter hour time",font="lucida 15").pack(padx=30,pady=20)
    tm = StringVar()
    Entry(r,textvariable=tm).pack(padx=10)
    Label(r,text="Enter minute time",font="lucida 15").pack(padx=30,pady=20)
    m = StringVar()
    Entry(r,textvariable=m).pack(padx=10)
    Button(r,text="set",command=sets,font="lucida 20",bg="grey",fg="white",width=7).pack(padx=10,pady=20)
    r.mainloop()
def timer():
    tick = strftime('%I:%M:%S %p')
    cl.after(1000,timer)
    cl.config(text=tick)
if __name__=='__main__':
    root = Tk()
    root.geometry("400x300")
    root.title("Alarm")
    Label(root,text="Alarm",font="lucida 30").pack()
    cl =Label(root,font="sans 25 bold")
    cl.pack(pady=20)
    f1 = Frame(root)
    f1.pack(side=LEFT)
    f2 = Frame(root)
    f2.pack(side=RIGHT)
    timer()
    Button(f1,text="set alarm",command=set_alarm,font="senc 20",bg="grey",fg="white").pack(side=BOTTOM,anchor=W,padx=20,pady=30)
    Button(f2,text="After time",command=after_time,font="senc 20",bg="grey",fg="white").pack(side=BOTTOM,anchor=N,padx=20,pady=30)
    root.mainloop()