from tkinter import *
import requests
import tkinter.messagebox

base = Tk()
base.title("Weather Info")
base.config(bg='light blue')

def weather_response_format(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = int(weather['main']['temp'] - 273)  
        
        display_str = 'City   : %s \nConditions : %s \nTemperature(°C): %s ' % (name, desc, temp) 
    except:
        display_str = '''Sorry!
        Invalid City Name, Please try again!'''  

    return display_str


def get_weather(city):
    weather_key = '14ed2a78adcbcbfe1ac9d1ffb8c5eea6'  
    url = 'https://api.openweathermap.org/data/2.5/weather'  
    params = {'APPID': weather_key, 'q': city}
    weather_response = requests.get(url, params=params)
    weather = weather_response.json()
    


    label['text'] = weather_response_format(weather)
 


HEIGHT, WIDTH = 600, 600
canvas = Canvas(base, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = Frame(base, bg='black', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame,bg='brown' ,font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)


button = Button(frame, text="Get Weather", font=('Aria', 12),bg='light grey',command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = Frame(base, bg='light yellow', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, background="light yellow", font=('Courier', 18))
label.place(relwidth=1, relheight=1)






base.mainloop()