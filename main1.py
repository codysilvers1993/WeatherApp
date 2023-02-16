import requests
import tkinter as tk
from tkinter import Label
from tkinter import *


# blank display generator for window
# fixed error with name of application displaying in window frame
def display():
    window = tk.Tk()
    window.title('ClimaChat')
    label = Label(window, text="Welcome to ClimaChat!\n Your Resource For Weather Information On Demand!",
                  font=('Times New Roman', 13, 'bold'))
    label.pack()
    width = 600
    height = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    text = Text(window, width=50, height=30, background="black", foreground="#fff",
                font=('Sans Serif', 13, 'italic bold'))
    text.insert(INSERT, "Hello, What Is Your location?")
    text.pack(expand=1, fill=BOTH)

    window.mainloop()


# function with city_name and api_key as parameters and returns weather_data
def get_weather_data(city_name, api_key):
    # Retrieves only CURRENT WEATHER AND FORECAST data for a given city using the OpenWeatherMap API.
    # Just activated private key, website says it will take a couple hours before private key is active.
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data


def main():
    # run window function to draw display. loops draw.
    display()
    # defines api key and city name
    api_key = "e90573d841c1b6685552f55de613bc6a"
    # city name hard coded for testing but will be accessed from user input later
    city_name = "london"
    # calls get weather function and prints info
    weather_data = get_weather_data(city_name, api_key)
    print(weather_data)


if __name__ == '__main__':
    main()
