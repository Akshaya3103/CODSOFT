import requests
from pprint import pprint
# Define the function to get the weather data from the API
def get_weather_data(city_name):
    # Make the API request
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": "YOUR_API_KEY",
    }
    response = requests.get(url, params=params)
    # Parse the response
    data = response.json()
    # Extract the relevant weather information
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    return temperature, humidity, wind_speed, description
# Define the function to display the weather to the user
def display_weather(temperature, humidity, wind_speed, description):
    print("The current temperature in {} is {} degrees Celsius.".format(city_name, temperature))
    print("The humidity is {}%.".format(humidity))
    print("The wind speed is {} meters per second.".format(wind_speed))
    print("The weather description is '{}'.".format(description))
# Get the city name from the user
city_name = input("Enter the city name: ")
# Get the weather data for the city
temperature, humidity, wind_speed, description = get_weather_data(city_name)
# Display the weather to the user
display_weather(temperature, humidity, wind_speed, description)