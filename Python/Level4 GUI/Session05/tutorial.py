# To use the scrollbar widget, you need to:
    # First, create a scrollbar widget.
    # Second, link the scrollbar with a scrollable widget.

# padx & pady => Margin
# ipadx & ipady => padding

# T = Text(root, bg, fg, bd, height, width, font, ..)
# w = Scrollbar(master, options) 

# ------------------------------------------------------

import tkinter as tk

root = tk.Tk()

root.geometry('500x450')
root.title('Session 05 GUI')

label1 = tk.Label(root, text='Enter Your Text : ')
label1.pack()


frame = tk.Frame(root, bg='white')
# frame.pack( padx=20, pady=20, ipadx=20, ipady=20 )
frame.pack()

scroll = tk.Scrollbar(frame, orient='vertical')
scroll.pack( side='right', fill='y' )

T = tk.Text(frame, width= 40, height=10, yscrollcommand= scroll.set)
T.pack(ipadx=10, ipady=10, padx=10, pady=10)

scroll.config( command= T.yview )


root.mainloop()



# ------------------------------------------------------


# import tkinter as tk

# root = tk.Tk()

# root.geometry('450x250')
# root.title('Session 05 Tutorial')

# lab01 = tk.Label(root, text= 'Enter You Text Here : ', font='50')
# lab01.pack()

# scroll = tk.Scrollbar(root)
# scroll.pack( side='right', fill='both')

# mylist = tk.Listbox(root, yscrollcommand=scroll.set)

# for i in range(1,25):
#     mylist.insert(i, 'This is Line' + str(i) + '\n')

# mylist.pack( side='left', fill='both')

# scroll.config( command= mylist.yview )

# root.mainloop()

# ------------------------------------------------------


# # Create Text Widget
# text = tk.Text(root, height=5, width=20, wrap='none')
# text.pack()

# # Create ScrollBar
# scrollb = tk.Scrollbar(root, orient='horizontal', command=text.xview)
# scrollb.pack()

# # Communicate Back to the ScrollBar
# text['xscrollcommand'] = scrollb.set


# ------------------------------------------------------


# Cretae label
# label1 = tk.Label(root, text= "Enter You Text here: ")
# label1.pack()

# Create Scroll Bar
# scroll = tk.Scrollbar(root, orient='vertical')
# scroll.pack( side='right', fill='y' )

# Create Text Widget
# text = tk.Text(root, height=3, wrap='none', yscrollcommand= scroll.set)
# text.pack( padx=10, pady=5, ipadx=5, ipady=5 )

# Create List Widget
# myList = tk.Listbox(root)
# myList.pack()



# Communicate Back to the ScrollBar
# text['yscrollcommand'] = scroll.set

# ------------------------------------------------------
