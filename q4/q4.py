from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import *
import csv
import os
import xlsxwriter 

window = Tk()
window.config(bg="red")
window.geometry("800x600")
canvas = Canvas(window,width=800,height=100,bg="red")
canvas.pack()
read = Image.open("./download.png")
read = read.resize((250, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(read)

# labels
CityLabel = Label(window,text="City",background="red",foreground="white")
CityLabel.place(x=20,y=200)
CinemaLabel = Label(window,text="Cinema",background="red",foreground="white")
CinemaLabel.place(x=20,y=250)
MinimumChargeKLabel = Label(window,text="Movie",background="red",foreground="white")
MinimumChargeKLabel.place(x=20,y=300)
DepotLabel = Label(window,text="Date",background="red",foreground="white")
DepotLabel.place(x=20,y=350)
fareIncrementLabel = Label(window,text="Show Timing",background="red",foreground="white")
fareIncrementLabel.place(x=20,y=400)
childFare = Label(window,text="Class",background="red",foreground="white")
childFare.place(x=20,y=450)
adultFare = Label(window,text="No Of tickets",background="red",foreground="white")
adultFare.place(x=20,y=500)

# inputs
variable = StringVar()
variable1 = StringVar()
variable2 = StringVar()
variable3 = StringVar()
variable4 = StringVar()
variable5 = StringVar()
variable6 = StringVar()
w = OptionMenu(window,variable,"","Delhi","Ahmedabas","Baroda")
w.place(x=170,y=200)
w1 = OptionMenu(window,variable1,"","Reliance","REv mall","eutopia")
w1.place(x=170,y=250)
w2 = OptionMenu(window,variable2,"","Sholey","DevD","Karwaan")
w2.place(x=170,y=300)
w3 = OptionMenu(window,variable3,"","Delhi","Ahmedabas","Baroda")
w3.place(x=170,y=350)
w4 = OptionMenu(window,variable4,"","10.00(SCREEN1)","1.00(SCREEN1)","4.00(SCREEN1)")
w4.place(x=170,y=400)
w5 = OptionMenu(window,variable5,"","GOLD(450rs)","platinum(550rs)","silver(250rs)")
w5.place(x=170,y=450)
w6 = OptionMenu(window,variable6,"","1","2","3","4")
w6.place(x=170,y=500)
var=""
var1=""
var2=""
var3=""
var4=""
var5=""
var6=""
def submit():
    global var
    global var1
    global var2
    global var3
    global var4
    global var5
    global var6
    var = variable.get()
    var1 = variable1.get()
    var2 = variable2.get()
    var3 = variable3.get()
    var4 = variable5.get()
    var5 = variable6.get()
    var6 = variable4.get()
    print(var)
    print(var1)
    print(var2)
    print(var3)
    print(var4)
    print(var5)
    print(var6)
    slave = Tk()
    slave.geometry("800x600")
    lbl = Label(slave,text=var2)
    lbl.pack()
    slave.mainloop()
    
    
    

btn = Button(window,text="SUBMIT",command=submit)
btn.place(x=170,y=550)
canvas.create_image(0, 0,anchor="nw", image=img) 
window.mainloop()