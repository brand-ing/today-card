import unittest
from today_card.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test Task", score=10)

        self.assertEqual(task.task_name, "Test Task")
        self.assertEqual(task.score, 10)
        self.assertFalse(task.completed, False)

    def test_task_mark_completion(self):
        task = Task("Test Task", score=10)

        self.assertFalse(task.completed)

        task.mark_complete()

        self.assertTrue(task.completed)

    def task_self_string_representation(self):
        task = Task("Test Task", score=10)

        expected_output = "Task: Test Task | Date: 2021-08-01 | Score: 10 | Status: ✗ Not Completed"
        self.assertEqual(str(task), expected_output)

        task.mark_complete()
        expected_output_completed = "Task: Test Task | Date: 2021-08-01 | Score: 10 | Status: ✓ Completed"
        self.assertEqual(str(task), expected_output_completed)

if __name__ == "__main__":
    unittest.main()