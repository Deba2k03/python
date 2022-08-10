from tkinter import *
root = Tk()
root.geometry("655x445")
root.title("hello title")
# root.wm_iconbitmap("bullet.png")
root.configure(background="grey")

width  = root.winfo_screenmmwidth()
height = root.winfo_screenheight()
print(f"{width} {height}")

Button(text="close",command=root.destroy).pack()
root.mainloop()