from tkinter import messagebox
import pandas as pd
import datetime
import openpyxl
import os

# Save to spreadsheet
DB_FILE = "tasks_db.xlsx"

class TaskManager:
    def __init__(self):
        self.db_file = DB_FILE

def save_tasks(task_area):
    tasks = task_area.get("1.0", tk.END)
    if tasks:
        tasks_list = tasks.split("\n")
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        data = [{"Date": today, "Tasks": task} for task in tasks_list if task.strip()]

        try:
            df = pd.DataFrame(data)
            with pd.ExcelWriter(DB_FILE, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                # Ensure the file exists
                if not os.path.exists(DB_FILE):
                    df.to_excel(writer, sheet_name= DB_FILE, index=False)
                df.to_excel(writer, index=False, header=not writer.sheets)
            messagebox.showinfo("Saved", "Tasks saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("No Tasks", "No tasks to save")


def load_tasks(task_area):
    try:
        df = pd.read_excel(DB_FILE)
        today = datetime.datetime.today()
        today_tasks = df[df["Date"] == pd.Timestamp(today)]
        if not today_tasks.empty:
            for task in today_tasks["Tasks"]:
                task_area.insert(tk.END, f" - {task}\n")
    except FileExistsError:
        messagebox.showwarning("Not Found", "No spreadsheet database found.")
    except Exception as e:
        messagebox.showwarning("Error", f"Could not load tasks: {e}")
    return []
