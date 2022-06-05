from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("weather App")
root.geometry ("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        clock.place(x=90,y=120)
        name.config(text="CURRENT WEATHER")
        name.place(x=90,y=95)

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e8bc5be69fb7dde8780bb0681fce3ed2"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°C"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))

        w.config(text=(wind,"km/h"))
        h.config(text=(humidity,"%"))
        d.config(text=description)
        p.config(text=(pressure,"hPa"))

    except Exception as e:
        messagebox.showerror("Weather App","Invalid entry !!")

#Search box
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=70,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=100,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=450,y=34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=200,y=100)

#Bottom box
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=40,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=130,y=410)

label1=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=260,y=410)

label1=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=440,y=410)

label1=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=660,y=410)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=450,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=450,y=250)

w=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")   
w.place(x=130,y=435)
h=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")
h.place(x=260,y=435)
d=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")
d.place(x=440,y=435)
p=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")
p.place(x=660,y=435)


root.mainloop()
