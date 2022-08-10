from tkinter import *

def upload():
    statusvar.set("busy...")
    # sbar.update()
    import time
    time.sleep(2)
    statusvar.set("ready now")
root = Tk()
root.title("status bar")
root.geometry("400x400")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=X)

Button(root,text="upload",command=upload).pack()
root.mainloop()