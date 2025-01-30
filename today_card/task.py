import datetime

class Task:
    def __init__(self, task_name: str, date: str = None, score: int = 0, completed: bool = False):
        self.task_name = task_name
        self.date = date if date else datetime.datetime.today().strftime("%Y-%m-%d")
        self.score = score
        self.completed = completed

    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        """String representation of the task."""
        status = "✓ Completed" if self.completed else "✗ Not Completed"
        return f"Task: {self.task_name} | Date: {self.date} | Score: {self.score} | Status: {status}"




