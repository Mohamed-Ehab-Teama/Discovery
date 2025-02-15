## Session 5: Scrollbar and Text Widget

   # 1- The Scrollbar widget in Tkinter allows users to scroll through content in widgets like Text, Listbox.
   
'''
Key Properties of Scrollbar:
   orient	      Defines the direction (tk.VERTICAL or tk.HORIZONTAL).
   command	      Links the scrollbar to a widget.
   set()	         Updates the scrollbar position when linked to a widget.
'''


'''
Attaching a Scrollbar to a Widget
   To connect a scrollbar to a widget (like Text), we use the yview() and yscrollcommand methods.

📌 Example Usage:
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

      command=text_widget.yview → Moves the text when the scrollbar is dragged.
      yscrollcommand=scrollbar.set → Updates scrollbar when text is scrolled.

'''


   # 2- The Text widget allows users to input and edit multi-line text.
   
'''
📌 Key Methods of Text Widget:
   .insert(index, text)	      Inserts text at a specific position.
   .get(start, end)	         Retrieves text from a range.
   .delete(start, end)	      Deletes text from a range.
   .see(index)	               Scrolls to a specific position.
   .config(wrap=tk.WORD)	   Ensures text wraps within the widget width.

📌 Example Usage:
   text_widget.insert(tk.END, "This is an example of a multi-line text widget.\n")

'''



   # ----------- Full Project ---------------
import tkinter as tk
from tkinter import scrolledtext, Menu

# Create the main window
root = tk.Tk()
root.title("Advanced Text Editor")
root.geometry("600x400")

# Create a Frame to hold the Text widget and Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a Scrollable Text Widget
text_widget = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), undo=True)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar and attach it to the Text widget
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Text widget to use the Scrollbar
text_widget.config(yscrollcommand=scrollbar.set)


# Create a Menu Bar
menu_bar = Menu(root)

# Add File Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="Edit", menu=file_menu)

# Display the Menu
root.config(menu=menu_bar)

# Run the Tkinter event loop
root.mainloop()
