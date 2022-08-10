from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusvar = Label(self,textvariable=self.var,anchor=W,relief=SUNKEN)
        self.statusvar.pack(side=BOTTOM,fill=X)

    def click(self):
        print("button clicked")

    def create_button(self,inptext):
        Button(text=inptext,command=self.click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.create_button("click me")
    window.mainloop()
