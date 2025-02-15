'''
## Session 2: Working with Entry, Label, Frame, and Buttons

### Objective:
- Learn how to use the `Entry` widget and its parameters.
- Understand the `Label` widget and how to style it.
- Explore the `Frame` widget for organizing content.
- Learn more about `Button` widgets and their functions.
- Add validation to the login form.

### Explanation:

1. **Entry Widget:**
   - Used to take input from the user.
   - Can have attributes like `width`, `show` (for password fields), and `textvariable` (to store input).

2. **Label Widget:**
   - Displays static text in the GUI.
   - Can be customized with `font`, `fg` (foreground color), and `bg` (background color).

3. **Frame Widget:**
   - Acts as a container to group related widgets together.
   - Useful for layout management.

4. **Button Widget:**
   - Performs an action when clicked.
   - Can be linked to a function using the `command` parameter.

5. **Validating Login Form:**
   - Check if the user has entered a username and password.
   - Display a message if the fields are empty.

'''

### Code: Enhanced Login Form with Validation
import tkinter as tk
from tkinter import messagebox

# Function to validate login
def validate_login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Create a frame for better layout
frame = tk.Frame(root)
frame.pack(pady=20)

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

# Login button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack(pady=10)

# Run the application
root.mainloop()


'''

### Explanation of Code:
1. **Creating the GUI:** The main window is created using `Tk()` and given a title and size.
2. **Using a Frame:** A `Frame` is used to structure the layout better.
3. **Labels and Entry Fields:** Widgets are placed in a grid layout inside the frame.
4. **Login Validation:**
   - The `validate_login()` function checks the entered username and password.
   - If correct, a success message is shown; otherwise, an error message appears.
5. **Messagebox:** Used to show alerts or messages to the user.

### Expected Output:
A login form with:
- A username and password field.
- A "Login" button that validates credentials.
- A success or error popup message based on the input.

This session introduces basic event handling in Tkinter. Let me know if you need any modifications! 🚀

'''