import tkinter as tk
from tkinter import ttk  # Import ttk 
from tkinter import messagebox
from styles import configure_styles

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title(".")

        self.tasks = []

        # Title Label of Task.
        self.title_label = tk.Label(self.root, text="ToDo List", font=("Helvetica", 20, "bold"), pady=10)
        self.title_label.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Entry with a placeholder text....
        self.entry_var = tk.StringVar()
        self.entry_var.set("Enter your task here...")
        self.entry = tk.Entry(self.root, width=50, textvariable=self.entry_var, font=("Helvetica", 12), bd=0, highlightthickness=0)
        self.entry.pack(pady=10)

        # Bind events to handle entry focus
        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_focus_out)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Config-styles
        configure_styles()

        self.add_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task, style='TButton')
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = ttk.Button(self.button_frame, text="Complete Task", command=self.complete_task, style='TButton')
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task, style='TButton')
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def on_entry_click(self, event):
        """Function to handle click events on entry widget."""
        if self.entry.get() == "Enter your task here...":
            self.entry.delete(0, tk.END)  # delete all the text in the entry
            self.entry.config(fg='black')  # change text color to black

    def on_focus_out(self, event):
        """Function to handle focus out event on entry widget."""
        if self.entry.get() == '':
            self.entry.insert(0, "Enter your task here...")
            self.entry.config(fg='grey')  # change text color to grey

    def add_task(self):
        task = self.entry.get()
        if task and task != "Enter your task here...":
            self.tasks.append({"description": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
            self.entry_var.set("Enter your task here...")  # reset placeholder text
            self.entry.config(fg='grey')  # set text color to grey
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            self.task_listbox.insert(tk.END, f"{i + 1}. {task['description']} [{status}]")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")
