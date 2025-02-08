# List Box Widget
    # The Listbox widget allows users to select one or more items from a list.
import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox
listbox = tk.Listbox(root)
listbox.pack(pady=10)

# Add items to the Listbox
items = ["Python", "Java", "C++", "JavaScript"]
for item in items:
    listbox.insert(tk.END, item)

root.mainloop()

# insert(index, item) → Adds an item
# delete(index) → Removes an item
# get(index) → Retrieves the selected item
# curselection() → Returns the index of the selected item


# ---------------- ======================= -------------------- ====================

# Menu widget
    # The Menu widget allows adding dropdown menus to an application.

import tkinter as tk

root = tk.Tk()
root.title("Menu Example")

# Create a Menu bar
menu_bar = tk.Menu(root)

# Create a File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New File")
file_menu.add_command(label="Open")
file_menu.add_command(label="Exit", command=root.quit)

# Add File Menu to Menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()

# add_command(label, command=function) → Adds a menu item.
# add_separator() → Adds a separator line.
# add_cascade(label, menu=submenu) → Adds a submenu.
