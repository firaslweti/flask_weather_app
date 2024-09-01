Weather App
A simple weather application built with Flask, HTML, and CSS that provides current weather information based on user input or detected location. The app features modern animations to visually represent different weather conditions.

Features
Location Detection: Automatically detects the user's location using their IP address.
User Input: Allows users to manually enter a city to get weather information.
Weather Animations: Displays Lottie animations based on weather conditions (e.g., clouds, clear skies).
Responsive Design: Designed to be responsive and look great on various devices.
Technologies Used
Flask: Web framework for building the application.
HTML/CSS: For building the user interface and styling.
Lottie: For animations representing different weather conditions.
OpenWeatherMap API: For fetching weather data.
IPInfo API: For detecting user's location based on IP address.
OpenCage Geocoding API: For converting geographic coordinates to a city name.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/weather-app.git
cd weather-app
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory of the project and add your API keys:

makefile
Copy code
OPENWEATHER_API_KEY=your_openweathermap_api_key
OPENCAGE_API_KEY=your_opencage_api_key
Run the application:

bash
Copy code
python app.py
Open your browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
Usage
Default Location: When the app loads, it will attempt to detect your location automatically and display the weather information for your city.
Manual Input: Enter a city name into the input field and click "Get Weather" to retrieve weather information for that location.
Project Structure
app.py: The main Flask application file.
templates/: Contains HTML files used by Flask.
index.html: The main template for the weather app.
static/: Contains static files such as CSS, JavaScript, and Lottie animation JSON files.
styles.css: The main stylesheet.
loader.json: Loader animation.
clouds.json: Clouds animation.
clear.json: Clear skies animation.
.env: Environment variables file (not included in the repo).
Contributing
Fork the repository.
Create a feature branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
LottieFiles for the animations.
OpenWeatherMap for the weather data.
IPInfo for IP-based location detection.
OpenCage for geocoding services.
