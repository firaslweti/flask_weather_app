from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
api_key = 'd12644ba686140fd2cc2ea17fed47f9c'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('location')
    else:
        # Get user's IP address
        ip_request = requests.get('https://api.ipify.org?format=json')
        ip_address = ip_request.json()['ip']

        # Get location details from IP
        location_request = requests.get(f'https://ipinfo.io/{ip_address}/json')
        location_data = location_request.json()
        city = location_data['city']

    # Fetch weather data for the detected or input city
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    
    if weather_data.json()['cod'] == '404':
        weather = None
        temp = None
        error = "City not found!"
        animation = None  # No weather animation
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp_fahrenheit = weather_data.json()['main']['temp']
        temp_celsius = round((temp_fahrenheit - 32) * 5 / 9)
        error = None

        # Determine the appropriate animation
        if 'Clouds' in weather:
            animation = 'clouds.json'
        elif 'Clear' in weather:
            animation = 'clear.json'
        else:
            animation = None  # No weather animation

    return render_template('index.html', city=city, weather=weather, temp=temp_celsius, error=error, animation=animation)

if __name__ == '__main__':
    app.run(debug=True)
