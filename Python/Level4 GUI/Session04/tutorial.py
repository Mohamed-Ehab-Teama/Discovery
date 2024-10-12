# List Box Widget
# Menu Widget

import tkinter as tk

root = tk.Tk()

root.geometry('800x650')
root.title('Session 04 GUI')


listBox = tk.Listbox(
    root,
    width=60,
    bg='gray',
    fg='blue',
    highlightcolor= 'yellow',
    activestyle='underline',     # none - underline - dotbox
)
listBox.pack(pady=20)

listBox.insert(1, 'Element 01')
listBox.insert(2, 'Element 02')
listBox.insert(3, 'Element 03')
listBox.insert(4, 'Element 04')
listBox.insert(5, 'Element 05')
listBox.insert(6, 'Element 06')
listBox.insert(7, 'Element 07')

# listBox.delete(2)     # index
# listBox.delete(2,5)   # Range




menuBar = tk.Menu(root)     # create Menu Bar
root.config(menu= menuBar)

file_m = tk.Menu(menuBar, tearoff = 0)      # add first Menu
menuBar.add_cascade(label = 'File', menu = file_m)

file_m.add_command( label= 'New File', command= None )      # add Menu Commands
file_m.add_command( label= 'Open', command= None )
file_m.add_command( label= 'Save', command= None )
file_m.add_separator()
file_m.add_command( label= 'Exit', command= None)



root.mainloop()