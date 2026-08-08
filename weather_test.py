import requests

api_key = "f7f97b0f2564eb5931828adf6a718a91"
city = "PuneXYZ123"
units = "metric"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q":city,
    "appid":api_key,
    "units":units
}


try:
    response = requests.get(url,params=params)
    response.raise_for_status()
    print("Request sucessfull")

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    weather_message = f"The temperature in Pune is {temperature} degrees Celsius ,with {description}. Humidity is {humidity} % ."

    print(weather_message)
    

except requests.RequestException:
    print("Exception happend !!")




