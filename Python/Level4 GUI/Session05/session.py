import tkinter as tk

root = tk.Tk()

root.geometry('500x450')
root.title('Session 05 GUI')

label1 = tk.Label(root, text='Enter Your Text : ')
label1.pack()

# scroll = tk.Scrollbar(root, orient='vertical')
# scroll.pack( side='right', fill='y' )

# text = tk.Text(root, width=60, height=5, wrap='none', yscrollcommand=scroll.set)
# text.pack()


# scroll.config( command= text.yview )

frame = tk.Frame(root, bg='white')
# frame.pack( padx=20, pady=20, ipadx=20, ipady=20 )
frame.pack()

scroll = tk.Scrollbar(frame, orient='vertical')
scroll.pack( side='right', fill='y' )

T = tk.Text(frame, width= 40, height=10, yscrollcommand= scroll.set)
T.pack(ipadx=10, ipady=10, padx=10, pady=10)

scroll.config( command= T.yview )


# label2 = tk.Label(frame,text="Hello")
# label2.pack()



root.mainloop()