from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Debashish")
user = Label(root, text="User name")
password = Label(root, text="password")
user.grid()
password.grid(row=1)


def getvalue():
    print("the value of user name is", user_value.get())
    print("the value of password is", password_value.get())


# variable classe in tkinter
# 1.boolean var
# 2.double var
# 3.StringVar
# 4.Int var
user_value = StringVar()
password_value = StringVar()

user_entry = Entry(root, textvariable=user_value)
pass_entry = Entry(root, textvariable=password_value)
user_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

b1 = Button(text="submit", command=getvalue).grid()


root.mainloop()
