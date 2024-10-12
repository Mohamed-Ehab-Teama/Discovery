import tkinter as tk

root = tk.Tk()

root.geometry('900x600')
root.title('Session 04 GUI')


#list Box
# list_box = tk.Listbox(root, 
#     bg='yellow', 
#     fg='black', 
#     width=30,
#     height=30,
#     font=('Arial',30),
#     activestyle='underline'
# )

# list_box.insert(1, "Do HomeWork")
# list_box.insert(2, "Excerise")
# list_box.insert(3, "Eating")
# list_box.insert(4, "Sleeping")

# list_box.delete(2)

# list_box.pack()

def out():
    print ("This is new file")


menuBar = tk.Menu(root)

file_menu = tk.Menu(menuBar, tearoff=0)

file_menu.add_command(label='New File', command=out)
file_menu.add_command(label='Save', command=None)
file_menu.add_command(label='Save as', command=None)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=None)

menuBar.add_cascade(label='File', menu=file_menu)
#------------------------------------------------
edit_menu = tk.Menu(menuBar, tearoff=0)

edit_menu.add_command( label= 'Undo', command=None)
edit_menu.add_command( label= 'Redo', command=None)
edit_menu.add_separator()
edit_menu.add_command( label= 'Copy', command=None)
edit_menu.add_command( label= 'Cut', command=None)
edit_menu.add_command( label= 'Paste', command=None)

menuBar.add_cascade(label='Edit', menu=edit_menu)
#------------------------------------------------


root.config(menu=menuBar)




root.mainloop()