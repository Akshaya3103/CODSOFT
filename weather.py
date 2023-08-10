import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            weather_info = {
                "Temperature": data["main"]["temp"],
                "Humidity": data["main"]["humidity"],
                "Wind Speed": data["wind"]["speed"],
                "Description": data["weather"][0]["description"].capitalize()
            }
            return weather_info
        else:
            print("Error: Unable to fetch weather data.")
            return None

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def display_weather(weather_info):
    if weather_info:
        print("\nWeather Information:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    else:
        print("\nWeather information not available.")

def main():
    api_key = "858ee7df8bf0c82eed63adf6e628ad18"  
    location = input("Enter the city name or zip code: ")
    weather_info = get_weather(api_key, location)

    display_weather(weather_info)

if __name__ == "__main__":
    main()
