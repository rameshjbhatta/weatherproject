from django.shortcuts import render
import requests
from django.contrib import messages

# def login(request):
#     if request.method == 'POST':
        
    


def tempInCel(kel_value):
    celsius_value = kel_value - 273.15
    return round(celsius_value, 2)

def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city_name']
        api_key = 'f3b91a342fed4f9a32e494273278888a'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'  #f string format
        response = requests.get(url) #parse the json file
        response = response.json()
        if response['cod'] == 200:
            temp = response['main']['temp'] #extract data from respons
            temp=tempInCel(temp)
            lon = response['coord']['lon']
            lat = response['coord']['lat']
            name = response['name']
            humidity = response['main']['humidity']
            wind = response['wind']['speed']
            weather_condition = response['weather'][0]['main']  # Weather condition data
            coord={
                'lon':lon,
                'lat':lat
            }
            data = {                   
                'temp': temp,
                'coord': coord,
                'name': name,
                'humidity': humidity,
                'wind':wind,
                'city':city,
                'weather_condition':weather_condition
            }
            messages.success(request,'Congrats data found!!')
            return render(request, 'weatherapp/weather.html', {'data': data})
        else:
            messages.warning(request,'The entered city  is not in our database ')
            
    return render(request, 'weatherapp/index.html')
