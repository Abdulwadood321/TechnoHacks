import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def edit_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        new_task = task_entry.get()
        if new_task:
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position
window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create widgets
task_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add Task", command=add_task, width=20, height=1)
remove_button = tk.Button(root, text="Remove Task", command=remove_task, width=20, height=1)
edit_button = tk.Button(root, text="Edit Task", command=edit_task, width=20, height=1)
tasks_listbox = tk.Listbox(root)

# Place widgets on the grid
task_entry.grid(row=0, column=9, padx=10, pady=10)
add_button.grid(row=0, column=3, padx=10, pady=10)
remove_button.grid(row=1, column=3, padx=0, pady=0)
edit_button.grid(row=2, column=3, padx=1, pady=1)
tasks_listbox.grid(row=1, column=9, padx=10, pady=10)

# Start the main loop
root.mainloop()
