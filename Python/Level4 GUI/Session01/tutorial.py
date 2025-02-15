'''
## Session 1: Introduction to GUI with Tkinter
### Objective:
- Understand what a GUI (Graphical User Interface) is.
- Learn about Tcl, Tk, and Tkinter.
- Understand the steps to create a Tkinter application.
- Explore basic Tkinter widgets (Button, Canvas).
- Create a simple **Login Form** with two labels, two entry fields, and a button.

### Explanation:
1. **What is a GUI?**
   - A GUI allows users to interact with a program using graphical elements like windows, buttons, and text fields instead of typing commands in a console.

2. **What are Tcl, Tk, and Tkinter?**
   - **Tcl (Tool Command Language)**: A scripting language used for rapid prototyping, scripting, and GUI applications.
   - **Tk**: A GUI toolkit originally created for Tcl but later adapted for many other languages, including Python.
   - **Tkinter**: The Python wrapper for the Tk GUI toolkit, making it easy to build GUI applications.

3. **Steps to Create a Tkinter App:**
   - Import the Tkinter module.
   - Create the main application window.
   - Add widgets (buttons, labels, text boxes, etc.).
   - Run the application event loop.

4. **Basic Tkinter Widgets:**
   - **Label**: Displays text in the GUI.
   - **Entry**: Allows user input.
   - **Button**: Performs an action when clicked.
   - **Canvas**: Used for drawing shapes and images.
   
'''
### Code: Creating a Simple Login Form
# python
import tkinter as tk

# Step 1: Create the main application window
root = tk.Tk()
root.title("Login Form")  # Set window title
root.geometry("300x200")  # Set window size

# Step 2: Add Labels and Entry Widgets
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")  # Hide password characters
entry_password.pack()

# Step 3: Add a Button
login_button = tk.Button(root, text="Login")
login_button.pack()

# Step 4: Run the application
root.mainloop()

'''

### Explanation of Code:
1. `tk.Tk()` creates the main application window.
2. `Label` is used to display text for "Username" and "Password".
3. `Entry` allows users to input text.
4. `Button` is used for submitting the form.
5. `mainloop()` runs the application, keeping the window open.

### Expected Output:
A simple GUI with:
- A "Username" field.
- A "Password" field (masked with `*`).
- A "Login" button.

'''
