import tkinter as tk
from tkinter import messagebox

# Predefined username and password
valid_username = "user"
valid_password = "password"

# Function to validate login
def validate_login():
    name = username_entry.get()
    password = password_entry.get()
    
    if name == valid_username and password == valid_password:
        messagebox.showinfo('Success', "Login Successfully")
        open_new_window()
    else:
        messagebox.showerror('Failure', 'Name or Email is incorrect')


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.geometry('300x250')
    new_window.title('Task Manager')

    def add_task():
        task = task_entry.get()
        if task:
            task_list.insert(tk.END, task)
        else:
            messagebox.showerror('Empty Task', 'You must write your task')
        
    
    add_label = tk.Label(new_window, text='Add your Task:')
    add_label.pack()
    
    task_entry = tk.Entry(new_window)
    task_entry.pack()
    
    add_btn = tk.Button(new_window, text='Add Task', command=add_task)
    add_btn.pack()
    
    task_list = tk.Listbox(new_window)
    task_list.pack(fill='both', padx=2, pady=2)


# Main window (root)
root = tk.Tk()
root.title("Login Form")
root.geometry("300x150")

# Username and Password labels and entries
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.grid(row=2, column=1, pady=10)

# Start the Tkinter loop
root.mainloop()

