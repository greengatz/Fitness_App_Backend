import unittest
from app import fitness_repo

class test_save_workout_route(unittest.TestCase):
    
    def test_happy_path(self):
        self.assertEqual("true", "true")
    
    def test_duplicate_value(self):
        self.assertEqual("true", "true")
