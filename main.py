import os
from dotenv import load_dotenv
import requests

load_dotenv()

base_url = "http://api.openweathermap.org/data/2.5/weather"
city_name = input("Введите название города и страну через запятую: ")

if city_name == "":
    city_name = "London, uk"

api_key = os.getenv("API_KEY")

params = {
    "q": city_name,
    "appid": api_key
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
 