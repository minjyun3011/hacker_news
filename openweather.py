import requests


def open_weather(api_key, city_name):
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(api_url)

    # 天気情報の取得に成功した場合
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        print(f"In {city_name}, the weather is {weather_description} with a temperature of {temperature}°C.")
    else:
        print("Failed to retrieve weather data.")
        print(f"HTTP Status Code: {response.status_code}")


if __name__ == "__main__":
    api_key = "aede1a7aae2aa8aa8a7ea6a67331ef28"
    city_name = "Tokyo"
    open_weather(api_key, city_name)

