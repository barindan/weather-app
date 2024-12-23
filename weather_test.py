import unittest
from unittest.mock import patch, MagicMock
from urllib.error import URLError
from datetime import datetime
from weather_api_service import (
    _parse_weather_type,
    _parse_city,
    _parse_temperature,
    _parse_sun_time,
    _get_openweather_response,
    ApiServiceError
)
from temperature_converter import from_celsius_to_fahrenheit, from_celsius_to_kelvin
class TestWeatherApiService(unittest.TestCase):

    def setUp(self):
        self.openweather_response = {
            "coord": {
                "lon": 7.367,
                "lat": 45.133
            },
            "weather": [
                {
                    "id": 501,
                    "main": "Rain",
                    "description": "moderate rain",
                    "icon": "10d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 284.2,
                "feels_like": 282.93,
                "temp_min": 283.06,
                "temp_max": 286.82,
                "pressure": 1021,
                "humidity": 60,
                "sea_level": 1021,
                "grnd_level": 910
            },
            "visibility": 10000,
            "wind": {
                "speed": 4.09,
                "deg": 121,
                "gust": 3.47
            },
            "rain": {
                "1h": 2.73
            },
            "clouds": {
                "all": 83
            },
            "dt": 1726660758,
            "sys": {
                "type": 1,
                "id": 6736,
                "country": "IT",
                "sunrise": 1726636384,
                "sunset": 1726680975
            },
            "timezone": 7200,
            "id": 3165523,
            "name": "Province of Turin",
            "cod": 200
        }

    def test_parse_weather_type(self):
        self.assertEqual(_parse_weather_type(self.openweather_response), self.openweather_response["weather"][0]["main"])

    def test_parse_city(self):
        self.assertEqual(_parse_city(self.openweather_response), self.openweather_response["name"])

    def test_parse_temperature(self):
        self.assertEqual(_parse_temperature(self.openweather_response), round(self.openweather_response["main"]["temp"]))

    def test_parse_sun_time(self):
        self.assertEqual(
            _parse_sun_time(self.openweather_response, "sunrise"),
            datetime.fromtimestamp(self.openweather_response["sys"]["sunrise"])
        )
        self.assertEqual(
            _parse_sun_time(self.openweather_response, "sunset"),
            datetime.fromtimestamp(self.openweather_response["sys"]["sunset"])
        )

    @patch('weather_api_service.urllib.request.urlopen')
    def test_get_openweather_response_success(self, mock_urlopen):
        # Mock the response of urlopen
        mock_response = MagicMock()
        mock_response.read.return_value = '{"mock": "data"}'
        mock_urlopen.return_value = mock_response

        # Call the function
        response = _get_openweather_response(latitude=0.0, longitude=0.0)

        # Assert the response is as expected
        self.assertEqual(response, '{"mock": "data"}')

    @patch('weather_api_service.urllib.request.urlopen')
    def test_get_openweather_response_failure(self, mock_urlopen):
        # Simulate a URLError
        mock_urlopen.side_effect = URLError('Mocked error')

        # Assert that ApiServiceError is raised
        with self.assertRaises(ApiServiceError):
            _get_openweather_response(latitude=0.0, longitude=0.0)


class TestTemperatureConverter(unittest.TestCase):
    def test_from_celsius_to_fahrenheit(self):
        self.assertEqual(from_celsius_to_fahrenheit(0), 32)
        self.assertEqual(from_celsius_to_fahrenheit(100), 212)
        self.assertEqual(from_celsius_to_fahrenheit(-40), -40)

    def test_from_celsius_to_kelvin(self):
        self.assertEqual(from_celsius_to_kelvin(0), 273)
        self.assertEqual(from_celsius_to_kelvin(100), 373)
        self.assertEqual(from_celsius_to_kelvin(-40), 233)