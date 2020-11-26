import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task1 = Task("Wash dishes", 5)
        self.task2 = Task("Cook dinner", 10)
        self.task3 = Task("Clean windows", 15)

    def test_task_has_desc(self):
        self.assertEqual("Wash dishes", self.task1.description)
    
    def test_task_has_duration(self):
        self.assertEqual(5, self.task1.duration)

    # def test_task_has_preference_level(self):
    #     self.assertEqual(3, self.task2.preference_level)

    def test_get_preferred_option(self):
        self.assertEqual("Wash dishes", self.task1.description, self.task2.description)


    


    

    
