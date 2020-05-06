from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import *
import csv
import os
import xlsxwriter 


def saveData():
    pass

def clearData():
    variable.set("selectOne")
    busnum.set("")
    mincharge.set("")
    cfare.set("")
    afare.set("")
    fareinc.set("")
    depot.set("")

window = Tk()
window.config(bg="#FFFDD0")
window.title = "Bus Booking"
# add canvas to add image

canvas = Canvas(window,width=800,height=150,bg="#000")
canvas.pack()
read = Image.open("./download.jpg")
read = read.resize((150, 150), Image.ANTIALIAS)
img = ImageTk.PhotoImage(read)

canvas.create_image(0, 0,anchor="nw", image=img) 
lbl = Label(window,text="K.S.R.T.C BUS DETAILS",background="black",foreground="#FFFDD0")
lbl.config(font=("Times New Roman",25,"bold"))
lbl.place(x=250,y=50)

# labels
busTypeLabel = Label(window,text="Bus Type",background="#FFFDD0")
busTypeLabel.place(x=20,y=200)
busNumberLabel = Label(window,text="Bus Number",background="#FFFDD0")
busNumberLabel.place(x=20,y=250)
MinimumChargeKLabel = Label(window,text="Minimum charge",background="#FFFDD0")
MinimumChargeKLabel.place(x=20,y=300)
DepotLabel = Label(window,text="Depot",background="#FFFDD0")
DepotLabel.place(x=20,y=350)
fareIncrementLabel = Label(window,text="Fare Increment",background="#FFFDD0")
fareIncrementLabel.place(x=20,y=400)
childFare = Label(window,text="Child Fare",background="#FFFDD0")
childFare.place(x=20,y=450)
adultFare = Label(window,text="Adult Fare",background="#FFFDD0")
adultFare.place(x=20,y=500)

# inputs
variable = StringVar()
busnum = StringVar()
mincharge =StringVar()
depot = StringVar()
fareinc = StringVar()
cfare = StringVar()
afare = StringVar()

w = OptionMenu(window,variable,"select One","Luxury","lorem","ipsum")
w.place(x=170,y=200)
entry2 = Entry(window,textvariable=busnum)
entry3 = Entry(window,textvariable=mincharge)
entry4 = Entry(window,textvariable=depot)
entry5 = Entry(window,textvariable=fareinc)
entry6 = Entry(window,textvariable=cfare)
entry7 = Entry(window,textvariable=afare)
entry2.place(x=170,y=250)
entry3.place(x=170,y=300)
entry4.place(x=170,y=350)
entry5.place(x=170,y=400)
entry6.place(x=170,y=450)
entry7.place(x=170,y=500)

# buttons
resetButton = Button(window,text="New",command=clearData)
resetButton.place(x=20,y=550)

saveButton = Button(window,text="Save",command=saveData)
saveButton.place(x=120,y=550)

exitButton = Button(window,text="Exit",command=exit)
exitButton.place(x=220,y=550)

window.tk.call('wm','iconphoto',window._w,PhotoImage(file="./automobile.png"))
window.geometry("800x600")
window.mainloop()