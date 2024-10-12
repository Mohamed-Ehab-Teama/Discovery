import tkinter as tk
from functools import partial


root = tk.Tk()

root.geometry("800x650")
root.title("Session 2 Tkinter")

userName = ""

label = tk.Label(root, text = "Heading Label", font = ("Arial",30), bg="yellow", fg="red", padx="50", pady="50", anchor="center" )
label.pack()

en = tk.Entry(root, bg="red", fg="white", bd="10", justify='center', relief='sunken', show='#', textvariable=userName)
en.pack()


frame = tk.Frame(root, bg='Yellow', bd=4, cursor='hand2', height=100, highlightcolor="red", highlightthickness=4, highlightbackground='blue', relief='ridge', width=400)
frame.pack(padx=50, pady=50)

def func0 (txt):
    print (txt);


btn = tk.Button(frame, text="Click Me One", command=lambda : func0("Hello Mohamed") )
btn.pack()

btn0 = tk.Button(frame, text="Click Me Two", command=partial(func0, "Hello From Button 2") )
btn0.pack()



root.mainloop()