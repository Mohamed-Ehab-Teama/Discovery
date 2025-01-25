import tkinter as tk

root = tk.Tk()

root.geometry('600x500')
root.title("Session 02 Tkinter")


# # Label
# label0 = tk.Label( root, text="Welcome To Pyhton", bg="black", fg='white', font=('Arial',25), pady=20, padx=50 )
# label0.pack()


# # Entry
# en = tk.Entry( root, bg='blue', fg='yellow', font=('Arial', 30), justify='left', border=10, relief='sunken', show='*' )
# en.pack()


# def test(x, y):
#     print("Testing now", x , y)
# # Button
# btn = tk.Button( root, text="Click Me 0 ", border=5, relief='groove', font=(15), command=lambda: test("Ahmed", "Ali") )
# btn.pack()

fr = tk.Frame(root, bg='orange', width=400, height=200)
fr.pack()

label10 = tk.Label(fr, text="We are in Frame", font=(30))
label10.pack()





root.mainloop()