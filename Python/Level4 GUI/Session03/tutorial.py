from tkinter import *
import tkinter as tk

root = tk.Tk()

root.geometry('600x500')
root.title('Tkinter Tutorial')

# ------------------------------------------------------------------------------------
# Message Widget
# Message(parent, options)
# message01 = tk.Message(root, text='This is Message Widget', bg='orange', fg='blue')
# message01.pack()



# ------------------------------------------------------------------------------------
# Radio Button
# Radio(root, options)

# def h(number):
#     print(var.get(), number)
# def h():
#     print(var.get())

# var = IntVar()
# rad01 = tk.Radiobutton(root, text='option 01', value= 1, variable=var)
# rad01.pack()
# rad02 = tk.Radiobutton(root, text='option 01', value= 2, variable=var)
# rad02.pack()
# rad03 = tk.Radiobutton(root, text='option 01', value= 3, variable=var)
# rad03.pack()

# btn = tk.Button(root, text='Get Value of Radio', command=lambda: h())
# btn.pack()

# var = StringVar()
# rad01 = tk.Radiobutton(root, text='option 01', value= "option 01", variable=var)
# rad01.pack()
# rad02 = tk.Radiobutton(root, text='option 01', value= 'option 02', variable=var)
# rad02.pack()
# rad03 = tk.Radiobutton(root, text='option 01', value= "option 03", variable=var)
# rad03.pack()

# btn = tk.Button(root, text='Get Value of Radio', command=lambda: h())
# btn.pack()


# ------------------------------------------------------------------------------------
# Check Button
# CHECKBUTTON(parent, options)

# def say():
#     print(var.get())

# var = StringVar()

# ch1 = tk.Checkbutton(root, text='option 01', variable=var, onvalue="Mohamed", offvalue="Not selected", command=say)
# ch1.pack()
# ch2 = tk.Checkbutton(root, text='option 02')
# ch2.pack()
# ch3 = tk.Checkbutton(root, text='option 3')
# ch3.pack()


# ------------------------------------------------------------------------------------

root.mainloop()