import tkinter as tk

root = tk.Tk()  # window 

root.geometry("800x600")
root.title(" My First Project ")

label01 = tk.Label(root, text="Enter Name")
name = tk.Entry(root)

label02 = tk.Label(root, text="Enter Password")
password = tk.Entry(root)

login = tk.Button(root, text="Login")

label01.pack()
name.pack()
label02.pack()
password.pack()
login.pack()

root.mainloop()