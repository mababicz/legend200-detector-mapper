# tests/test_loader.py
import unittest
from legend200_data_loader.loader import LegendDataLoader

class TestLegendDataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = LegendDataLoader()

    def test_load_raw_data(self):
        # Assuming you have a mock or test environment set up for this
        loaded_data = self.loader.load_raw_data()
        self.assertIsInstance(loaded_data, dict)  # Check if data is returned as a dictionary

if __name__ == '__main__':
    unittest.main()
