import requests
import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import *
import spacy
import sqlite3
from PIL import Image, ImageTk


# Window generator function

def display():
    # Basic window characteristics
    window = tk.Tk()
    window.geometry("600x400")

    # Load the animated GIF image using PIL
    gif = Image.open("cloud.gif")

    # Create a sequence of frames from the GIF image
    frames = []
    for frame in range(0, gif.n_frames):
        gif.seek(frame)
        frames.append(ImageTk.PhotoImage(gif))

    # Create a label to hold the GIF image
    label = Label(window)
    label.pack(fill=BOTH, expand=YES)

    # Function to loop through the frames and display them in the label
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == len(frames):
            ind = 0
        label.configure(image=frame)
        window.after(100, update, ind)

    # Start the loop to update the GIF frames
    window.after(0, update, 0)

    # create transparent styles for the text boxes and buttons
    style = ttk.Style(window)
    style.configure('Transparent.TEntry', background='systemTransparent')
    style.configure('Transparent.TButton', background='systemTransparent')

    window.title('ClimaChat')
    label = Label(window, text="Welcome to ClimaChat!\n Your Resource For Weather Information On Demand!",
                  font=('Arial', 16, 'bold'))
    label.pack()
    width = 600
    height = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    # Create the labels for the text boxes, username and password
    username_label = tk.Label(window, text="Username", anchor="w", foreground="black", font=("Arial", 14))
    password_label = tk.Label(window, text="Password", anchor="w", foreground="black", font=("Arial", 14))

    # Initialize the text boxes
    username_textbox = tk.Entry(window, width=30, font=("Arial", 14))
    password_textbox = tk.Entry(window, width=30, font=("Arial", 14))

    # Display the labels and text boxes into the window(fill = x fills entire horizontal space)
    username_label.pack(fill="x")
    username_textbox.pack(fill="x")
    password_label.pack(fill="x")
    password_textbox.pack(fill="x")

    # Creates buttons for login and register, buttons will print message as test
    login_button = tk.Button(window, text="Login", command=test_login_button, width=20, height=2, font="10")
    register_button = tk.Button(window, text="Register", command=test_register_button, width=20, height=2, font="10")

    login_button.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.N)
    register_button.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.N)

    # Draw window continuously until program exit.
    window.mainloop()


# Function that stores user information into constructor (python dictionary) and returns a user.
def store_personal_info(first_name, last_name, location):
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'location': location
    }
    return user


# Iest functions for when I implement buttons for register and login.
def test_login_button():
    print("login button clicked")


def test_register_button():
    print("register button clicked")


# Function to initialize database table with three columns (first_name, last_name, and location). Will only create
# Once and will check if already created. If already created will not execute.
def database_of_personal_info():
    conn = sqlite3.connect('database_of_personal_info')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_database
                 (first_name text, last_name text, location text)''')
    conn.commit()
    conn.close()


# Function with city_name and api_key as parameters and returns weather_data
def get_weather_data(city_name, api_key):
    # Retrieves only CURRENT WEATHER AND FORECAST data for a given city using the OpenWeatherMap API.
    # Just activated private key, website says it will take a couple hours before private key is active.
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data


def main():
    # Create database_of_personal_info table database on startup.
    database_of_personal_info()
    # Run window function to draw display. loops draw.
    display()
    # Define API key(Only good for 60 calls a day)
    api_key = "e90573d841c1b6685552f55de613bc6a"
    # City name hard coded for testing but will be accessed from user input later
    city_name = "london"
    # Calls weather function and prints info for testing
    # Only prints string so that's an issue.


# deactivated api call

# weather_data = get_weather_data(city_name, api_key)
# print(weather_data)


if __name__ == '__main__':
    main()
