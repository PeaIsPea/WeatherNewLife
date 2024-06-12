import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap

#hàm lấy thông tin weather from openweatherMap API
def get_weather(city):
    API_key = "2fa42e02d25a282909e1b898d9190720"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    if res.status_code == 404:
        messagebox.showerror("Error","City not found")

    weather  = res.json()
    icon_id = weather['weather'][0]["icon"]
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url,temperature,description,city,country)

#hàm tìm city
def search():
    city = city_entry.get()
    res = get_weather(city)
    if res is None:
        return
    icon_url,temperature,description,city,country = res
    location_label.configure(text=f"{city},{country}")
    image= Image.open(requests.get(icon_url,stream = True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon
    

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")


root = ttkbootstrap.Window(themename="morph")
root.title("WeatherNewLife")
root.geometry("600x700")

city_entry = ttkbootstrap.Entry(root, font="ROBOTO, 18")
city_entry.pack(pady=10)

search_btn = ttkbootstrap.Button(root, text="Search", command=search, bootstyle = "warning")
search_btn.pack(pady=10)


location_label = tk.Label(root, font="ROBOTO, 25")
location_label.pack(pady=20)
icon_label = tk.Label(root)

icon_label.pack()

temperature_label = tk.Label(root,font="ROBOTO, 20")
temperature_label.pack()

description_label = tk.Label(root,font="ROBOTO, 20")
description_label.pack()

root.mainloop()