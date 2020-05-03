from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

print("hello world")
# main window
window = Tk()

# function for RB-payment
def sel():
    print("you selected option")
    print(str(var.get()))

# fn for crust selection
def crust_sell():
    print(str(crust_selection.get()))

# function for RB-delivery
def sell():
    print("you selected option")

# detect button click
def submit():
    name_value=name.get()
    address_value = address.get()
    phone_value = Phone.get()
    #! to change values in text box
    # name.set("abcd")
    # address.set("efgh")
    # Phone.set("lmop")
    # print(f'{phone_value} {name_value} {address_value}')
    #todo validation
    if name_value == "" or address_value == "" or phone_value == "":
        messagebox.showinfo("some fields are empty","please provide your name,address and phone properly")
        # messagebox.showwarning("this is warning","warning")
        # messagebox.showerror("this is error","aksjdl")
        # bool_val = messagebox.askokcancel("lorem ipsum","sit init")
        # if bool_val:
        #     messagebox.showinfo('you clicked on yes',"asd")
        # else:
        #     messagebox.showinfo("sldjfsf","dfls")
        #     window.destroy()

# select payment option
var = IntVar()

# select delivery option
varr = IntVar() 

name = StringVar()
address = StringVar()
Phone = StringVar()

# crust selection RB
crust_selection = IntVar()

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
w = Entry(group,textvariable=name)
w.pack(side=LEFT)
# add label 2 and entry 2
lbl2= Label(group,text="Address : ")
lbl2.pack(side=LEFT)
w2 = Entry(group,textvariable=address)
w2.pack(side=LEFT)
# add label 3 and entry 3
lbl2= Label(group,text="Phone : ")
lbl2.pack(side=LEFT)
w2 = Entry(group,textvariable=Phone)
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

# three input groups
# crust
crustLabelFrame = LabelFrame(window,text="Crust",padx=5,pady=5)
crustLabelFrame.pack(side=LEFT,padx=5,pady=5)
rb6 = Radiobutton(crustLabelFrame,text="Thin",variable=crust_selection,value=6,command=crust_sell)
rb6.pack()
rb7 = Radiobutton(crustLabelFrame,text="Thick",variable=crust_selection,value=7,command=crust_sell)
rb7.pack()
rb8 = Radiobutton(crustLabelFrame,text="HandTossed",variable=crust_selection,value=8,command=crust_sell)
rb8.pack()
rb9 = Radiobutton(crustLabelFrame,text="Artisanal",variable=crust_selection,value=9,command=crust_sell)
rb9.pack()

# Veggies 
veggiesLabelFrame = LabelFrame(window,text="Veggies",padx=5,pady=5)
veggiesLabelFrame.pack(side=LEFT,padx=40)
chkbox1 = Checkbutton(veggiesLabelFrame,text="Peppers")
chkbox2 = Checkbutton(veggiesLabelFrame,text="Onions")
chkbox3 = Checkbutton(veggiesLabelFrame,text="Mushrums")
chkbox4 = Checkbutton(veggiesLabelFrame,text="Olives")
chkbox1.pack()
chkbox2.pack()
chkbox3.pack()
chkbox4.pack()

# Meats
meatsLabelFrame = LabelFrame(window,text="Meats",padx=5,pady=5)
meatsLabelFrame.pack(side=LEFT,padx=20)
rb10 = Radiobutton(meatsLabelFrame,text="Pepperoni",variable=crust_selection,value=6,command=crust_sell)
rb10.pack()
rb11 = Radiobutton(meatsLabelFrame,text="Onions",variable=crust_selection,value=6,command=crust_sell)
rb11.pack()
rb12 = Radiobutton(meatsLabelFrame,text="Mushrooms",variable=crust_selection,value=6,command=crust_sell)
rb12.pack()
rb13 = Radiobutton(meatsLabelFrame,text="Olives",variable=crust_selection,value=6,command=crust_sell)
rb13.pack()

# pack button on main
btn = Button(window,text="place order",command=submit,bg ="#01796f",fg="white")
btn.pack(pady=5,padx=5,side=BOTTOM)

window.tk.call('wm','iconphoto',window._w,PhotoImage(file="./slice.png"))
window.geometry("800x500")
window.mainloop()