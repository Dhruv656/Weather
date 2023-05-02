import requests
api_key = "2f7baa6e335553ea1ca4d8924a6a769b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
data = response.json()
if data["cod"] != "404":
    main = data["main"]
    temperature = main["temp"]
    temperature_celsius = round(temperature - 273.15, 2)
    weather = data["weather"]
    weather_description = weather[0]["description"]
    print(f"Temperature: {temperature_celsius}°C")
    print(f"Weather description: {weather_description}")
else:
    print("City not found.")
