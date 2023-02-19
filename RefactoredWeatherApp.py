from tkinter import *
import tkinter as tk
import requests

# draws main window
mainWindow = tk.Tk()
mainWindow.title("ClimaChat")
mainWindow.geometry("500x500")
mainWindow.resizable(False, False)

# global variable to store weather data
weather_data = None


def getWeatherData(getCityName):
    api_key = "e90573d841c1b6685552f55de613bc6a"
    openWeatherAPIurl = f"http://api.openweathermap.org/data/2.5/weather?q={getCityName}&appid={api_key}"
    response = requests.get(openWeatherAPIurl)
    weatherData = response.json()
    return weatherData


# function that returns city name gathered from textfield and gets weather data
def getCityName():
    global weather_data
    city_name = textfield.get()
    weather_data = getWeatherData(city_name)


def print_weather_data():
    # access global weather data variable
    global weather_data
    getCityName()
    # if city name and API keywords valid will update label fields with current weather info
    if weather_data:
        wind_speed = weather_data["wind"]["speed"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        pressure = weather_data["main"]["pressure"]

        # update labels with weather information
        windLabel.config(text=f"{wind_speed} m/s")
        humidityLabel.config(text=f"{humidity}%")
        descriptionLabel.config(text=description)
        pressureLabel.config(text=f"{pressure} hPa")


# chatbox
label = tk.Label(mainWindow, text="Welcome To ClimaChat\n Please Enter Your City For Current Weather Information",
                 font=("Arial", 14))
label.pack(pady=10)
textfield = tk.Entry(mainWindow, justify="center", width=17, font=("Times New Roman", 25, "bold"), bg="light blue")
textfield.place(x=95, y=65)
textfield.focus()
button = tk.Button(mainWindow, text="Generate Request", font=("Arial", 14), command=print_weather_data)
button.place(x=148, y=115)

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
windLabel = Label(text="...", font=("Times New Roman", 12, "bold"), fg="#ee666d")
windLabel.place(x=10, y=400)
humidityLabel = Label(text="...", font=("Times New Roman", 12, "bold"), fg="#ee666d")
humidityLabel.place(x=70, y=400)
descriptionLabel = Label(text="...", font=("Times New Roman", 12, "bold"), fg="#ee666d")
descriptionLabel.place(x=185, y=400)
pressureLabel = Label(text="...", font=("Times New Roman", 12, "bold"), fg="#ee666d")
pressureLabel.place(x=333, y=400)
mainWindow.mainloop()
