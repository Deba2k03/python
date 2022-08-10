
from tkinter import *
from turtle import left
from PIL import Image, ImageTk
root = Tk()

# width x height
root.geometry("800x600")

# #width , height
# root.minsize(400, 300)

# #width , height
# root.maxsize(1200, 1000)

# deb = Label(text="Deb is a student and this is his GUI")
# deb.pack()

#load image png
# photo = PhotoImage(file="bullet.png")
# label1 = Label(image = photo)
# label1.pack()

#for jpg images
# image1 = Image.open("background.jpg")
# photo1 = ImageTk.PhotoImage(image1)
# label2 = Label(image = photo1)
# label2.pack()
# create title
root.title("Debashish")

#important label option
# text = adds th text
# bd = background
# fg = foreground
# font = sets the font
# 1.font=("comicsans",10,"bold")
# 2.font="cosmicsans  20 bold"
# padx = x pedding
# pady = y pedding
# relief = border Styling = SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''
i am a good,
i would to be a programmer 
inn the software industry''',bg="red",fg="white",padx=60, pady=30,font=("comicsans",10,"bold"),borderwidth=3, relief=SUNKEN
)

# title_label.pack()

#important pack option
# anchor = nw,se,sw,ne
# title_label.pack(anchor = "nw")
# title_label.pack(anchor = "ne")
# title_label.pack(anchor = "se")
# side = top,bottom,left,right
# title_label.pack(side=BOTTOM,anchor="sw")
# fill = 

# title_label.pack(side=BOTTOM,fill=X)
# title_label.pack(side=LEFT,fill=Y)
# padx=
# pady=

title_label.pack(side = LEFT,fill=Y,padx=300,pady=20)
root.mainloop()
