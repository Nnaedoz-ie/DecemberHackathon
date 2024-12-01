import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Fetch credentials from .env
API_KEY = os.getenv('API_KEY')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Function to fetch weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        print(f"Weather in {city}: {weather_description}, {temperature:.2f}°C")
    else:
        print(f"Failed to fetch weather data: {response.status_code}")

# Prompt user for a city and display weather
if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    get_weather(city_name)

def get_weather(city):
    if not API_KEY:
        print("Error: API key is missing. Please check your .env file.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 401:
        print("Error: Unauthorized. Check if your API key is valid.")
    elif response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        print(f"Weather in {city}: {weather_description}, {temperature:.2f}°C")
    else:
        print(f"Failed to fetch weather data: {response.status_code}")

