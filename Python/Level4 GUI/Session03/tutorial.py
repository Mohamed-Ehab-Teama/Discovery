'''
## Session 3: Working with Message, Radio Button, and Check Button Widgets

### Objective:
- Learn about the `Message` widget and its usage.
- Understand `RadioButton` for selecting one option from multiple choices.
- Learn how to use `CheckButton` for selecting multiple options.
- Add a radio button to the login form for selecting user roles (Admin or Guest).

### Explanation:

1. **Message Widget:**
   - Used to display long text messages in the GUI.
   - Similar to `Label` but automatically wraps text.

2. **Radio Button Widget:**
   - Allows the user to select one option from a predefined list.
   - Uses a `tk.StringVar()` to keep track of the selected value.

3. **Check Button Widget:**
   - Allows users to select multiple options.
   - Uses a `tk.IntVar()` (1 for checked, 0 for unchecked) to store the state.

4. **Adding Role Selection to the Login Form:**
   - Use `RadioButton` to choose between "Admin" and "Guest" roles.
   - Display the selected role after login.

'''

### Code: Enhanced Login Form with Role Selection
import tkinter as tk
from tkinter import messagebox

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    role = role_var.get()
    
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", f"Welcome {username}! Role: {role}")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
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
1. **Creating the GUI:** The main window is created with a title and size.
2. **Username & Password Fields:** Used to enter credentials.
3. **Role Selection using Radio Buttons:**
   - Users can choose between "Admin" and "Guest" roles.
   - Uses `tk.StringVar()` to track selection.
4. **Login Validation:**
   - If credentials are correct, it displays a success message with the selected role.
   - If incorrect, it shows an error message.

### Expected Output:
A login form with:
- Username and password fields.
- Radio buttons for selecting user roles.
- A login button that validates credentials and displays the selected role.

This session introduces the use of radio buttons and how to capture user selections. Let me know if you need any modifications! 🚀
'''