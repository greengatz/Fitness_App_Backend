import unittest
from unittest.mock import MagicMock
from fitness_service import FitnessService
from fitness_repo import FitnessRepository

class test_save_workout_route(unittest.TestCase):

    mock_repo = FitnessRepository(None)
    service = FitnessService(mock_repo)

    def test_happy_path(self):
        valid_workout_dict = {"distance" : "1.23", "start_time" : "a_time", "end_time" : "another_time"}
        self.mock_repo.store_workout = MagicMock(return_value=202)
        self.assertEqual(self.service.validate_and_save_workout(valid_workout_dict)[1], 202)

    def test_invalid_workout_fields_missing(self):
        dict_missing_dates = {"distance" : "1.23"}
        self.assertEqual(self.service.validate_and_save_workout(dict_missing_dates)[1], 400)
