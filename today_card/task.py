import datetime

class Task:
    def __init__(self, task_name: str, date: str = None, points: int = 0, completed: bool = False):
        self.task_name = task_name
        self.date = date if date else datetime.datetime.today().strftime("%Y-%m-%d")
        self.points = points
        self.completed = completed

    def mark_complete(self):
        self.completed = True
    
    def to_dict(self) -> dict:
        return {
            "Task": self.task_name,
            "Date": self.date,
            "Points": self.points,
            "Completed": self.completed
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Task":
        """Creates a Task object from a dictionary."""
        return Task(
            task_name=data.get("Task", "Untitled Task"),
            date=data.get("Date", None),
            points=data.get("Points", 0),
            completed=data.get("Completed", False)
        )


    def __str__(self):
        """String representation of the task."""
        status = "✓ Completed" if self.completed else "✗ Not Completed"
        return f"Task: {self.task_name} | Date: {self.date} | Points: {self.points} | Status: {status}"