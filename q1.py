import tkinter as tk

print("hello world")
window = tk.Tk()
canvas = tk.Canvas(window,width=300,height=300)
canvas.pack()
img = tk.PhotoImage(file = "./photo.jpg")
canvas.create_image(20,20,anchor=tk.NW,image=img)
window.tk.call('wm','iconphoto',window._w,tk.PhotoImage(file="./slice.png"))
window.geometry("800x500")
window.mainloop()