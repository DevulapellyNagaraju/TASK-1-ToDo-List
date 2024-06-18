import tkinter as tk
from todo_app import TodoApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()