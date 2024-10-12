from tkinter import *
import tkinter as tk

root = tk.Tk()

root.geometry('600x450')
root.title('Session 03 GUI')

# Message Widget
# mess = tk.Message(root, text="This is the first message", bg='red', fg='yellow', font=('Arial',30), cursor='hand2', width=500)
# mess.pack()


# Radio Button
# def out():
#     print( var.get())

# var = StringVar()
# rad1 = tk.Radiobutton(root, text='Male', value="Male", variable=var, command=out)
# rad2 = tk.Radiobutton(root, text='Female', value="Female", variable=var, command=out)
# rad1.pack()
# rad2.pack()


# Check Button
def out():
    print (var.get())

var = StringVar()

ch1 = tk.Checkbutton(root, text="Football", onvalue="Football", offvalue="No football",variable=var, command=out)
ch2 = tk.Checkbutton(root, text="BasketBall", onvalue='Basketball', offvalue='No BasketBall')
ch3 = tk.Checkbutton(root, text="Swimming", onvalue='Swimming', offvalue= ' no swimming')
ch1.pack()
ch2.pack()
ch3.pack()


root.mainloop()