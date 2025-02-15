'''
## Session 4: Listbox and Menu Widgets

### Objective:
- Learn about the `Listbox` widget and its usage.
- Understand the `Menu` widget and how to create menus in Tkinter.
- Create a new form after logging in, with a file menu and a submenu to add another form.

### Explanation:

1. **Listbox Widget:**
   - Used to display a list of items.
   - Allows users to select one or multiple items.
   
2. **Menu Widget:**
   - Used to create dropdown menus, context menus, or pop-up menus.
   - Provides a way to organize commands in a structured manner.

3. **Building a File Menu:**
   - Create a menu bar with a "File" menu.
   - Add options like "New Form" to navigate to another form.

4. **Adding a New Form After Login:**
   - After successful login, open a new window.
   - Implement a file menu with an option to open another form (Study Management form in the next session).

'''

### Code: Enhanced Login Form with Menu and Listbox
import tkinter as tk
from tkinter import messagebox

# Function to open new form
def open_new_form():
    new_window = tk.Toplevel(root)
    new_window.title("New Form")
    new_window.geometry("300x200")
    tk.Label(new_window, text="Welcome to the New Form!", font=("Arial", 12)).pack(pady=20)

# Function to validate login and open main dashboard
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    role = role_var.get()
    
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", f"Welcome {username}! Role: {role}")
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to create main dashboard after login
def open_dashboard():
    global root
    root.destroy()
    
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")
    
    # Create menu bar
    menubar = tk.Menu(dashboard)
    
    # File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New Form", command=open_new_form)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=dashboard.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    
    dashboard.config(menu=menubar)
    
    # Listbox for selection
    tk.Label(dashboard, text="Select a Subject:").pack(pady=5)
    subjects_listbox = tk.Listbox(dashboard)
    subjects_listbox.pack(pady=5)
    subjects_listbox.insert(1, "Mathematics")
    subjects_listbox.insert(2, "Science")
    subjects_listbox.insert(3, "History")
    subjects_listbox.insert(4, "Programming")
    
    dashboard.mainloop()

# Create main login window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

# Create a frame for better layout
frame = tk.Frame(root)
frame.pack(pady=10)

# Username label and entry
label_username = tk.Label(frame, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5)
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Password label and entry
label_password = tk.Label(frame, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Role selection
role_var = tk.StringVar(value="Guest")  # Default role
label_role = tk.Label(frame, text="Select Role:")
label_role.grid(row=2, column=0, padx=5, pady=5)
radio_admin = tk.Radiobutton(frame, text="Admin", variable=role_var, value="Admin")
radio_admin.grid(row=2, column=1, padx=5, pady=2)
radio_guest = tk.Radiobutton(frame, text="Guest", variable=role_var, value="Guest")
radio_guest.grid(row=3, column=1, padx=5, pady=2)

# Login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack(pady=10)

# Run the application
root.mainloop()


'''

### Explanation of Code:
1. **Creating the Login Form:**
   - Username and password fields.
   - Role selection using radio buttons.
   - A login button that validates credentials.

2. **Adding a Menu:**
   - A file menu with options to open a new form and exit the app.

3. **Adding a Listbox:**
   - Displays a list of subjects.
   - Users can select a subject from the list.

4. **Opening a New Form After Login:**
   - Upon successful login, the main login window closes, and a dashboard opens.
   - The dashboard contains a menu bar and a listbox.
   - The "File" menu allows the user to open another form.

### Expected Output:
- A login form with username, password, role selection, and login button.
- After successful login, a dashboard with:
  - A file menu with "New Form" and "Exit" options.
  - A listbox containing different subjects.

'''