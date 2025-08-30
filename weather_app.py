import requests
from datetime import datetime
import pytz

api_key="beab0307196303f569285ee10eeea633"

user_input = input("Enter city name: ")
#print(user_input)
#get_weather(user_input)app

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
#print(weather_data.status_code)
#print(weather_data.json())


if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    description = weather_data.json()['weather'][0]['description']
    temp = round(weather_data.json()['main']['temp'])
    sunset_timestamp = weather_data.json()['sys']['sunset']
    sunrise_timestamp = weather_data.json()['sys']['sunrise']

    # Get the IST timezone object
    ist = pytz.timezone('Asia/Kolkata')

# Convert the UTC timestamps to IST-aware datetime objects
    sunrise_ist = datetime.fromtimestamp(sunrise_timestamp, tz=ist)
    sunset_ist = datetime.fromtimestamp(sunset_timestamp, tz=ist)
  
# Format the datetime objects into a readable string
# "%Y-%m-%d %H:%M:%S %Z%z" shows the year, month, day, hour, minute, second,
# timezone abbreviation (IST), and UTC offset (+0530)
    sunrise_formatted = sunrise_ist.strftime("%H:%M:%S %Y-%m-%d %Z")
    sunset_formatted = sunset_ist.strftime("%H:%M:%S %Y-%m-%d %Z")
    print("\n\n============================================================")
    print(f"The Weather in {user_input} is: {weather}")
    print(f"The Temperature in {user_input} is: {temp}ºC")
    print(f"Weather description: {description}")
    print(f"Sunrise time: {sunrise_formatted}")
    print(f"Sunset time: {sunset_formatted}")
    print("============================================================\n\n")
    #print(weather_data.json())
