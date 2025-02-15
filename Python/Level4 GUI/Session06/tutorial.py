'''
## Session 6: Completing the Study Management App

### Objective:
- Finalize the study management desktop application.
- Implement features to manage study time.
- Improve the UI with additional functionalities.

### Features to Implement:
1. **Main Dashboard:**
   - Welcome message with user details.
   - Navigation buttons for different sections.
2. **Study Timer:**
   - Start, Pause, and Reset buttons.
   - A label to display the countdown timer.
3. **Task List:**
   - An entry field to add study tasks.
   - A listbox to display added tasks.
   - Buttons to remove selected tasks.


'''

### Code: Study Management App
import tkinter as tk
from tkinter import messagebox
import time

class StudyManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Management App")
        self.root.geometry("500x400")

        # Timer Variables
        self.time_left = 1500  # 25 minutes default
        self.running = False
        
        # Study Timer Label
        self.timer_label = tk.Label(root, text=self.format_time(), font=("Arial", 20))
        self.timer_label.pack(pady=10)
        
        # Timer Control Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_timer)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Task List
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        
        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack()

    def format_time(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        return f"{minutes:02}:{seconds:02}"
    
    def start_timer(self):
        if not self.running:
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
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
    
    def remove_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            self.task_listbox.delete(selected_task)

# Run the Application
root = tk.Tk()
app = StudyManager(root)
root.mainloop()

'''

### Explanation of Code:
1. **Study Timer Implementation:**
   - Displays a countdown timer with Start, Pause, and Reset functionalities.
2. **Task Management:**
   - Allows users to add and remove study tasks.
3. **User Interface Enhancements:**
   - Organized layout with buttons and listbox for ease of use.

### Expected Output:
- A functional study management app with a timer and task list.
- Users can track study time and maintain a task list.

'''