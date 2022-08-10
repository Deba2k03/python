from ast import Slice
from tkinter import *
root = Tk()
root.title("QUIZ")
root.geometry("400x300")
def filex():
    with open("quiz_file.txt","a") as f:
        f.write(f"you choose {sliderx.get()} \n")
    f.close()
Label(root,text="choose a amount").pack()
sliderx = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=25)
sliderx.pack()
Button(root,text="Write in file",command=filex).pack(pady=10)
root.mainloop()
