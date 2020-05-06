from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import *

window = Tk()
window.title("student system")
# *all labels 
lbl1 = Label(window,text="First Name")
lbl2 = Label(window,text="Middle Name")
lbl3 = Label(window,text="Last Name")
lbl4 = Label(window,text="Date of Birth")
lbl5 = Label(window,text="City")
lbl6 = Label(window,text="Gender")
lbl7 = Label(window,text="Hobbies")
lbl1.place(x=20,y=30)
lbl2.place(x=20,y=60)
lbl3.place(x=20,y=90)
lbl4.place(x=20,y=120)
lbl5.place(x=20,y=150)
lbl6.place(x=20,y=180)
lbl7.place(x=20,y=210)

lbl8 = Label(window,text="Subject 1 Marks")
lbl9 = Label(window,text="Subject 2 Marks")
lbl10 = Label(window,text="Subject 3 Marks")
lbl11 = Label(window,text="Percentage")
lbl12 = Label(window,text="Class")
lbl13 = Label(window,text="Result")
lbl8.place(x=450,y=30)
lbl9.place(x=450,y=60)
lbl10.place(x=450,y=90)
lbl11.place(x=450,y=120)
lbl12.place(x=450,y=150)
lbl13.place(x=450,y=180)
percentage_label = Label(window,text="a")
class_label = Label(window,text="b")
result_label = Label(window,text="x")
percentage_label.place(x=550,y=120)
class_label.place(x=550,y=150)
result_label.place(x=550,y=180)

# *all labels 

#  ! controls
fname= StringVar()
mname= StringVar()
lname= StringVar()
date = StringVar()
s1mark = StringVar()
s2mark = StringVar()
s3mark = StringVar()
frm = Frame(window)
rbVar = IntVar()
rb1 = Radiobutton(frm,text="Male",variable=rbVar,value=1)
rb1.pack(side=LEFT)
rb2 = Radiobutton(frm,text="Female",variable=rbVar,value=2)
rb2.pack(side=LEFT)
options = ["a","b","c","d"]
optionVar = StringVar()
city = OptionMenu(window,optionVar,"select a value",*options)
entry1 = Entry(window,textvariable=fname)
entry2 = Entry(window,textvariable=mname)
entry3 = Entry(window,textvariable=lname)
entry4 = Entry(window,textvariable = date)
mark1 = Entry(window,textvariable = s1mark)
mark2 = Entry(window,textvariable = s2mark)
mark3 = Entry(window,textvariable = s3mark)
entry1.place(x=120,y=30)
entry2.place(x=120,y=60)
entry3.place(x=120,y=90)
entry4.place(x=120,y=120)
city.place(x=120,y=150)
frm.place(x=120,y=180)
frm2 = Frame(window)
frm3 = Frame(window)
ch_var1 = IntVar()
ch_var2 = IntVar()
ch_var3 = IntVar()
ch_var4 = IntVar()
ch_var5 = IntVar()
ch_var6 = IntVar()
chkbox1 = Checkbutton(frm2,text="Washing",variable=ch_var1,onvalue=1,offvalue=0)
chkbox2 = Checkbutton(frm2,text="Oilchange",variable=ch_var2,onvalue=2,offvalue=0)
chkbox3 = Checkbutton(frm2,text="Battery Change",variable=ch_var3,onvalue=3,offvalue=0)
chkbox4 = Checkbutton(frm3,text="Battery Change",variable=ch_var4,onvalue=4,offvalue=0)
chkbox5 = Checkbutton(frm3,text="Battery  ",variable=ch_var5,onvalue=5,offvalue=0)
chkbox6 = Checkbutton(frm3,text="Battery s",variable=ch_var6,onvalue=6,offvalue=0)
chkbox1.pack(side=LEFT)
chkbox2.pack(side=LEFT)
chkbox3.pack(side=LEFT)
chkbox4.pack(side=LEFT)
chkbox5.pack(side=LEFT)
chkbox6.pack(side=LEFT)
frm2.place(x=120,y=210)
frm3.place(x=120,y=230)

mark1.place(x=550,y=30)
mark2.place(x=550,y=60)
mark3.place(x=550,y=90)
def a():
    classs = ""
    result= ""
    total = int(s1mark.get())+int(s2mark.get())+int(s3mark.get())
    per = total/3
    percentage_label.config(text=str(per))
    if per >= 80:
        classs = "A"
        result = "pass"
    elif per > 60 and per < 80:
        classs = "B"
        result= "pass"
    else:
        classs = "C"
        result = "fail"
    class_label.config(text=str(classs))
    result_label.config(text= result)
    print(per)
    print(classs)
    name = fname.get() + " " + mname.get() + " " + lname.get() 
    f = open(f'./results/{name}.txt','w')
    f.write("===============================================================\n")
    f.write(f'name : {name}\n')
    f.write(f'Birth Data : {date.get()}\n')
    f.write(f'City : {optionVar.get()}\n')
    f.write(f'Total : {total}\n')
    f.write(f'Result : {result}\n')
    f.write(f'class : {classs}\n')
    f.write(f'percentage : {per}\n')
    f.write("===============================================================")
    f.close()

def b():
    pass
def c():
    pass
btn = Button(window,text="EXIT",command=b)
btn1 = Button(window,text="CHECK & SAVE",command=a)
btn2 = Button(window,text="RESET",command=c)
btn.place(x=20,y=500)
btn1.place(x=250,y=500)
btn2.place(x=500,y=500)
#  ! controls
window.geometry("800x600")
window.mainloop()