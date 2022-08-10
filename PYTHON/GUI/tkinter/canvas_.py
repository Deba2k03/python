from tkinter import *
root = Tk()
root.title("Ddebashish")
canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack() 

# the line goes from x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
# can_widget.create_line(0,400,800,0,fill="red") 

#to create a rectangle specify parameter in this order:- co-ordinates of left cornur and co-ordinates of right buttum cornur
# can_widget.create_rectangle(50,50,750,350,fill="blue")

#print text in screen
# can_widget.create_text(400,200,text="Debashish",fill="red")

#to create a rectangle specify parameter in this order:- co-ordinates of left cornur and co-ordinates of right buttum cornur
# can_widget.create_oval(200,100,600,300,fill="grey")

# create circle to take the square co-ordinates
# can_widget.create_oval(100,100,300,300,fill="yellow")

# can_widget.create_arc(200,100,600,300)



root.mainloop()