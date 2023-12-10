import unittest
from unittest.mock import patch
from weather_utils import get_weather, format_weather

class TestWeatherUtils(unittest.TestCase):

    @patch('builtins.input', return_value='Stockholm')
    def test_get_weather(self, mock_input):
        weather_data = get_weather('Stockholm')
        self.assertIsInstance(weather_data, dict)
        self.assertIn('name', weather_data)

    def test_format_weather(self):
        sample_weather_data = {
            'name': 'Stockholm',
            'weather': [{'main': 'Clear', 'description': 'clear sky'}],
            'main': {'temp': 273.15}
        }
        formatted_weather = format_weather(sample_weather_data)
        expected_output = "Now in the city Stockholm Clear (clear sky) and temperature is 0.00°C."
        self.assertEqual(formatted_weather, expected_output)

    @patch('builtins.input', return_value='NonexistentCity')
    def test_get_weather_nonexistent_city(self, mock_input):
        weather_data = get_weather('NonexistentCity')
        self.assertIsInstance(weather_data, dict)
        self.assertIn('cod', weather_data)
        self.assertEqual(weather_data['cod'], '404')

        formatted_weather = format_weather(weather_data)
        expected_output = "City is not found."
        self.assertEqual(formatted_weather, expected_output)

if __name__ == '__main__':
    unittest.main()
