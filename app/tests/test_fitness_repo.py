import unittest
from unittest.mock import MagicMock
from fitness_repo import FitnessRepository
from workout import Workout

class test_save_workout_route(unittest.TestCase):

    mock_conn = type('Connection', (object,), { "cursor": "method", "commit": "otherMethod" })
    mock_cursor = type('Cursor', (object,), { "execute": "method", "close": "otherMethod" })
    repository = FitnessRepository(mock_conn)

    def test_happy_path(self):
        valid_workout = Workout({ "distance" : "1.23", "start_time" : "a_time", "end_time" : "another_time" })

        self.mock_cursor.execute = MagicMock()
        self.mock_cursor.close = MagicMock()
        self.mock_conn.cursor = MagicMock(return_value=self.mock_cursor)
        self.mock_conn.commit = MagicMock()

        self.assertEqual(self.repository.store_workout(valid_workout), 202)

