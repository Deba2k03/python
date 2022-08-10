from tkinter import *
from datetime import datetime
import time
from time import strftime
import pygame
pygame.mixer.init()

pygame.mixer.music.load('n1.mp3')
def set_alarm():
    r = Tk()
    r.geometry("300x300")
    r.mainloop()
def after_time():
    a = int(tm.get())
    time.sleep(a)
    pygame.mixer.music.play()
def add_music():
    pass
def about_us():
    pass
def clock():
    tick = strftime('%I:%M:%S %p')
    cl.after(1000,clock)
    cl.config(text=tick)
def stop_music():
    pygame.mixer.music.stop()



if __name__=='__main__':
    root = Tk()
    root.title("Alarm")
    root.geometry("400x400")
    Label(root,text="Alarm",font="lucida 20 bold").pack(pady=10)
    cl = Label(root,font="sans 20")
    cl.pack()
    clock()
    f1=Frame(root)
    f1.pack(side=LEFT)
    Label(f1,text="Set Alarm",font="lucida 15").pack(padx=30)
    tm = StringVar()
    Entry(f1,textvariable=tm).pack(padx=10)
    Button(f1,text="set alarm",width=4,height=1,command=set_alarm).pack(padx=10,pady=20)
    f2=Frame(root)
    f2.pack(side=RIGHT)
    Label(f2,text="After time",font="lucida 15").pack(padx=10)
    Entry(f2,textvariable=tm).pack(padx=30)
    Button(f2,text="Ok",width=4,height=1,command=after_time).pack(padx=10,pady=20)
    Button(root,text="STOP",command=stop_music,width=10,height=3,font="lucida 10 bold").pack(side=BOTTOM)
    mainmanu =Menu(root)
    m1 = Menu(mainmanu,tearoff=0)
    m1.add_command(label="add music",command=add_music)
    m1.add_command(label="about us",command=about_us)
    mainmanu.add_cascade(label="setting",menu=m1)
    root.config(menu=mainmanu)

    root.mainloop()