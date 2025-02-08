from tkinter import *
import tkinter as tk

root = tk.Tk()

root.geometry("600x400")
root.title(" Python - GUI - Tkinter - Session 04 ")


# Create ListBox
# select_country = tk.Listbox(root, width=10, height=5)
# select_country.pack()

# select_country10 = tk.Listbox(root)
# select_country10.pack()

# select_country.insert(tk.END , "Egypt")
# select_country.insert(tk.END , "Sudan")
# select_country.insert(tk.END , "Russia")
# select_country.delete(2)
# print( select_country.get(2) )

# all_countries = ['Qatar', 'Saudi Arabia', 'IraQ', 'Syria', 'Plestine']
# for i in all_countries:
#     select_country10.insert( tk.END, i )


# Create Menu Bar
menu_bar = tk.Menu(root)

# Create file Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New File")
file_menu.add_command(label="New Window")
file_menu.add_separator()
file_menu.add_command(label="New Folder")
file_menu.add_command(label="Exit")

# create Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add File Menu to Menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
# Add Edit Menu to Menu bar
menu_bar.add_cascade(label='Edit', menu=edit_menu)

root.config(menu=menu_bar)



root.mainloop()