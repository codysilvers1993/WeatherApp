import requests


# function with city_name and api_key as parameters and returns weather_data
def get_weather_data(city_name, api_key):
    # Retrieves only CURRENT WEATHER AND FORECAST data for a given city using the OpenWeatherMap API.
    # Just activated private key, website says it will take a couple hours before private key is active.
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data


def main():
    # defines api key and city name
    api_key = "e90573d841c1b6685552f55de613bc6a"
    # city name hard coded for testing but will be accessed from user input later
    city_name = "london"
    # calls get weather functon and prints info
    weather_data = get_weather_data(city_name, api_key)
    print(weather_data)

if __name__ == '__main__':
    main()
