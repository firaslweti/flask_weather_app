import requests

api_key = 'd12644ba686140fd2cc2ea17fed47f9c'

# Get the user's IP address
ip_request = requests.get('https://api.ipify.org?format=json')
ip_address = ip_request.json()['ip']

# Use the IP address to get the user's location
location_request = requests.get(f'https://ipinfo.io/{ip_address}/json')
location_data = location_request.json()
city = location_data['city']

# Fetch the weather data using the detected city
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {city} is: {weather}")
    print(f"The temperature in {city} is: {temp}ºF")
