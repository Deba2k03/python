from tkinter import *
root = Tk()
root.geometry("600x400")

def get_value():
    with open("records.txt","a") as f:
        f.write(f"{name_value.get(),phone_value.get(),gender_value.get(),emergency_value.get(),payment_value.get(),foodservice_value.get()}\n")

#heading
Label(root,text="Welcom to Deb Travels",pady=20,font="comicsens 10 bold").grid(row=0,column=3)
name=Label(root,text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emergency = Label(root,text="Emergency Contact")
payment = Label(root,text="Payment mode")
#text for our form
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)
#create variable for storing
name_value=StringVar()
phone_value=StringVar()
gender_value=StringVar()
emergency_value=StringVar()
payment_value=StringVar()

foodservice_value=IntVar()

#entry for our form
name_entry=Entry(root,textvariable=name_value).grid(row=1,column=3)
phone_entry=Entry(root,textvariable=phone_value).grid(row=2,column=3)
gender_entry=Entry(root,textvariable=gender_value).grid(row=3,column=3)
emergency_entry=Entry(root,textvariable=emergency_value).grid(row=4,column=3)
payment_entry=Entry(root,textvariable=payment_value).grid(row=5,column=3)


#check box
foodservice=Checkbutton(text="want to prebook your meal",variable=foodservice_value)
#packing
foodservice.grid(row=6,column=3,pady=20)

#button and packing it and assigning it as a command
Button(text="Submit to Deb travel",command=get_value).grid(row=7,column=3,pady=20)

# _entry=Entry(root,textvariable="")

root.mainloop()
