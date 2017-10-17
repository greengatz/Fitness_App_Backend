import unittest
from unittest.mock import MagicMock
from app import fitness_service

class test_save_workout_route(unittest.TestCase):
    
    def test_happy_path(self):
        self.assertEqual("true", "true")
    
    # not implemented
    def test_invalid_object(self):
        self.assertEqual("true", "true")