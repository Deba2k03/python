from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("scroll Bar")

#for connecting scrollbar to widget
# 1.widget(yscrollcommand = Scrollbar.set)
#2.scrollbar.config(command=widget.yview)
# scrollbar = Scrollbar(root)
# scrollbar.pack(fill=BOTH,side=RIGHT)
# listbox = Listbox(root,yscrollcommand=scrollbar.set,width=30,height=30)
# for i in  range(200):
#     listbox.insert(END,f"Itemm {i}")

# listbox.pack(fill=BOTH)
# scrollbar.config(command = listbox.yview)


sbar = Scrollbar(root)
sbar.pack(fill="both",side=RIGHT)
text = Text(root,yscrollcommand=sbar.set,height=100)
text.pack(fill="both")
sbar.config(command=text.yview)

root.mainloop()