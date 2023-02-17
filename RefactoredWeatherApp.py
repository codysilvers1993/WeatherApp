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

# chatbox
label = tk.Label(mainWindow, text="Welcome To ClimaChat, Please Enter Your City!", font=("Arial", 16))
label.pack(pady=10)
textfield = tk.Entry(mainWindow, justify="center", width=17, font=("Times New Roman", 25, "bold"), bg="light blue")
textfield.place(x=10, y=50)
textfield.focus()

# label
label1 = Label(mainWindow, text="WIND", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
label1.place(x=10, y=366)
label2 = Label(mainWindow, text="HUMIDITY", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
label2.place(x=100, y=366)
label3 = Label(mainWindow, text="DESCRIPTION", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
label3.place(x=220, y=366)
label4 = Label(mainWindow, text="PRESSURE", font=("Times New Roman", 15, "bold"), fg="black", bg="#1ab5ef")
label4.place(x=598, y=366)


mainWindow.mainloop()
