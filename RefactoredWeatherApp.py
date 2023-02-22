from tkinter import *
import tkinter as tk
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen

# draws main window
mainWindow = tk.Tk()
mainWindow.title("ClimaChat")
mainWindow.geometry("500x500")
mainWindow.resizable(False, False)

# global variable to store weather data
weather_data = None


def getWeatherData(getCityName):
    api_key = "e90573d841c1b6685552f55de613bc6a"
    openWeatherAPIurl = f"http://api.openweathermap.org/data/2.5/weather?q={getCityName}&appid={api_key}&units=imperial"
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
        temp = weather_data["main"]["temp"]
        wind_speed = weather_data["wind"]["speed"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        pressure = weather_data["main"]["pressure"]
        icon = weather_data["weather"][0]["icon"]

        #creates weather icon
        weatherIconURL = f"https://openweathermap.org/img/wn/{icon}.png"
        URL = weatherIconURL
        u = urlopen(URL)
        raw_data = u.read()
        u.close()

        photo = ImageTk.PhotoImage(data=raw_data)


        # update labels with weather information
        temperatureLabel.configure(text=f"{temp}\u00b0 F")
        windLabel.config(text=f"{wind_speed} m/s")
        humidityLabel.config(text=f"{humidity}%")
        descriptionLabel.config(text=description)
        pressureLabel.config(text=f"{pressure} hPa")
        # place weather icon
        weatherIconLabel = tk.Label(image=photo)
        weatherIconLabel.image = photo
        weatherIconLabel.place(x=200, y=280)






# chatbox
label = tk.Label(mainWindow, text="Welcome To ClimaChat\n Please Enter Your City For Current Weather Information", font=("Arial", 14))
label.pack(pady=10)
textfield = tk.Entry(mainWindow, justify="center", width=17, font=("Times New Roman", 25, "bold"), bg="light blue")
textfield.place(x=95, y=65)
textfield.focus()
button = tk.Button(mainWindow, text="Generate Request", font=("Arial", 14), command=print_weather_data)
button.place(x=148, y=115)

# labels
temperatureTitleLabel = Label(mainWindow, text="TEMPERATURE", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
temperatureTitleLabel.place(x=10, y=170)
windTitleLabel = Label(mainWindow, text="WIND", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
windTitleLabel.place(x=175, y=170)
humidityTitleLabel = Label(mainWindow, text="HUMIDITY", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
humidityTitleLabel.place(x=243, y=170)
descriptionTitleLabel = Label(mainWindow, text="DESCRIPTION", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
descriptionTitleLabel.place(x=10, y=250)
pressureTitleLabel = Label(mainWindow, text="PRESSURE", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
pressureTitleLabel.place(x=358, y=170)
weatherIconTitleLabel = Label(mainWindow, text="ICON", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
weatherIconTitleLabel.place(x=200, y=250)

# placeholder labels
temperatureLabel = Label(text="...", font=("Times New Roman", 14, "bold"), fg="#ee666d")
temperatureLabel.place(x=65, y=200)
windLabel = Label(text="...", font=("Times New Roman", 14, "bold"), fg="#ee666d")
windLabel.place(x=175, y=200)
humidityLabel = Label(text="...", font=("Times New Roman", 14, "bold"), fg="#ee666d")
humidityLabel.place(x=270, y=200)
descriptionLabel = Label(text="...", font=("Times New Roman", 14, "bold"), fg="#ee666d")
descriptionLabel.place(x=10, y=280)
pressureLabel = Label(text="...", font=("Times New Roman", 14, "bold"), fg="#ee666d")
pressureLabel.place(x=370, y=200)

weatherIconLabel = Label(text="", font=("Times New Roman", 14, "bold"), fg="#ee666d")
weatherIconLabel.place(x=200, y=280)

mainWindow.mainloop()
