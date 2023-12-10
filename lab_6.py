import unittest
from unittest.mock import patch
from weather_utils import get_weather, format_weather

class TestWeatherUtils(unittest.TestCase):

    @patch('builtins.input', return_value='Stockholm')
    def test_get_weather(self, mock_input):
        weather_data = get_weather('Stockholm')
        self.assertIsInstance(weather_data, dict)
        self.assertIn('name', weather_data)

        weather_data_invalid = get_weather('InvalidCity')
        self.assertIsInstance(weather_data_invalid, dict)
        self.assertIn('cod', weather_data_invalid)
        self.assertEqual(weather_data_invalid['cod'], '404')

    def test_format_weather(self):
        sample_weather_data = {
            'name': 'Stockholm',
            'weather': [{'main': 'Clear', 'description': 'clear sky'}],
            'main': {'temp': 273.15}
        }
        formatted_weather = format_weather(sample_weather_data)
        expected_output = "Now in the city Stockholm Clear (clear sky) and temperature is 0.00°C."
        self.assertEqual(formatted_weather, expected_output)

        sample_weather_data_invalid = {
            'weather': [{'main': 'Clear', 'description': 'clear sky'}],
            'main': {'temp': 273.15}
        }
        formatted_weather_invalid = format_weather(sample_weather_data_invalid)
        expected_output_invalid = "Error."
        self.assertEqual(formatted_weather_invalid, expected_output_invalid)

        sample_weather_data_no_main = {
            'name': 'Stockholm',
            'weather': [{'main': 'Clear', 'description': 'clear sky'}],
        }
        formatted_weather_no_main = format_weather(sample_weather_data_no_main)
        expected_output_no_main = "Error."
        self.assertEqual(formatted_weather_no_main, expected_output_no_main)

if __name__ == '__main__':
    unittest.main()
