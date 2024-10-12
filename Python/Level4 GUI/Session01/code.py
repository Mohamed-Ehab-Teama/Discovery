import tkinter as tk

root = tk.Tk()

root.geometry("800x650")
root.title("My First GUI in Python")

label1 = tk.Label(root, text="Enter Your Name:", font=("Arial", 16))
label1.pack()
entry1 = tk.Entry(root, width=50)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Your Email:", font=("Arial", 16))
label2.pack(pady=5)
entry2 = tk.Entry(root, width=50)
entry2.pack()

ch = tk.Checkbutton(root, text="Football")
ch.pack()
ch2 = tk.Checkbutton(root, text="BasketBall")
ch2.pack()
ch3 = tk.Checkbutton(root, text="Swimming")
ch3.pack()


rad = tk.Radiobutton(root, text="Male")
rad.pack()
rad1 = tk.Radiobutton(root, text="Female")
rad1.pack()

btn = tk.Button(root, text="LogIn", font=("Arial", 10), width=8, height=2)
btn.pack(padx=10, pady=10)



root.mainloop()