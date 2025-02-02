import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry('600x500')
root.title('Session 03 - Python - Tkinter - GUI')

# User Name or Email
# l1 = tk.Label(root, text="Enter Email", font=(25), fg='red', bg='blue' )
# l1.pack( padx=10, pady=10 )

# userName = tk.Entry(root, width=50, justify='center', font=30)
# userName.pack( pady=10 )

# # Password
# l2 = tk.Label(root, text="Enter Password", font=(25), fg='red', bg='blue' )
# l2.pack( padx=10, pady=10 )

# user_password = tk.Entry(root, width=50, justify='center', font=30, show='*')
# user_password.pack( pady=10 )


# # Button
# login = tk.Button(root, text="Login", font=(30) , bg='black', fg='yellow' )
# login.pack()

# # Message
# mess = tk.Message(root, text="This is My Message", font=(20), width=200, fg='red', bg='yellow')
# mess.pack()


# Radio Button
# gender = StringVar()
# # gender = IntVar()
# r1 = tk.Radiobutton(root, text="Option 1", variable=gender, value="hello")
# r1.pack()

# r2 = tk.Radiobutton(root, text="Option 2", variable=gender, value="hello2")
# r2.pack()


# ChackButton
ch1 = tk.Checkbutton(root, text='Footabll', onvalue="Foot", offvalue='Not Found')
ch1.pack()

ch2 = tk.Checkbutton(root, text='BasketBall', onvalue="basket", offvalue='Not Found')
ch2.pack()

ch3 = tk.Checkbutton(root, text='Volly', onvalue="Volly", offvalue='Not Found')
ch3.pack()




root.mainloop()