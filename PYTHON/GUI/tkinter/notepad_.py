from tkinter import *
import os
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
def newfile():
    global file
    root.title("Untitled-Notepad")
    file = NONE
    textarea.delete(1.0,END)


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
    # help menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="about notepad", command=about)
    menubar.add_cascade(label="help", menu=helpmenu)

    root.config(menu=menubar)

    #add scroll bar
    scrollbar = Scrollbar(textarea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)

    root.mainloop()
