from tkinter import *
root = Tk()
root.title("Debasis")
root.geometry("600x400")
def deba(event):
    print(f"you click on the botton at {event.x},{event.y}")
widge = Button(root, text='Click me please')
widge.pack()

widge.bind('<Button-1>',deba)
widge.bind('<Double-1>',quit)

root.mainloop()