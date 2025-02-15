import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('600x600')
root.title('Session 05')


# create Frame
frame01 = tk.Frame( root, bg='orange' )
frame01.pack(pady=10, fill=tk.BOTH, expand=True)

# Create Text Widget
text_widget01 = tk.Text( frame01, wrap=tk.WORD, font=(20) )
text_widget01.pack(fill=tk.BOTH, expand=True)

# Create Scroll Bar
scroll_text = tk.Scrollbar(text_widget01, orient='vertical', command=text_widget01.yview )
scroll_text.pack( side='right', fill=tk.Y )

# Configure the Text widget to use the Scrollbar
text_widget01.config( yscrollcommand=scroll_text.set )



root.mainloop()