import requests
import tkinter as tk
from tkinter import Label
from tkinter import *
import spacy
import sqlite3


# blank display generator for window

def display():
    window = tk.Tk()
    window.title('ClimaChat')
    label = Label(window, text="Welcome to ClimaChat!\n Your Resource For Weather Information On Demand!",
                  font=('Times New Roman', 16, 'bold'))
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


# function that stores userinformation into constructor (python dictionary) and returns a user
def store_personal_info(first_name, last_name, location):
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'location': location
    }
    return user


# function to initialize database containing table with columns first_name, last_name, and location. Will only create
# once and will check if already created.
def database_of_personal_info():
    conn = sqlite3.connect('user_database')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_database
                 (first_name text, last_name text, location text)''')
    conn.commit()
    conn.close()


# function with city_name and api_key as parameters and returns weather_data
def get_weather_data(city_name, api_key):
    # Retrieves only CURRENT WEATHER AND FORECAST data for a given city using the OpenWeatherMap API.
    # Just activated private key, website says it will take a couple hours before private key is active.
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

def main():
    # create user database on startup
    database_of_personal_info()
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
