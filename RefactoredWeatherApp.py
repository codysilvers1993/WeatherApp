from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import requests
import pytz

# draws main window
mainWindow = tk.Tk()
mainWindow.title("ClimaChat")
mainWindow.geometry("500x500")
mainWindow.resizable(False, False)

# test function to print API data to console
def print_weather_data():
    city_name = getCityName()
    weather_data = getWeatherData(city_name)
    print(weather_data)


# passes returned city name to openWeatherAPI to gather API weather data
def getWeatherData(getCityName):
    api_key = "e90573d841c1b6685552f55de613bc6a"
    openWeatherAPIurl = f"http://api.openweathermap.org/data/2.5/weather?q={getCityName}&appid={api_key}"
    response = requests.get(openWeatherAPIurl)
    weatherData = response.json()
    return weatherData


# function that returns city name gathered from textfield
def getCityName():
    city_name = textfield.get()
    return city_name


# chatbox
label = tk.Label(mainWindow, text="Welcome To ClimaChat, Please Enter Your City!", font=("Arial", 16))
label.pack(pady=10)
textfield = tk.Entry(mainWindow, justify="center", width=17, font=("Times New Roman", 25, "bold"), bg="light blue")
textfield.place(x=10, y=50)
textfield.focus()
button = tk.Button(mainWindow, text="Generate Request", font=("Arial", 14), command=print_weather_data)
button.place(x=50, y=100)

# labels
windTitleLabel = Label(mainWindow, text="WIND", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
windTitleLabel.place(x=10, y=366)
humidityTitleLabel = Label(mainWindow, text="HUMIDITY", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
humidityTitleLabel.place(x=75, y=366)
descriptionTitleLabel = Label(mainWindow, text="DESCRIPTION", font=("Times New Roman", 15, "bold"), fg="black",
                              bg="#1ab5ef")
descriptionTitleLabel.place(x=188, y=366)
pressureTitleLabel = Label(mainWindow, text="PRESSURE", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
pressureTitleLabel.place(x=335, y=366)

# placeholder labels
windLabel = Label(text="...", font=("Times New Roman", 20, "bold"), fg="#ee666d")
windLabel.place(x=10, y=400)
humidityLabel = Label(text="...", font=("Times New Roman", 20, "bold"), fg="#ee666d")
humidityLabel.place(x=70, y=400)
descriptionLabel = Label(text="...", font=("Times New Roman", 20, "bold"), fg="#ee666d")
descriptionLabel.place(x=185, y=400)
pressureLabel = Label(text="...", font=("Times New Roman", 20, "bold"), fg="#ee666d")
pressureLabel.place(x=333, y=400)
mainWindow.mainloop()
