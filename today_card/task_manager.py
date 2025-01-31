from tkinter import messagebox
import pandas as pd
import datetime
import openpyxl
import os
from task import Task

# Save to spreadsheet
DB_FILE = "tasks_db.xlsx"
MAX_TASKS = 9


class TaskManager:
    def __init__(self):
        self.db_file = DB_FILE
        self.tasks = self.load_tasks()

        while len(self.tasks) < MAX_TASKS:
            self.tasks.append(None)
        
    def add_tasks(self, task_name: str):
        if len([t for t in self.tasks if t]) >= MAX_TASKS:
            messagebox.showwarning("FULL", "You have reached the maximum number of tasks for today.")
            return False

        new_task = Task(task_name)
        self.tasks.append(new_task)
        self.save_tasks()
        return True


    def save_tasks(self):
        """ Format the tasks and store in the database"""
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        data = []

        for task in self.tasks:
            if task:  # Ensure no empty entries
                data.append({"Date": today, "Tasks": task.task_name})  # Store task name

        try:
            df = pd.DataFrame(data)

            if os.path.exists(DB_FILE):
                existing_df = pd.read_excel(DB_FILE)
                df = pd.concat([existing_df, df], ignore_index=True)  # Append new data

            df.to_excel(DB_FILE, index=False)  # Overwrite with new data

            messagebox.showinfo("Saved", "Tasks saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


    def load_tasks(self):
        try:
            if not os.path.exists(DB_FILE):
                return []

            df = pd.read_excel(DB_FILE)

            if df.empty or not all(col in df.columns for col in ["Task", "Points", "Completed"]):
                return []

            today = datetime.datetime.today().strftime("%Y-%m-%d")
            today_tasks = df[df["Date"] == today]

            tasks_list = []
            for _, row in today_tasks.iterrows():
                task_name = row["Task"]
                points = row["Points"]
                completed = row["Completed"] == "Yes"  # Convert string to boolean
                tasks_list.append(Task(task_name, points, completed))

            return tasks_list

        except Exception as e:
            messagebox.showwarning("Error", f"Could not load tasks: {e}")
            return []


    def get_tasks(self):
        return self.tasks