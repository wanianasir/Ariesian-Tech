import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    completed INTEGER NOT NULL
)
''')
conn.commit()

# Application class for the To-Do List Manager
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("400x400")
        
        # Frame for the task list
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Scrollbar for the task list
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, height=10, width=40, selectmode=tk.SINGLE, yscrollcommand=self.scrollbar.set)
        self.task_listbox.pack()

        # Connect the scrollbar to the listbox
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry widget for task input
        self.task_entry = tk.Entry(self.root, width=35)
        self.task_entry.pack(pady=10)

        # Buttons for Add, Edit, and Delete tasks
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        # Load tasks from the database when the app starts
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the SQLite database into the listbox."""
        self.task_listbox.delete(0, tk.END)
        cursor.execute("SELECT id, description, completed FROM tasks")
        tasks = cursor.fetchall()
        for task in tasks:
            task_str = task[1] + (" [COMPLETED]" if task[2] else "")
            self.task_listbox.insert(tk.END, task_str)

    def add_task(self):
        """Add a new task to the database and listbox."""
        task = self.task_entry.get()
        if task:
            cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (task, 0))
            conn.commit()
            self.load_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def edit_task(self):
        """Edit the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)

            if " [COMPLETED]" in selected_task:
                task_desc = selected_task.replace(" [COMPLETED]", "")
            else:
                task_desc = selected_task

            new_task = self.task_entry.get()
            if new_task:
                task_id = cursor.execute("SELECT id FROM tasks WHERE description = ?", (task_desc,)).fetchone()[0]
                cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_task, task_id))
                conn.commit()
                self.load_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task description.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def delete_task(self):
        """Delete the selected task from the database and listbox."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)

            if " [COMPLETED]" in selected_task:
                task_desc = selected_task.replace(" [COMPLETED]", "")
            else:
                task_desc = selected_task

            task_id = cursor.execute("SELECT id FROM tasks WHERE description = ?", (task_desc,)).fetchone()[0]
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_completed(self):
        """Mark the selected task as completed."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_index)

            if " [COMPLETED]" in selected_task:
                task_desc = selected_task.replace(" [COMPLETED]", "")
            else:
                task_desc = selected_task

            task_id = cursor.execute("SELECT id FROM tasks WHERE description = ?", (task_desc,)).fetchone()[0]
            cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
            conn.commit()
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")


# Create the main window
root = tk.Tk()

# Instantiate the TodoApp
app = TodoApp(root)

# Start the application
root.mainloop()

# Close the database connection when the app exits
conn.close()

