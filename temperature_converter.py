def from_celsius_to_fahrenheit(celsius: float) -> int:
    return round(celsius * 9 / 5 + 32)

def from_fahrenheit_to_celsius(fahrenheit: float) -> int:
    return round((fahrenheit - 32) * 5 / 9)

def from_celsius_to_kelvin(celsius: int) -> int:
    return celsius + 273

def from_kelvin_to_celsius(kelvin: int) -> int:
    return kelvin - 273