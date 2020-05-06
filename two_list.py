from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter.ttk import *
import csv
import os
import xlsxwriter 
i = j =4
def lb1(evt):
    print(listbox1.get(listbox1.curselection()))

def lb2(evt):
    print(listbox2.get(listbox2.curselection()))

def swap():
    listbox2.insert(j+1,listbox1.get(listbox1.curselection()))
    listbox1.delete(ANCHOR)

def swap2():
    listbox1.insert(i+1,listbox2.get(listbox2.curselection()))
    listbox2.delete(ANCHOR)

def swap3():
    arr = listbox1.curselection()
    print(arr)
    for i in arr:
        listbox2.insert(j+1,listbox1.get(i))
    for i in arr[::-1]:
        listbox1.delete(i)

def swap4():
    arr = listbox2.curselection()
    print(arr)
    for k in arr:
        listbox1.insert(i+1,listbox2.get(k))
    for k in arr[::-1]:
        listbox2.delete(k)

window = Tk()
window.geometry("500x400")
window.title("1 ka double")
listbox1 = Listbox(window,selectmode='multiple')
listbox1.bind('<<ListboxSelect>>',lb1)
listbox1.insert(1,"abcd")
listbox1.insert(2,"efgh")
listbox1.insert(3,"hijk")
listbox1.insert(4,"lmop")
listbox1.place(x=10,y=10)

listbox2 = Listbox(window,selectmode='multiple')
listbox2.bind('<<ListboxSelect>>',lb2)
listbox2.insert(1,"abcd")
listbox2.insert(2,"efgh")
listbox2.insert(3,"hijk")
listbox2.insert(4,"lmop")
listbox2.place(x=280,y=10)

btn = Button(window,text=">",command=swap)
btn.place(x=150,y=30)
btn2 = Button(window,text="<",command=swap2)
btn2.place(x=150,y=70)
btn3 = Button(window,text=">>",command=swap3)
btn3.place(x=150,y=120)
btn3 = Button(window,text="<<",command=swap4)
btn3.place(x=150,y=150)

window.mainloop()