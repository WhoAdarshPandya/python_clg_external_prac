from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

print("hello world")
# main window
window = Tk()

# selected value vars
payment_sel_value=""
delivery_sel_value=""
crust_sel_value=""
veggies_sel_value=""
meats_sel_value=""

# function for RB-payment
def sel():
    global payment_sel_value
    if var.get() == 1:
        payment_sel_value="Cash"
    if var.get() == 2:
        payment_sel_value = "Cheque"
    if var.get() == 3:
        payment_sel_value = "Credit Card"
    print(payment_sel_value)

# fn to reset all
def clear_all():
    name.set("")
    Phone.set("")
    address.set("")
    var.set(0)
    varr.set(0)
    crust_selection.set(0)
    meat_selection.set(0)
    veggies_selection1.set("")
    veggies_selection2.set("")
    veggies_selection3.set("")
    veggies_selection4.set("")

# fn for crust selection
def crust_sell():
    global crust_sel_value
    if crust_selection.get() == 6:
        crust_sel_value= "Thin"
    if crust_selection.get() == 7:
        crust_sel_value= "Thick"
    if crust_selection.get() == 8:
        crust_sel_value = "Hand Tossed"
    if crust_selection.get() == 9:
        crust_sel_value = "Artisanal"
    print(crust_sel_value)

# fn for meat selection
def meat_sell():
    global meats_sel_value
    if meat_selection.get() == 10:
        meats_sel_value= "Pepperoni"
    if meat_selection.get() == 11:
        meats_sel_value= "Sausage"
    if meat_selection.get() == 12:
        meats_sel_value = "Hamburger"
    if meat_selection.get() == 13:
        meats_sel_value = "Canadian Baccon"
    print(meats_sel_value)

# fn for veggies sel
def veggie_sell():
    global veggies_sel_value
    veggies_sel_value = veggies_selection1.get() + veggies_selection2.get()  + veggies_selection3.get() +veggies_selection4.get()
    print(veggies_sel_value) 

# function for RB-delivery
def sell():
    global delivery_sel_value
    if varr.get() == 4:
        delivery_sel_value = "Home Delivery"
    else:
        delivery_sel_value = "Pickup"
    print(delivery_sel_value)

# detect button click
def submit():
    name_value=name.get()
    address_value = address.get()
    phone_value = Phone.get()
    print(payment_sel_value,delivery_sel_value,meats_sel_value,veggies_sel_value,crust_sel_value)

    #! to change values in text box
    # name.set("abcd")
    # address.set("efgh")
    # Phone.set("lmop")
    #todo validation
    if name_value == "" or address_value == "" or phone_value == "":
        messagebox.showinfo("some text fields are empty","please provide your name,address and phone properly")
        # messagebox.showwarning("this is warning","warning")
        # messagebox.showerror("this is error","aksjdl")
        # bool_val = messagebox.askokcancel("lorem ipsum","sit init")
        # if bool_val:
        #     messagebox.showinfo('you clicked on yes',"asd")
        # else:
        #     messagebox.showinfo("sldjfsf","dfls")
        #     window.destroy()
    if crust_sel_value == "":
        messagebox.showinfo("msg","crust is not selected")
    if meats_sel_value == "":
        messagebox.showinfo("msg","Meat is not selected")
    if veggies_sel_value == "":
        messagebox.showinfo("msg","veggie not selected")
    if payment_sel_value == "":
        messagebox.showinfo("msg","payment not selected")
    if delivery_sel_value == "":
        messagebox.showinfo("msg","delivery not selected")

# select payment option
var = IntVar()

# select delivery option
varr = IntVar() 

name = StringVar()
address = StringVar()
Phone = StringVar()

# crust selection RB
crust_selection = IntVar()
meat_selection = IntVar()
veggies_selection1 = StringVar()
veggies_selection2 = StringVar()
veggies_selection3 = StringVar()
veggies_selection4 = StringVar()

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
chkbox1 = Checkbutton(veggiesLabelFrame,text="Peppers",variable=veggies_selection1,onvalue="Peppers",offvalue="",command=veggie_sell)
chkbox2 = Checkbutton(veggiesLabelFrame,text="Onions",variable=veggies_selection2,onvalue="Onions",offvalue="",command=veggie_sell)
chkbox3 = Checkbutton(veggiesLabelFrame,text="Mushrums",variable=veggies_selection3,onvalue="Mushrooms",offvalue="",command=veggie_sell)
chkbox4 = Checkbutton(veggiesLabelFrame,text="Olives",variable=veggies_selection4,onvalue="Olives",offvalue="",command=veggie_sell)
chkbox1.pack()
chkbox2.pack()
chkbox3.pack()
chkbox4.pack()

# Meats
meatsLabelFrame = LabelFrame(window,text="Meats",padx=5,pady=5)
meatsLabelFrame.pack(side=LEFT,padx=20)
rb10 = Radiobutton(meatsLabelFrame,text="Pepperoni",variable=meat_selection,value=10,command=meat_sell)
rb10.pack()
rb11 = Radiobutton(meatsLabelFrame,text="sausage",variable=meat_selection,value=11,command=meat_sell)
rb11.pack()
rb12 = Radiobutton(meatsLabelFrame,text="Hamburger",variable=meat_selection,value=12,command=meat_sell)
rb12.pack()
rb13 = Radiobutton(meatsLabelFrame,text="canadian bacon",variable=meat_selection,value=13,command=meat_sell)
rb13.pack()

# pack button on main
btn = Button(window,text="place order",command=submit,bg ="#01796f",fg="white")
btn.pack(pady=5,padx=5,side=BOTTOM)
btn = Button(window,text="reset",command=clear_all,bg ="#01796f",fg="white")
btn.pack(pady=5,padx=5,side=BOTTOM)

window.tk.call('wm','iconphoto',window._w,PhotoImage(file="./slice.png"))
window.geometry("800x500")
window.mainloop()