from weather_api_service import Weather
from temperature_converter import from_celsius_to_fahrenheit, from_celsius_to_kelvin
from weather_api_service import Celsius

def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (
        f"{weather.city}, the temperature is {weather.temperature}°C, "
        f"{weather.weather_type.value}\n"
        f"Sunrise: {weather.sunrise.strftime('%H:%M')}\n"
        f"Sunset: {weather.sunset.strftime('%H:%M')}\n"
    )


def format_temperature(temperature: Celsius) -> str:
    """Formats temperature in string that contains all temperature formats"""
    return (
        "Temperature in different formats:\n"
        f"{temperature}°C, "
        f"{from_celsius_to_fahrenheit(temperature)}°F, "
        f"{from_celsius_to_kelvin(temperature)}K"
    )
