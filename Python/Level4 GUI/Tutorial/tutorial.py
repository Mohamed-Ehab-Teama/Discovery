'''
## Python GUI Basic (Desktop App) Course

### Session 1: Introduction to Tkinter and GUI
#### Topics Covered:
- What are Tcl, Tk, and Tkinter?
- Steps to create a Tkinter app.
- Introduction to Tkinter Widgets.
- Creating a simple login form.

#### Code:
'''
import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login").pack()

root.mainloop()

# -----------------------------------------------------------------
'''

### Session 2: Entry, Label, Frame, and Buttons
#### Topics Covered:
- Understanding Entry, Label, Frame, and Button widgets.
- Using these widgets to create a functional login form with validation.


'''
#### Code:
import tkinter as tk
from tkinter import messagebox

def validate_login():
    if username_entry.get() == "admin" and password_entry.get() == "1234":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1)

tk.Label(frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=validate_login).pack()

root.mainloop()

# -----------------------------------------------------------------

'''
### Session 3: Message, Radio, and Check Buttons
#### Topics Covered:
- Using Message, Radio Buttons, and Check Buttons.
- Enhancing the login form with an admin/guest option.
'''

#### Code:
import tkinter as tk

def show_selection():
    print("Role selected:", role_var.get())

root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

role_var = tk.StringVar(value="Guest")
tk.Radiobutton(root, text="Admin", variable=role_var, value="Admin").pack()
tk.Radiobutton(root, text="Guest", variable=role_var, value="Guest").pack()

tk.Button(root, text="Login", command=show_selection).pack()

root.mainloop()


# -----------------------------------------------------------------

'''
### Session 4: Listbox and Menu
#### Topics Covered:
- Creating a menu with a submenu.
- Adding a listbox for options.
- Navigating between forms.
'''
#### Code:

import tkinter as tk

def open_new_form():
    new_window = tk.Toplevel(root)
    new_window.title("New Form")
    new_window.geometry("300x200")
    tk.Label(new_window, text="Welcome to the new form!").pack()

root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open New Form", command=open_new_form)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

tk.Label(root, text="Select an option:").pack()
listbox = tk.Listbox(root)
listbox.pack()
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")

root.mainloop()


# -----------------------------------------------------------------

'''
### Session 5: Scrollbar and Text Widget
#### Topics Covered:
- Adding a text area with a scrollbar.
- Creating a simple text editor with a save function.
'''

#### Code:
import tkinter as tk
from tkinter import filedialog

def save_text():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        file.write(text_area.get("1.0", tk.END))
        file.close()

root = tk.Tk()
root.title("Text Editor")
root.geometry("400x300")

text_area = tk.Text(root, wrap="word")
scrollbar = tk.Scrollbar(root, command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
text_area.pack(expand=True, fill="both")

tk.Button(root, text="Save", command=save_text).pack()

root.mainloop()


# -----------------------------------------------------------------

'''
### Session 6: Completing the Study Management App
#### Topics Covered:
- Implementing a Study Timer.
- Managing a task list.

'''

#### Code:
import tkinter as tk

class StudyManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Management App")
        self.root.geometry("500x400")

        self.time_left = 1500
        self.running = False

        self.timer_label = tk.Label(root, text=self.format_time(), font=("Arial", 20))
        self.timer_label.pack()

        tk.Button(root, text="Start", command=self.start_timer).pack()
        tk.Button(root, text="Pause", command=self.pause_timer).pack()
        tk.Button(root, text="Reset", command=self.reset_timer).pack()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()
        tk.Button(root, text="Add Task", command=self.add_task).pack()
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack()
        tk.Button(root, text="Remove Task", command=self.remove_task).pack()

    def format_time(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        return f"{minutes:02}:{seconds:02}"

    def start_timer(self):
        self.running = True
        self.countdown()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 1500
        self.timer_label.config(text=self.format_time())

    def countdown(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=self.format_time())
            self.root.after(1000, self.countdown)

root = tk.Tk()
app = StudyManager(root)
root.mainloop()


# -----------------------------------------------------------------
