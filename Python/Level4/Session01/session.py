import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("My First GUI App in python")


lable = tk.Label(root, text="Hello From Tkinter !")
lable.pack()

lable = tk.Label(root, text="Enter Your Name:")
lable.pack()
entry = tk.Entry(root)
entry.pack(padx=10)

lable = tk.Label(root, text="Enter Your Email:")
lable.pack()
entry = tk.Entry(root)
entry.pack(padx=10)

btn = tk.Button(root, text="Submit")
btn.pack(padx=10)


txt = tk.Text(root, width=50, height=10)
txt.pack()


check1 = tk.Checkbutton(root, text="Check Me 01")
check1.pack()
check2 = tk.Checkbutton(root, text="Check Me 02")
check2.pack()

radio1 = tk.Radiobutton(root, text="opt1")
radio1.pack()
radio2 = tk.Radiobutton(root, text="opt2")
radio2.pack()

root.mainloop()