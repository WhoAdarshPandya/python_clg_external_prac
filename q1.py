from tkinter import *
from PIL import ImageTk,Image

print("hello world")
# main window
window = Tk()

# function for RB-payment
def sel():
    print("you selected option")
    print(str(var.get()))

# function for RB-delivery
def sell():
    print("you selected option")


# select payment option
var = IntVar()

# select delivery option
varr = IntVar() 

# add canvas to add image
canvas = Canvas(window,width=800,height=200,bg="red")
canvas.pack()
# use ImageTk to read image
img = ImageTk.PhotoImage(Image.open("./photo.jpg"))
canvas.create_image(0, 0,anchor=NW, image=img) 

# add input group
group = LabelFrame(window,width=800, text="Customer Info", padx=5, pady=5)
group.pack(fill="x",side=TOP)

# add label 1 and entry 1
lbl = Label(group,text="Name :")
lbl.pack(side=LEFT)
w = Entry(group)
w.pack(side=LEFT)
# add label 2 and entry 2
lbl2= Label(group,text="Address : ")
lbl2.pack(side=LEFT)
w2 = Entry(group)
w2.pack(side=LEFT)
# add label 3 and entry 3
lbl2= Label(group,text="Phone : ")
lbl2.pack(side=LEFT)
w2 = Entry(group)
w2.pack(side=LEFT)
# add another input group for payment
payment_group = LabelFrame(group,text="payment",padx=5,pady=5)
payment_group.pack(side=BOTTOM)
rb1 = Radiobutton(payment_group,text="Cash",variable=var,value=1,command=sel)
rb1.pack(side=LEFT)
rb2 = Radiobutton(payment_group,text="cheque",variable=var,value=2,command=sel)
rb2.pack(side=LEFT)
rb3 = Radiobutton(payment_group,text="Credit Card",variable=var,value=3,command=sel)
rb3.pack(side=LEFT)

# add another input group delivery
delivery_group = LabelFrame(group,text="Delivery",padx=5,pady=5)
delivery_group.pack(side=BOTTOM)

# add radio button
rb4 = Radiobutton(delivery_group,text="Home Delivery",variable=varr,value=4,command=sell)
rb4.pack(side=LEFT)
rb5 = Radiobutton(delivery_group,text="Pickup",variable=varr,value=5,command=sell)
rb5.pack(side=LEFT)

window.tk.call('wm','iconphoto',window._w,PhotoImage(file="./slice.png"))
window.geometry("800x500")
window.mainloop()