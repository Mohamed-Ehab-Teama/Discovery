import tkinter as tk
from tkinter import messagebox

# Predefined username and password
valid_username = "user"
valid_password = "password"

# Function to validate login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Login Success", "Login successful!")
        open_task_manager()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials, please try again.")

# Function to create the task manager window
def open_task_manager():
    task_window = tk.Toplevel(root)
    task_window.title("Task Manager")
    task_window.geometry("300x200")

    # Function to add tasks
    def add_task():
        task = task_entry.get()
        if task:
            task_listbox.insert(tk.END, task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    # Task entry and add button
    task_label = tk.Label(task_window, text="New Task:")
    task_label.pack(pady=5)

    task_entry = tk.Entry(task_window)
    task_entry.pack(pady=5)

    add_button = tk.Button(task_window, text="Add Task", command=add_task)
    add_button.pack(pady=5)

    # Listbox to show tasks
    task_listbox = tk.Listbox(task_window)
    task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

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

