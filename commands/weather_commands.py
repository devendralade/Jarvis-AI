import os
import requests

from dotenv import load_dotenv
from speech import speak


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"


def weather_control(command):
    command = command.lower()

    weather_keywords = [
        "what is the weather in",
        "weather in"
    ]

    for keyword in weather_keywords:

        if keyword in command:

            city = command.split(keyword, 1)[1].strip()

            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            try:
                response = requests.get(URL, params=params)
                response.raise_for_status()

                data = response.json()

                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"]

                speak(
                    f"The temperature in {city} is "
                    f"{temperature} degrees Celsius, "
                    f"with {description}. "
                    f"Humidity is {humidity} percent."
                )

            except requests.RequestException:
                speak("Sorry, I couldn't get the weather.")

            return True

    return False