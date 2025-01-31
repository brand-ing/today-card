import unittest
from today_card.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test Task", points=10)

        self.assertEqual(task.task_name, "Test Task")
        self.assertEqual(task.points, 10)
        self.assertFalse(task.completed, False)

    def test_task_mark_completion(self):
        task = Task("Test Task", points=10)

        self.assertFalse(task.completed)

        task.mark_complete()

        self.assertTrue(task.completed)

    def test_task_to_dict(self):
        """Test if to_dict() correctly converts the task to a dictionary."""
        task = Task("Test Task", "2025-07-28", 10, True)
        expected_dict = {
            "Task": "Test Task",
            "Date": "2025-07-28",
            "Points": 10,
            "Completed": True
        }
        self.assertEqual(task.to_dict(), expected_dict)

    def test_task_from_dict(self):
        """Test if from_dict() correctly converts a dictionary to a Task object."""
        task_data = {
            "Task": "Review Code",
            "Date": "2025-07-28",
            "Points": 5,
            "Completed": False
        }
        task = Task.from_dict(task_data)
        self.assertEqual(task.task_name, "Review Code")
        self.assertEqual(task.date, "2025-07-28")
        self.assertEqual(task.points, 5)
        self.assertFalse(task.completed)

    def task_self_string_representation(self):
        task = Task("Test Task", points=10)

        expected_output = "Task: Test Task | Date: 2021-08-01 | Points: 10 | Status: ✗ Not Completed"
        self.assertEqual(str(task), expected_output)

        task.mark_complete()
        expected_output_completed = "Task: Test Task | Date: 2021-08-01 | Points: 10 | Status: ✓ Completed"
        self.assertEqual(str(task), expected_output_completed)

if __name__ == "__main__":
    unittest.main()