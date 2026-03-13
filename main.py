import os
from dotenv import load_dotenv
import requests
import time
import json
load_dotenv()

start_time = time.time()

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
 
end_time = time.time()
input_time = end_time - start_time
print(f"Время выполнения: {input_time:.2f} секунд")
response = requests.get(base_url, params=params)
elapsed = response.elapsed.total_seconds()
    
print(f"Время запроса: {elapsed:.2f} секунд")