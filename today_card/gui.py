import tkinter as tk
from tkinter import messagebox
from task_manager import save_tasks, load_tasks
from utils import set_date
from task_manager import TaskManager

class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("The Today Card")
        root.geometry("400x250")
        root.resizable(False, False)
        root.configure(bg="#FFFAFA")  # Snow color for a paper white look

        self.task_manager = TaskManager()

        self.frame = tk.Frame(root, bg="#FFFAFA", relief="ridge", bd=2)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=380, height=230)

        today = set_date()
        self.header = tk.Label(root, text= today, font=("Helvetica", 16, "bold"), bg="#FFFAFA")
        self.header.pack(pady=10)

        self.task_area = tk.Text(self.frame, height=6, width=42, bg="#FFFAFA", wrap="word", font=("Helvetica", 12), bd=0)
        self.task_area.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(self.frame, bg="#FFF8DC")
        self.button_frame.pack(pady=10)

        self.save_button = tk.Button(self.button_frame, text="Save Tasks", command=lambda: save_tasks(self.task_area), bg="#FFD700", font=("Helvetica", 10)) #command=save_tasks
        self.save_button.pack(side="left", padx=5)

        self.load_button = tk.Button(self.button_frame, text="Load Tasks", command=lambda: load_tasks(self.task_area), bg="#32CD32", font=("Helvetica", 10)) # command=load_tasks,
        self.load_button.pack(side="left", padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=lambda: self.task_area.delete("1.0", tk.END), bg="#FF6347", font=("Helvetica", 10))
        self.clear_button.pack(side="left", padx=5)
        
        # settings_button = tk.Button(button_frame, text="Settings",bg="#F0FF00", font=("Helvetica", 10))
        # settings_button.pack(side="left", padx=5)
        
        # flip_card_button = tk.Button(button_frame, text="Flip Card", bg="#AA66FF", font=("Helvetica", 10))
        # flip_card_button.pack(side="left", padx=5)

        # Add footer - currently not showing
        self.footer = tk.Label(root, text="Make it a great day!", font=("Helvetica", 10), bg="#FFFAFA")
        self.footer.pack(side="bottom", pady=5)


    def save_tasks(self):
            """Saves tasks from the text area."""
            tasks_text = self.task_area.get("1.0", "end")
            self.task_manager.save_tasks(tasks_text)

    def load_tasks(self):
        """Loads tasks from the database into the text area."""
        self.task_area.delete("1.0", "end")  # Clear existing tasks
        tasks = self.task_manager.load_tasks()
        for task in tasks:
            self.task_area.insert("end", f" - {task}\n")

    def clear_tasks(self):
        """Clears the task area."""
        self.task_area.delete("1.0", "end")
