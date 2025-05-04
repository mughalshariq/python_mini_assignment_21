class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """Convert Celsius to Fahrenheit"""
        return (c * 9/5) + 32

# Using the static method
print("32°C is", TemperatureConverter.celsius_to_fahrenheit(32), "°F")
print("0°C is", TemperatureConverter.celsius_to_fahrenheit(0), "°F")
print("100°C is", TemperatureConverter.celsius_to_fahrenheit(100), "°F")