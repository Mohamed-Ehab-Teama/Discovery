# import tkinter as tk
# from tkinter import messagebox, simpledialog, ttk
# import time
# import threading

# # Predefined username and password for validation
# admin_username = "admin"
# admin_password = "1234"
# guest_username = "guest"
# guest_password = "123"

# # Timer functionality (to track time)
# class TaskTimer:
#     def __init__(self, label):
#         self.label = label
#         self._running = False
#         self.seconds = 0

#     def start(self):
#         self._running = True
#         threading.Thread(target=self._run).start()

#     def _run(self):
#         while self._running:
#             time.sleep(1)
#             self.seconds += 1
#             mins, secs = divmod(self.seconds, 60)
#             hours, mins = divmod(mins, 60)
#             self.label.config(text=f"{hours:02}:{mins:02}:{secs:02}")

#     def stop(self):
#         self._running = False

#     def reset(self):
#         self._running = False
#         self.seconds = 0
#         self.label.config(text="00:00:00")


# # Function to create the Study Management form (new window)
# def open_study_management():
#     study_window = tk.Toplevel(root)
#     study_window.title("Study Management")
#     study_window.geometry("500x400")

#     tasks = []

#     # Add Task
#     def add_task():
#         task_name = simpledialog.askstring("New Task", "Enter task name:")
#         if task_name:
#             tasks.append({"name": task_name, "timer": TaskTimer(task_time_labels[len(tasks)])})
#             task_listbox.insert(tk.END, task_name)
#             start_buttons[len(tasks) - 1].config(state="normal")
#             stop_buttons[len(tasks) - 1].config(state="normal")

#     # Create a frame for task management
#     task_frame = tk.Frame(study_window)
#     task_frame.pack(pady=10)

#     # Listbox to display tasks
#     task_listbox = tk.Listbox(task_frame, height=10, width=30)
#     task_listbox.grid(row=0, column=0, rowspan=10, padx=10)

#     # Labels for displaying task timers
#     task_time_labels = [tk.Label(task_frame, text="00:00:00") for _ in range(10)]
#     for i, label in enumerate(task_time_labels):
#         label.grid(row=i, column=1)

#     # Buttons to start/stop tracking time
#     start_buttons = [tk.Button(task_frame, text="Start", state="disabled") for _ in range(10)]
#     stop_buttons = [tk.Button(task_frame, text="Stop", state="disabled") for _ in range(10)]
    
#     # Attach the start and stop buttons to tasks
#     def start_task(i):
#         tasks[i]["timer"].start()

#     def stop_task(i):
#         tasks[i]["timer"].stop()

#     for i, (start_button, stop_button) in enumerate(zip(start_buttons, stop_buttons)):
#         start_button.config(command=lambda i=i: start_task(i))
#         stop_button.config(command=lambda i=i: stop_task(i))
#         start_button.grid(row=i, column=2, padx=5)
#         stop_button.grid(row=i, column=3, padx=5)

#     # Add New Task button
#     add_task_button = tk.Button(study_window, text="Add Task", command=add_task)
#     add_task_button.pack(pady=20)

# # Function to open the new form after successful login
# def open_dashboard():
#     dashboard = tk.Toplevel(root)
#     dashboard.title("Dashboard")
#     dashboard.geometry("400x300")

#     # Create a menu bar
#     menubar = tk.Menu(dashboard)
    
#     # Add the "File" menu
#     file_menu = tk.Menu(menubar, tearoff=0)
#     file_menu.add_command(label="Study Management", command=open_study_management)  # Submenu
#     file_menu.add_separator()
#     file_menu.add_command(label="Exit", command=dashboard.quit)  # Exit the form

#     # Add File menu to the menubar
#     menubar.add_cascade(label="File", menu=file_menu)
#     dashboard.config(menu=menubar)
    
#     # Add a welcome label to the dashboard
#     welcome_label = tk.Label(dashboard, text="Welcome to the Dashboard!", font=('Arial', 16))
#     welcome_label.pack(pady=20)

# # Function to validate the username and password based on the selected role
# def validate_login():
#     username = username_entry.get()
#     password = password_entry.get()
#     user_type = user_role.get()  # Get the selected role (Admin or Guest)
    
#     if user_type == "Admin":
#         if username == admin_username and password == admin_password:
#             messagebox.showinfo("Login Success", "Welcome Admin, you have successfully logged in!")
#             open_dashboard()
#         else:
#             messagebox.showerror("Login Failed", "Invalid Admin credentials. Please try again.")
#     elif user_type == "Guest":
#         if username == guest_username and password == guest_password:
#             messagebox.showinfo("Login Success", "Welcome Guest, you have successfully logged in!")
#             open_dashboard()
#         else:
#             messagebox.showerror("Login Failed", "Invalid Guest credentials. Please try again.")

# # Create the main window (root window)
# root = tk.Tk()
# root.title("Login Form")
# root.geometry("300x200")  # Adjusted size to fit the radio buttons

# # Create a label for Username
# username_label = tk.Label(root, text="Username:")
# username_label.grid(row=0, column=0, padx=10, pady=10)

# # Create an entry widget for Username
# username_entry = tk.Entry(root)
# username_entry.grid(row=0, column=1, padx=10, pady=10)

# # Create a label for Password
# password_label = tk.Label(root, text="Password:")
# password_label.grid(row=1, column=0, padx=10, pady=10)

# # Create an entry widget for Password, use show='*' to hide the characters
# password_entry = tk.Entry(root, show='*')
# password_entry.grid(row=1, column=1, padx=10, pady=10)

# # Create radio buttons to choose between Admin and Guest
# user_role = tk.StringVar(value="Admin")  # Default value is Admin

# admin_radio = tk.Radiobutton(root, text="Admin", variable=user_role, value="Admin")
# admin_radio.grid(row=2, column=0, padx=10, pady=10)

# guest_radio = tk.Radiobutton(root, text="Guest", variable=user_role, value="Guest")
# guest_radio.grid(row=2, column=1, padx=10, pady=10)

# # Create a login button and attach the validation function
# login_button = tk.Button(root, text="Login", command=validate_login)
# login_button.grid(row=3, column=1, pady=10)

# # Start the Tkinter event loop
# root.mainloop()


#-----------------------------------------------------------------------------------------


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

