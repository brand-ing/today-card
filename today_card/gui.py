import tkinter as tk
from tkinter import messagebox, simpledialog
from utils import set_date
from task_manager import TaskManager

class gui:
    def __init__(self, root):
        self.root = root
        self.task_manager = TaskManager()

        self.root.title("The Today Card")
        root.geometry("400x260")
        root.resizable(False, False)
        root.configure(bg="#FFFAFA")  # Snow color for a paper white look


        self.frame = tk.Frame(root, bg="#FFFAFA", relief="ridge", bd=2)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=260)

        today = set_date()
        self.header = tk.Label(root, text= today, font=("Helvetica", 16, "bold"), bg="#FFFAFA")
        self.header.pack(pady=10)

        # Create a Canvas for Lined Paper Look
        self.canvas = tk.Canvas(self.frame, width=380, height=120, bg="#FDF5E6", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Draw horizontal lines (Blue lines like notebook paper)
        for i in range(1, 7):
            y = i * 20
            self.canvas.create_line(10, y, 380, y, fill="#A3C1DA", width=1)  # Light blue


        # Draw vertical red margin line (like an index card)
        self.canvas.create_line(40, 0, 40, 120, fill="red", width=2)

        self.task_area = tk.Text(
            self.canvas, height=6, width=42, wrap="word", font=("Helvetica", 12), 
            bg="#FDF5E6", fg="black", highlightthickness=0, borderwidth=0
        )
        self.task_area.config(state="disabled")

        # Scrollbar for Task Area
        self.scrollbar = tk.Scrollbar(self.frame, command=self.task_area.yview)
        self.task_area.config(yscrollcommand=self.scrollbar.set)


        self.button_frame = tk.Frame(self.frame, bg="#FFF8DC")
        self.button_frame.pack(pady=10)

        self.save_button = tk.Button(self.button_frame, text="Save Tasks", command=lambda: self.save_tasks(), bg="#FFD700", font=("Helvetica", 10)) #command=save_tasks
        self.save_button.pack(side="left", padx=5)

        self.load_button = tk.Button(self.button_frame, text="Load Tasks", command=lambda: self.load_tasks(), bg="#32CD32", font=("Helvetica", 10)) # command=load_tasks,
        self.load_button.pack(side="left", padx=5)

        self.add_task_button = tk.Button(self.button_frame, text="Add Tasks", command=lambda: self.add_tasks(), bg="#69420A",font=("Helvetica", 10)) # command=add_task,
        self.add_task_button.pack(side="left", padx=5)

        # self.clear_button = tk.Button(self.button_frame, text="Clear", command=lambda: self.task_area.delete("1.0", tk.END), bg="#FF6347", font=("Helvetica", 10))
        # self.clear_button.pack(side="left", padx=5)
        
        # settings_button = tk.Button(self.button_frame, text="Settings",bg="#F0FF00", font=("Helvetica", 10))
        # settings_button.pack(side="left", padx=5)
        
        # flip_card_button = tk.Button(self.button_frame, text="Flip Card", bg="#AA66FF", font=("Helvetica", 10))
        # flip_card_button.pack(side="left", padx=5)

        # Add footer - currently not showing
        self.footer = tk.Label(root, text="Make it a great day!", font=("Helvetica", 10), bg="#FFFAFA")
        self.footer.pack(side="bottom", pady=5)

        # Load
        self.load_tasks()
    

    def add_tasks(self):
        task_name = simpledialog.askstring("Add Task", "Enter the task name:")
        if task_name:
            success = self.task_manager.add_tasks(task_name)
            if success:
                self.update_task_area()


    def load_tasks(self):
        self.task_area.config(state="normal")
        self.task_area.delete(1.0, tk.END)  # Clear previous tasks

        tasks = self.task_manager.load_tasks()
        if not tasks:
            self.task_area.insert(tk.END, "No tasks for today.\n")
            self.task_area.config(state="disabled")
            return

        for index, task in enumerate(tasks, start=1):
            status = "✔" if task.completed else "✘"
            task_text = f"{index} Task: {task.task_name}  |  {task.points} pts  |  Completed: {status}\n"
            self.task_display.insert(tk.END, task_text)
        self.task_area.config(state="disabled")


    def save_tasks(self):
        tasks_text = self.task_area.get("1.0", tk.END).strip()
        if not tasks_text or tasks_text == "No tasks for today.":
            messagebox.showwarning("Warning", "No tasks to save.")
            return

        task_lines = tasks_text.split("\n")
        for line in task_lines:
            if line.strip():
                parts = line.split(" | ")
                if len(parts) >= 3:
                    task_name = parts[0].split(": ")[1].strip()
                    points = int(parts[1].split(" ")[0])
                    completed = parts[2].split(": ")[1].strip() == "✔"

                    self.task_manager.add_tasks(task_name, points, completed)

        self.task_manager.save_tasks()
        messagebox.showinfo("Success", "Tasks saved successfully.")


    def update_task_area(self):
        self.task_area.config(state="normal")
        self.clear_tasks()
        
        tasks = self.task_manager.get_tasks()
        if not tasks:
            self.task_area.insert("end", "No tasks for today.\n")
        else:
            for i, task in enumerate(tasks):
                task_text = f"{i+1}. {task.task_name}  |  {task.points} pts  |  Completed: {'✔' if task.completed else '✘'}\n"
                self.task_area.insert("end", task_text)

        self.task_area.config(state="disabled")


    def clear_tasks(self):
        """Clears the task area."""
        self.task_area.delete("1.0", "end")
