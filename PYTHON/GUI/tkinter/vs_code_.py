from msilib.schema import ListBox
from tkinter import *
import os
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
def newfile():
    global file
    root.title("Untitled-Notepad")
    file = NONE
    textarea.delete(1.0,END)


def add():
    i=0
    lbx.insert(ACTIVE,f"{i} ")
    i+=1
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),
    ("Text Documents",".txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),
        ("Text Documents",".txt")])
        if file == "":
            file = None
        else:
            with open(file,"w") as f:
                f.write(textarea.get(1.0,END))
                root.title(os.path.basename(file)+'-Notepad')
    else:
        with open(file,"w") as f:
                f.write(textarea.get(1.0,END))

def quitApp():
    root.destroy()


def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepad","Notepad by Debashish")


if __name__ == '__main__':
    root = Tk()
    root.title("Notepad")
    root.geometry("600x500")
    f1 = Frame(root)
    f1.pack(side=LEFT,fill=Y)
    textarea = Text(root, font="lucida 13")
    textarea.pack(fill=BOTH,expand=TRUE)
    file = None
    # create manu
    menubar = Menu(root)
    filemanu = Menu(menubar, tearoff=0)
    # open new file
    filemanu.add_command(label="New", command=newfile)
    # to open already existing file
    filemanu.add_command(label="Open", command=openfile)
    # to save the current file
    filemanu.add_command(label="save", command=savefile)
    filemanu.add_separator()
    filemanu.add_command(label="Exit", command=quitApp)
    menubar.add_cascade(label="file", menu=filemanu)

    Editmenu = Menu(menubar, tearoff=0)
    # to give a feature of cut,copy,paste
    Editmenu.add_command(label="cut", command=cut)
    Editmenu.add_command(label="copy", command=copy)
    Editmenu.add_command(label="paste", command=paste)
    menubar.add_cascade(label="Edit", menu=Editmenu)

    smenu = Menu(menubar, tearoff=0)
    smenu.add_command(label="cut", command=cut)
    smenu.add_command(label="copy", command=copy)
    smenu.add_command(label="paste", command=paste)
    menubar.add_cascade(label="Selection", menu=smenu)

    vmenu = Menu(menubar, tearoff=0)
    vmenu.add_command(label="cut", command=cut)
    vmenu.add_command(label="copy", command=copy)
    vmenu.add_command(label="paste", command=paste)
    menubar.add_cascade(label="View", menu=vmenu)

    gmenu = Menu(menubar, tearoff=0)
    gmenu.add_command(label="cut", command=cut)
    gmenu.add_command(label="copy", command=copy)
    gmenu.add_command(label="paste", command=paste)
    menubar.add_cascade(label="Go", menu=gmenu)

    Rmenu = Menu(menubar, tearoff=0)
    Rmenu.add_command(label="cut", command=cut)
    Rmenu.add_command(label="copy", command=copy)
    Rmenu.add_command(label="paste", command=paste)
    menubar.add_cascade(label="Run", menu=Rmenu)
    
    Tmenu = Menu(menubar, tearoff=0)
    Tmenu.add_command(label="cut", command=cut)
    Tmenu.add_command(label="copy", command=copy)
    Tmenu.add_command(label="paste", command=paste)
    menubar.add_cascade(label="Terminal", menu=Tmenu)
    # help menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="about notepad", command=about)
    menubar.add_cascade(label="help", menu=helpmenu)

    root.config(menu=menubar)

    lbx = Listbox(f1)
    lbx.pack(side=LEFT,fill=Y)
    lbx.insert(END,"EXPLORER")

    #add scroll bar
    # scrollbar = Scrollbar(lbx)
    # scrollbar.pack(side=RIGHT,fill=Y)
    # scrollbar.config(command=lbx.yview)
    # lbx.config(yscrollcommand=scrollbar.set)


    root.mainloop()
