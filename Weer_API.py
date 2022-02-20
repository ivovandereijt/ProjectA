import requests
from tkinter import *
import math

stad_naam = "Gorinchem,NL"
api_key = "f8ccf64854137d00cc5f1fb68c99c6fc"

def get_weather(api_key, stad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={stad}&appid={api_key}"

    response = requests.get(url).json()

    temp = response['main']['temp']
    temp = math.floor((temp - 272))

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like - 272))

    humidity = response['main']['humidity']


    return {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity
    }

weer = get_weather(api_key, stad_naam)


root = Tk()
root.geometry("300x300")
root.title(f'{stad_naam[:-3]} weer')

def display_stad_naam(stad):
    stad_label = Label(root, text=f"{stad_naam[:-3]}" )
    stad_label.config(font=("Consolas", 28))
    stad_label.pack(side= 'top')

def display_stats(weer):
    temp = Label(root, text=f"Temperatuur:{weer['temp']} °C")
    feels_like = Label(root, text=f"Voelt als:  {weer['feels_like']} °C")
    humidity = Label(root, text=f"Vochtigheid:  {weer['humidity']}% ")

    temp.config(font=("Consolas", 18))
    feels_like.config(font=("Consolas", 16))
    humidity.config(font=("Consolas", 16))

    temp.pack(side='top')
    feels_like.pack(side='top')
    humidity.pack(side='top')

display_stad_naam(stad_naam)
display_stats(weer)
mainloop()