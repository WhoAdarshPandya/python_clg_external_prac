from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

window=Tk()
total_price = "0.0"
textvar=0
title = Label(window,text="Bike Service System")
title.config(font=("Arial",15,"bold","italic"))
title.place(x=300,y=10)
lbl1 = Label(window,text="Owner Name")
lbl1.place(x=20,y=70)
lbl2 = Label(window,text="Owner Address")
lbl2.place(x=20,y=100)
lbl3 = Label(window,text="Owner Phone Number")
lbl3.place(x=20,y=130)
lbl4 = Label(window,text="Owner City")
lbl4.place(x=20,y=160)
lbl5 = Label(window,text="Service Type")
lbl5.place(x=20,y=190)
lbl6 = Label(window,text="Service Details")
lbl6.place(x=20,y=220)

def rb_check_to():
    if service_type_selection.get() == 1:
        total.config(text="0.00 (FREE)")
        scharge.config(text="0.00 (FREE)")
        gst.config(text="8.0%")
    if service_type_selection.get() == 2:
        total.config(text="")
        scharge.config(text="")
        gst.config(text="8.0%")
    
def chk_chk():
    totalp = ch_var1.get() + ch_var2.get() + ch_var3.get()
    main = (totalp * 8) / 100
    amount = totalp+main
    scharge.config(text=str(totalp))
    gst.config(text="8.0%")
    total.config(text=str(amount))

# inputs
varW1=StringVar()
varW2=StringVar()
varW3=StringVar()
variableOpiton = StringVar()
service_type_selection = IntVar()

w1=Entry(window,textvariable=varW1)
w2=Entry(window,textvariable=varW2)
w3=Entry(window,textvariable=varW3)
w1.place(x=150,y=70)
w2.place(x=150,y=100)
w3.place(x=150,y=130)

city = OptionMenu(window,variableOpiton,"","baroda","nadiad","Anand")
city.place(x=150,y=160)

frm = Frame(window)
frm.place(x=150,y=190)
rb6 = Radiobutton(frm,text="Free",variable=service_type_selection,value=1,command=rb_check_to)
rb6.pack(side=LEFT)
rb7 = Radiobutton(frm,text="Paid",variable=service_type_selection,value=2,command=rb_check_to)
rb7.pack(side=LEFT)

listbox = Listbox(window, height = 5,  width = 10,  bg = "grey", activestyle = 'dotbox',  font = "Helvetica", fg = "yellow") 
listbox.insert(1, "Nachos") 
listbox.insert(2, "Sandwich") 
listbox.insert(3, "Burger") 
listbox.insert(4, "Pizza") 
listbox.insert(5, "Burrito") 
listbox.place(x=150,y=220)

ch_var1= IntVar()
ch_var2= IntVar()
ch_var3= IntVar()
frm2 = Frame(window)
chkbox1 = Checkbutton(frm2,text="Washing",variable=ch_var1,onvalue=100,offvalue=0,command=chk_chk)
chkbox2 = Checkbutton(frm2,text="Oilchange",variable=ch_var2,onvalue=250,offvalue=0,command=chk_chk)
chkbox3 = Checkbutton(frm2,text="Battery Change",variable=ch_var3,onvalue=1200,offvalue=0,command=chk_chk)
chkbox1.pack()
chkbox2.pack()
chkbox3.pack()
frm2.place(x=150,y=320)

lbl7 = Label(window,text="Bike Maker")
lbl7.place(x=300,y=70)
frm3 = Frame(window)
bike_maker_sel=IntVar()
options = []
# fn
def rb_check():
    global options
    val = bike_maker_sel.get()
    if val == 3:
        options = ["hero1","hero2"]
    if val == 4:    
        options = ["honda","honda2"]
    if val == 5:
        options = ["bajaj2","bajaj"]
    bike_model.set_menu("",*options)
    
rb8 = Radiobutton(frm3,text="hero",variable=bike_maker_sel,value=3,command=rb_check)
rb8.pack()
rb9 = Radiobutton(frm3,text="honda",variable=bike_maker_sel,value=4,command=rb_check)
rb9.pack()
rb10 = Radiobutton(frm3,text="bajaj",variable=bike_maker_sel,value=5,command=rb_check)
rb10.pack()


bike_model_label = Label(window,text="bike model")
bike_model_label.place(x=300,y=180)
buke_model_var=StringVar()

bike_model = OptionMenu(window,buke_model_var,"",*options)
bike_model.place(x=400,y=180)
frm3.place(x=300,y=90)

scharge_label = Label(window,text="service Charge")
scharge_label.place(x=300,y=210)

gstLabel = Label(window,text="GST(8%)")
gstLabel.place(x=300,y=230)

totalLabel = Label(window,text="Total Charges")
totalLabel.place(x=300,y=250)

total = Label(window,text="0")

total.place(x=400,y=250)
scharge = Label(window,text="")
scharge.place(x=400,y=210)

gst = Label(window,text="")
gst.place(x=400,y=230)

window.geometry("800x600")

window.mainloop()