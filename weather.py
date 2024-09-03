import requests#used to make HTTP requests to the API
from dotenv import load_dotenv#Used to load environment variables from a .env file.
import os#Used to access environment variables.
from dataclasses import dataclass#usede to create dataclass

load_dotenv()  # Load environment variables from a .env file
api_key = os.getenv('API_KEY')  # os-Get the value of the API key from the environment variables .env

@dataclass#@dataclass: A decorator to automatically generate special methods like __init__() for the class.
#his data class holds the weather information: main, description, icon, and temperature.
class weatherdata:
    main: str
    description: str
    icon: str
    temperature:int
'''This function makes a request to the OpenWeatherMap Geocoding API to get the latitude and longitude of a given city.
If the response is successful, it extracts and returns the latitude and longitude.
If the response fails, it prints an error message and returns None.
'''
def get_lat_lon(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}&units=metric').json()
    if response:
        data = response[0]
        lat, lon = data.get('lat'), data.get('lon')
        return lat, lon
    else:
        print("Error: Unable to fetch coordinates.")
        return None, None
'''This function makes a request to the OpenWeatherMap Current Weather API to get the weather data for the given latitude and longitude.
It then creates an instance of the weatherdata data class with the relevant information and returns it.'''
def current_weather(lat, lon, API_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = weatherdata(
        main = response.get('weather')[0].get('main'),
        description = response.get('weather')[0].get('description'),
        icon = response.get('weather')[0].get('icon'),
        temperature = int(response.get('main').get('temp'))
    )
    return data
#main(): Combines the get_lat_lon() and current_weather() functions to get the weather data for a given city.
def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = current_weather(lat, lon, api_key)
    return weather_data


if __name__ == "__main__":
    lat, lon = get_lat_lon('Toronto', 'ON', 'Canada', api_key)
    if lat and lon:
        print(current_weather(lat, lon, api_key))

