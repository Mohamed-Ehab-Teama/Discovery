import tkinter as tk

root = tk.Tk()

root.geometry("600x450")
root.title("Session 2 Program")

label1 = tk.Label(root, text="UserName", font=("Arial",20), bg="yellow", fg="red")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Password", bg="yellow", fg="red")
label2.pack()
entry2 = tk.Entry(root, show="*")
entry2.pack()

fram0 = tk.Frame(root, width=200, height=150, bg="red", cursor="hand2")
fram0.pack(padx=10, pady=10)

def spaek():
    print ("Hello World")


def speak_again(speech):
    print (speech)


def gg():
    labelx = tk.Label(fram0, text="new label")
    labelx.pack()


btn1 = tk.Button(fram0, text="Click Me One", command=gg)
btn1.pack()


btn2 = tk.Button(fram0, text="Click Me Two", command=lambda:speak_again("Mohamed Ehab Teama") )
btn2.pack()





root.mainloop()