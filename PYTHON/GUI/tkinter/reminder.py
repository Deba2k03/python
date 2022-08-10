# from PIL import Image,ImageTk
from tkinter import *
import tkinter.messagebox as tmsg
import pygame
import time
from plyer import notification
pygame.mixer.init()
pygame.mixer.music.load("remind_02.mp3")
def set_a():
    root.destroy()
    if tm.get()!="":
        a=int(tm.get())*60*60
    else:
        a=0
    if tn.get()!="":
        b=int(tn.get())
    else:
        b=0
    while True: 
        time.sleep(a+b)
        pygame.mixer.music.play()
        tmsg.showinfo("Reminder","time's up!")
        notification.notify(title="Reminder",message="time's up!",app_name="Reminder",toast=True,timeout=10)
        q=tmsg.askyesno("Reminder","Want to stop the reminder?")
        if q:
            set_c()
def set_c():
    exit()
def set_b():
    root.destroy()
if __name__=='__main__':
    root = Tk()
    root.title("Reminder")
    root.geometry("300x200")
    Label(root,text="Enter Hour",font="lucida 10").pack()
    tm = StringVar()
    tn = StringVar()
    Entry(root,textvariable=tm).pack()
    Label(root,text="Enter Minute",font="lucida 10").pack()
    Entry(root,textvariable=tn).pack()
    Button(root,text="ON",width=4,height=1,bg="green",fg="yellow",command=set_a).pack(side=LEFT,padx=35)
    Button(root,text="OFF",width=4,height=1,command=set_b,bg="red",fg="yellow").pack(side=RIGHT,padx=35)
    root.mainloop()